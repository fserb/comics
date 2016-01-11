#!/usr/bin/env ruby
# encoding: utf-8

require './comics'

backfeed "all.xml"
feed "newfeed.xml"
backmail "mail.xml"

comic do
  title "Sharksplode"
  feed "http://sharksplode.com/feed/"
  post
end

comic do
  title "My Extra Life"
  feed "http://www.myextralife.com/feed/"
  post
end

comic do
  title "Amazing Super Powers"
  feed "http://feeds.feedburner.com/amazingsuperpowers"
  re /(<img.*?>)/
end

comic do
  title "Abominable"
  feed "http://abominable.cc/rss"
  post
end

comic do
  title "Poorly Drawn Lines"
  feed "http://feeds.feedburner.com/PoorlyDrawnLines"
  post
end

comic do
  title "Saturday Morning Breakfast Cereal"
  feed "http://www.smbc-comics.com/rss.php"
  img re /src="(http:\/\/www.smbc-comics.com\/comics\/.*?)"/
end

comic do
  title 'Bennett Editorial Cartoons'
  url 'http://www.timesfreepress.com/news/opinion/cartoons/'
  img re /src="(http:\/\/media-cdn.timesfreepress.com\/img\/photos\/.*\.jpg?)"/
end

comic do
  title "xkcd"
  url "http://xkcd.com"
  img re /<img src="(\/\/imgs\.xkcd\.com\/comics\/.*?)"/
  comment re /<img src="\/\/imgs.xkcd.com\/comics.*?" title="(.*?)"/
end

comic do
  title 'Non Sequitur'
  url 'http://www.gocomics.com/nonsequitur'
  img re /<img alt="Non Sequitur" [^>]*src="(.*?)"/
end

comic do
  title "Malvados"
  url "http://malvados.com.br/"
  re /"index(.*?)\.html"/
  img 'http://www.malvados.com.br/tirinha%s.jpg'
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
  title 'Vida Besta'
  url 'http://www.vidabesta.com/comicgallery.php'
  re /src="(vidabesta\/imagens\/tiras\/[^\"]*?\.gif)"/
  img 'http://www.vidabesta.com/%s'
end

comic do
  title "O Pintinho"
  feed 'http://opintinho.tumblr.com/rss'
  post
end

comic do
  title 'Savage Chickens'
  url 'http://www.savagechickens.com/category/cartoons/feed'
  re /(<img.*?>)/
end

comic do
  title 'Manual do Minotauro'
  feed 'http://manualdominotauro.blogspot.com/feeds/posts/default?alt=rss'
  img re /href="(.*?)"/
end

comic do
  title "Calvin and Hobbes"
  feed 'http://calvinhobbesdaily.tumblr.com/rss'
  post
end

comic do
  title "Peanuts"
  url 'http://www.gocomics.com/peanuts'
  img re /<img alt="Peanuts" [^>]*src="(.*?)"/
end

comic do
  title "Adão Iturrusgarai"
  feed 'http://adao-tiras.rssblog.uol.com.br'
  re /(<img.*?>)/
end

comic do
  title 'Muriel'
  feed 'http://murieltotal.rssblog.zip.net'
  re /(<img.*?>)/
end

comic do
  title 'Incidental Commics'
  feed 'http://www.incidentalcomics.com/feeds/posts/default'
  post
end

comic do
  title "You're all just jealous of my jetpack"
  feed "http://myjetpack.tumblr.com/rss"
  post
end

comic do
  title "Moonbeard"
  feed "http://moonbeard.com/feed/atom/"
  img re /<img src="(.*?)"/
end

comic do
  title "Safely Endangered"
  feed "http://www.safelyendangered.com/feed/"
  img re /<img.*?src="(.*?)" class="attachment-full wp-post-image"/
end
