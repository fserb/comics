=begin

Base utility to create a comics file

=end

require 'rss'
require 'open-uri'
require 'htmlentities'
require 'digest/sha1'
require 'thread'

class Grabber
  attr_accessor :content, :time, :page, :page_title, :guid

  # Grabber is a @content stack, a @title and some downladed @page.
  def initialize
    @title = ""
    @content = []
    @page = ""
    @time = nil
    @guid = nil
  end

  def to_s
    "< #{@title} : \n#{@content * '\n'} >"
  end

  def get_link
    (get_content.scan /(https?:\/\/[^"'>]*)/)[0][0]
  end

  def get_guid
    if not @guid then
      @guid = "//comic/#{Digest::SHA1.hexdigest (get_title + '/' + get_content)}"
    end
    @guid
  end

  def get_title
    @title.strip
  end

  def get_content
    @content * ''
  end

  def url(url)
    open url do |f|
      @page = f.read
    end
  end

  def title(title)
    @title = title
  end

  def feed(u)
    url u
    f = RSS::Parser.parse @page, false
    i = f.items[0]
    for m in [ :content_encoded, :description, :content, :summary ] do
      if i.respond_to? m and i.send(m) != nil then
        content = i.send(m)
        content = content.content if content.respond_to? :content
        content.strip!
        if content.length > 0 then
          @page = content
          return
        end
      end
    end
    raise "Not found"
  end

  def re(re)
    match = (@page.scan re)[0][0]
    @content.push match
    match
  end

  def add_or_replace(s)
    if s.include? '%s'
      @content.push(s % @content.pop)
    else
      @content.push s
    end
  end

  def img(s="%s")
    @content.pop if @content.last == s
    add_or_replace "<img src='#{s}'>"
  end

  def comment(s="%s")
    @content.pop if @content.last == s
    add_or_replace "<p>#{s}"
  end

  def post
    @content.push HTMLEntities.new.decode @page
  end

end

@feedname = ''
@backfeedname = ''
@data = []
@threads = []

@putsemaphore = Mutex.new

def comic(&name)
  @threads << Thread.new {
    cr = Grabber.new
    begin
      cr.instance_eval &name
      @data.push cr
      @putsemaphore.synchronize {
        puts "Done: " + cr.get_title
      }
    rescue
      @putsemaphore.synchronize {
        puts "Exception for: " + cr.get_title
        raise
      }
    end
  }
end

def load_old_file(filename)
  # Load old file
  if FileTest.exists? filename then
    open filename do |rss|
      feed = RSS::Parser.parse rss
      feed.items.each do |item|
        cr = Grabber.new
        cr.title item.title
        cr.content.push item.description
        cr.time = item.date
        @data.push cr
      end
    end
  end
end

def cleanup
  # Sort by time
  now = Time.now
  @data.sort_by! { |i| [i.time ? i.time : now, i.get_title] }
  @data.reverse!

  # Remove duplicates
  tc = {}
  @data.each do |i|
    tc[i.get_guid] = [] if not tc.key? i.get_guid
    tc[i.get_guid].push i
  end
  tc.each do |k, v|
    v[0..-2].each do |i|
      @data.delete i
    end
  end
end

def save filename
  now = Time.now
  puts "Saving: #{filename} with #{@data.length} entries"

  rss = RSS::Maker.make "rss2.0" do |maker|
    maker.channel.author = 'Fernando Serboncini'
    maker.channel.updated = now
    maker.channel.title = 'Comics'
    maker.channel.description = 'Comics feeds for the masses'
    maker.channel.link = filename

    @data.each do |cr|
      maker.items.new_item do |item|
        item.title = cr.get_title
        item.date = if cr.time then cr.time else now.to_s end
        item.description = cr.get_content
        item.link = cr.get_link
      end
    end
  end

  open(filename, "w") do |f|
    f.write(rss)
  end
end

def feed(filename)
  @feedname = filename
end

def backfeed filename
  @backfeedname = filename
end

def run
  @threads.each { |t| t.join }
  puts "Saving..."
  load_old_file @backfeedname
  cleanup
  @data = @data.take 10000
  save @backfeedname
  # Limit to 75 entries
  @data = @data.take 75
  save @feedname
end

at_exit { run }
