
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
    "%s",
    '<img src="http://imgs.xkcd.com/comics.*?" title="(.*?)"' ),

  ( 'Wulffmorgenthaler',
    'http://www.wulffmorgenthaler.com/',
    'src="(striphandler.*?)"',
    'http://www.wulffmorgenthaler.com/%s' ),

  ( 'Indexed',
    'http://indexed.blogspot.com/',
    '<img style.*? src="(.*?)" .*?>',
    '%s' ),

  ( 'The Perry Bible Fellowship',
    'http://pbfcomics.com',
    '<a href="\?cid=(.*?)"',
    'http://pbfcomics.com/archive_b/%s' ),

  ( 'The Joy of Tech',
    'http://www.joyoftech.com/joyoftech/index.html',
    '<img src="(joyimages/.*?)" alt="The Joy of Tech comic"',
    'http://www.joyoftech.com/joyoftech/%s' ),

  ( 'Pathetic Geek Stories',
    'http://www.patheticgeekstories.com/',
    '<img src="(/?archives/.*?/.*?)" ',
    'http://www.patheticgeekstories.com/%s' ),

  ( 'Sinfest',
    'http://www.sinfest.net/',
    '<p align="center"><img src="(http://sinfest.net/comikaze/comics/.*?)" ',
    '%s' ),

  ( 'See Mike Draw',
    'http://seemikedraw.wordpress.com/feed/',
    '<media:content url="(http://seemikedraw.files.wordpress.com.*?)"',
    '%s' ),

  ( 'Cectic',
   'http://cectic.com/',
   '<img id="comic" .*?src="(.*?)"',
   'http://cectic.com/%s' ),

  ( 'Bennett Editorial Cartoons',
   'http://www.timesfreepress.com/news/opinion/cartoons/',
   'img .*? src="(.*?img/news/.*?)_[^_]*\.jpg\?.*?"',
   '%s.jpg' ),

  ( 'Noise to Signal',
   'http://feeds.feedburner.com/RobCottinghamCartoons',
   'img src="(http://www.socialsignal.com/.*?)"',
   '%s' ),

  ( 'Truck Bearing Kibble',
   'http://truckbearingkibble.com',
   '"(http://truckbearingkibble.com/images/comic/.*?\.jpg)"',
   '%s' ),

  ( 'Wagner & Beethoven',
   'http://www.apostos.com/wagnerebeethoven/atom.xml',
   '',
   '',
   '<content.*?<!\[CDATA\[(.*?)\]\]>' ),

  ( 'Saturday Morning Breakfast Cereal',
   'http://www.smbc-comics.com/rss.php',
    '<img src="(.*?)">',
   '%s' ),

  ( 'PartiallyClips',
   'http://www.partiallyclips.com/',
   'img src="(.*?storage.*?)"',
   '%s' ),

  ( 'Pictures for sad children',
   'http://picturesforsadchildren.com/',
   'img src="(.*?comics.*?)"',
   '%s' ),

  ( 'Bellen!',
   'http://boxbrown.com/',
   'img src="(.*?comics.*?)"',
   '%s' ),

  ( 'New Yorker Cartoons',
   'http://feeds.feedburner.com/cartoonbank',
   '&lt;img src="(.*?)"',
   '%s' ),

  ( 'Wondermark',
   'http://wondermark.com',
   '<img src="(.*?)"',
   '%s' ),

  ( 'Rehabilitating Mr.Wiggles',
    'http://www.mrwiggleslovesyou.com/',
    'img src="(comics.*?)"',
    'http://www.mrwiggleslovesyou.com/%s' ),

    ]
