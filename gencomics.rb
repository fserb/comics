#!/usr/bin/env ruby

require './comics'

comic do
  title "xkcd"
  url "http://xkcd.com"
  img re /<img src="(http:\/\/imgs\.xkcd\.com\/comics\/.*?)"/
  comment re /<img src="http:\/\/imgs.xkcd.com\/comics.*?" title="(.*?)"/
end

comic do
  title "Saturday Morning Breakfast Cereal"
  feed "http://feeds.feedburner.com/smbc-comics/PvLb"
  img re /src="(http:\/\/www.smbc-comics.com\/.*?)"/
end

comic do
  title "Pearls Before Swine"
  url "http://www.gocomics.com/pearlsbeforeswine"
  img re /<img alt="Pearls Before Swine" [^>]*src="(.*?)"/
end

comic do
  title "Malvados"
  url "http://malvados.com.br/"
  re /"index(.*?)\.html"/
  img 'http://www.malvados.com.br/tirinha%s.jpg'
end

comic do
  title "PHD Comics"
  feed "http://www.phdcomics.com/gradfeed_justcomics.php"
  # it could be the full post...
  img re /src="(.*?)"/
end

comic do
  title "Wulffmorgenthaler"
  feed "http://feeds.feedburner.com/wulffmorgenthaler"
  img re /src="(.*?)"/
end

comic do
  title 'The Perry Bible Fellowship'
  feed 'http://pbfcomics.com/feed/feed.xml'
  post
end

comic do
  title 'Bennett Editorial Cartoons'
  url 'http://www.timesfreepress.com/news/opinion/cartoons/'
  re /src=.(http:\/\/media.timesfreepress.com\/img\/news\/tease\/.*?)_....\.jpg/
  img '%s.jpg'
end

comic do
  title 'Mau humor'
  feed 'http://www.oesquema.com.br/mauhumor/feed'
  img re /<a href="(.*?\/mundo.*?\.gif)"/
end


feed "newfeed.xml"

