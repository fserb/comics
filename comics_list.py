
comics = [
  ( "Dilbert",
    "http://feeds.feedburner.com/DilbertDailyStrip",
    '&lt;img src="(http://dilbert.com/dyn/str_strip/.*?)"',
    "%s" ),

  ( "Pearls Before the Swine",
    "http://comics.com/pearls_before_swine/",
    '"(http://assets.*?full.gif)"',
    "%s" ),

  ( "Malvados",
    "http://malvados.com.br/",
    '<frame name="mainFrame" src="index(.*?)\.html">',
    "http://www.malvados.com.br/tirinha%s.gif" ),

  ( "BugBash",
    "http://www.bugbash.net/",
    '(http:\/\/www.bugbash.net\/strips\/bug-bash.*?gif)" ',
    "%s" ),

  ( "Piled Higher & Deeper",
    "http://www.phdcomics.com/comics.php",
    '<img src=(http:\/\/www.phdcomics.com\/comics\/archive\/phd.*?) ',
    "%s" ),

  ( "Laerte",
    "http://p.php.uol.com.br/laerte/index.php",
    'tiraNome="(.*?)"',
    "http://www2.uol.com.br/laerte/tiras/%s" ),

  ( "xkcd",
    "http://xkcd.com/",
    '<img src="(http:\/\/imgs\.xkcd\.com\/comics\/.*?)"',
    "%s" ),

  ( 'Wulffmorgenthaler',
    'http://www.wulffmorgenthaler.com/',
    'src="(striphandler.*?)"',
    'http://www.wulffmorgenthaler.com/%s' ),

  ( 'Indexed',
    'http://indexed.blogspot.com/',
    '<img style.*? src="(.*?)" .*?>',
    '%s'),

  ('The Perry Bible Fellowship',
   'http://pbfcomics.com',
   '<a href="\?cid=(.*?)"',
   'http://pbfcomics.com/archive_b/%s'),

  ('The Joy of Tech',
   'http://www.joyoftech.com/joyoftech/index.html',
   '<img src="(joyimages/.*?)" alt="The Joy of Tech comic"',
   'http://www.joyoftech.com/joyoftech/%s'),

  ('Pathetic Geek Stories',
   'http://www.patheticgeekstories.com/',
   '<img src="(/?archives/.*?/.*?)" ',
   'http://www.patheticgeekstories.com/%s'),

  ('Sinfest',
   'http://www.sinfest.net/',
   '<p align="center"><img src="(http://sinfest.net/comikaze/comics/.*?)" ',
   '%s'),

  ('Subnormality',
   'http://www.viruscomix.com/subnormality.html',
   '<img.*src="(.*?)"></span>',
   'http://www.viruscomix.com/%s'),

  ('See Mike Draw',
   'http://seemikedraw.wordpress.com/feed/',
   '<media:content url="(http://seemikedraw.files.wordpress.com.*?)"',
   '%s'),

  ('Cectic',
   'http://cectic.com/',
   '<img id="comic" .*?src="(.*?)"',
   'http://cectic.com/%s'),

  ('Bennett Editorial Cartoons',
   'http://www.timesfreepress.com/news/rss/bennett/',
   'img src="(.*?)"',
   '%s'),

  ('Noise to Signal',
   'http://feeds.feedburner.com/RobCottinghamCartoons',
   'img src="(http://www.socialsignal.com/.*?)"',
   '%s'),

  ('Abstruse Goose',
   'http://abstrusegoose.com/',
   'src="(http://abstrusegoose.com/strips/.*?)"',
   '%s'),

  ('Truck Bearing Kibble',
   'http://truckbearingkibble.com',
   '"(http://truckbearingkibble.com/images/comic/.*?\.jpg)"',
   '%s'),

    ]
