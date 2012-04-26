=begin

Base utility to create a comics file

=end

require 'rss'
require 'open-uri'
require 'htmlentities'

class Grabber
  attr_accessor :content, :time, :page

  # Grabber is a @content stack, a @title and some downladed @page.
  def initialize
    @title = ""
    @content = []
    @page = ""
    @time = nil
  end

  def to_s
    "< #{@title} : \n#{@content * '\n'} >"
  end

  def get_title
    @title.strip
  end

  def get_content
    @content * '\n'
  end

  def url(url)
    puts "url: " + url
    open url do |f|
      @page = f.read
    end
  end

  def title(title)
    @title = title
  end

  def feed(u)
    url u
    f = RSS::Parser.parse @page
    i = f.items[0]
    for m in [ :content_encoded, :description, :content, :summary ] do
      if i.respond_to? m and i.send(m) != nil then
       content = (m == :summary ? i.send(m).content : i.send(m)).strip
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

@data = []

def comic(&name)
  cr = Grabber.new
  cr.instance_eval &name
  @data.push cr
end

def feed(filename)
  now = Time.now

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

  # Sort by time
  @data.sort_by { |i| i.time ? i.time : now }

  # Remove duplicates
  tc = {}
  @data.each do |i|
    k = i.get_title, i.get_content
    tc[k] = [] if not tc.key? k
    tc[k].push i
  end
  tc.each do |k, v|
    v[0..-2].each do |i|
      @data.delete i
    end
  end

  # Limit to 75 entries
  @data = @data.first 75

  puts "Saving: " + filename
  puts @data.length

  rss = RSS::Maker.make "rss2.0" do |maker|
    maker.channel.author = 'Fernando Serboncini'
    maker.channel.updated = now
    maker.channel.title = 'Comics'
    maker.channel.description = 'Comics feeds for the masses'
    maker.channel.link = filename

    @data.each do |cr|
      maker.items.new_item do |item|
        item.title = cr.get_title
        item.date = if cr.time then cr.time else now end
        item.description = cr.get_content
      end
    end

  end

  open(filename, "w") do |f|
    f.write(rss)
  end
end
