comics = [
  ("Dilbert",
   "http://feeds.feedburner.com/DilbertDailyStrip",
   '&lt;img src="(http://dilbert.com/dyn/str_strip/.*?)"',
   "%s"),

  ("Pearls Before the Swine",
   "http://comics.com/pearls_before_swine/",
   'img src="(http://.*?full.gif)"',
   "%s"),

  ("Malvados",
   "http://malvados.com.br/",
   'index(.*?)\.html"',
   "http://www.malvados.com.br/tirinha%s.jpg"),


  ("Piled Higher & Deeper",
   "http://www.phdcomics.com/comics.php",
   '<img src=(http:\/\/www.phdcomics.com\/comics\/archive\/phd.*?) ',
   "%s"),

  ("Laerte",
   "http://p.php.uol.com.br/laerte/index.php",
   'tiraNome="(.*?)"',
   "http://www2.uol.com.br/laerte/tiras/%s"),

  ("xkcd",
   "http://xkcd.com/",
   '<img src="(http:\/\/imgs\.xkcd\.com\/comics\/.*?)"',
   "%s",
   '<img src="http://imgs.xkcd.com/comics.*?" title="(.*?)"'),

  ('Wulffmorgenthaler',
   'http://www.wulffmorgenthaler.com/',
   'src="(striphandler.*?)"',
   'http://www.wulffmorgenthaler.com/%s'),

  ('Indexed',
   'http://thisisindexed.com/',
   'src="(http://thisisindexed.com/wp-content/.*?\.jpg)"',
   '%s'),

  ('The Perry Bible Fellowship',
   'http://pbfcomics.com',
   '<a href="\?cid=(.*?)"',
   'http://pbfcomics.com/archive_b/%s'),

  ('Pathetic Geek Stories',
   'http://www.patheticgeekstories.com/',
   '<img src="(/?archives/.*?/.*?)" ',
   'http://www.patheticgeekstories.com/%s'),

  ('See Mike Draw',
   'http://seemikedraw.wordpress.com/feed/',
   '<media:content url="(http://seemikedraw.files.wordpress.com.*?)"',
   '%s'),

  ('Cectic',
   'http://cectic.com/',
   '<img id="comic" .*?src="(.*?)"',
   'http://cectic.com/%s'),

  ('Bennett Editorial Cartoons',
   'http://www.timesfreepress.com/news/opinion/cartoons/',
   'img .*? src="(.*?img/news/.*?)_[^_]*\.jpg\?.*?"',
   '%s.jpg'),

  ('Truck Bearing Kibble',
   'http://truckbearingkibble.com',
   '"(http://truckbearingkibble.com/images/comic/.*?\.jpg)"',
   '%s'),

  ('Wagner & Beethoven',
   'http://wagnerebeethoven.apostos.com/feed/',
   '',
   '',
   '<content:encoded><!\[CDATA\[(.*?)\]\]></content:encoded>'),

  ('Saturday Morning Breakfast Cereal',
   'http://www.smbc-comics.com/rss.php',
   '<img src="(.*?)">',
   '%s'),

  ('PartiallyClips',
   'http://www.partiallyclips.com/',
   '(http://partiallyclips.com/comics/.*?.jpg)',
   '%s'),

  ('Pictures for sad children',
   'http://picturesforsadchildren.com/',
   'img src="(.*?comics.*?)"',
   '%s'),

  ('New Yorker Cartoons',
   'http://feeds.feedburner.com/cartoonbank',
   'src="(.*?\.jpg)\?',
   '%s'),

  ('Wondermark',
   'http://wondermark.com',
   '<img src="(.*?)"',
   '%s'),

  ('Savage Chickens',
   'http://www.savagechickens.com/category/cartoons',
   '<img src="(http://www.savagechickens.com/images/chicken.*?)" alt="Savage',
   '%s'),
  
  ('Lefty Cartoons',
   'http://www.leftycartoons.com/feed/',
   '<p><img src="(.*?)"',
   '%s'),

  ('En dosis diarias',
   'http://www.dosisdiarias.com/',
   'src="(http://.*?\.jpg)" alt',
   '%s'),

  ('Macanudo',
   'http://autoliniers.blogspot.com/feeds/posts/default',
   'SRC="(http://.*?JPG)"',
   '%s'),

  ('Stuff No-one told me',
   'http://stuffnoonetoldme.blogspot.com/feeds/posts/default',
   r'&lt;img.*?src=[\'"]([^\'"]*?\.jpg)[\'"]',
   '%s'),
  
  ('Mau humor',
   'http://www.oesquema.com.br/mauhumor/',
   'href="(http://www.oesquema.com.br/mauhumor/wp-content/uploads/[^"]*?\.gif)"',
   '%s'),

  ('Non Sequitur',
   'http://www.gocomics.com/nonsequitur',
   '<link rel="image_src" href="(.*?)"',
   '%s'),

  ("BugBash",
   "http://www.bugbash.net/",
   '(http:\/\/www.bugbash.net\/strips\/bug-bash.*?gif)" ',
   "%s"),

  ('Vida Besta',
   'http://www.vidabesta.com/comicgallery.php',
   'src="(vidabesta/imagens/tiras/[^"]*?\.gif)"',
   'http://www.vidabesta.com/%s'),

  ]
