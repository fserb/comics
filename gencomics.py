#!/usr/bin/env python2.5
"""
Generates comics.xml RSS feeds

TODO:
- debug mode
- send regular "debug" updates
"""

import re, urllib, thread, time, socket, datetime, sys, sha, os
import feedparser
import PyRSS2Gen as RSS2

#import fspcomics

Baselink = 'http://fserb.com.br/comics.xml'

debug = False

comics = [
    ( "Dilbert",
      "http://www.dilbert.com",
      '<IMG SRC=\"\/(comics\/dilbert\/archive\/images\/dilbert.*?)" ALT=\"Today\'s Comic\"',
      "http://www.dilbert.com/%s" ),
    ( "Pearls Before the Swine",
      "http://www.comics.com/comics/pearls/",
      '<IMG SRC="\/(comics\/pearls\/archive\/images\/pearls.*?)"',
      "http://www.comics.com/%s" ),
    ( "Malvados",
      "http://www.malvados.com.br/",
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
    ( "Penny Arcade",
      "http://www.penny-arcade.com/comic",
      'src="/(images/200.*?)"',
       "http://www.penny-arcade.com/%s" ),
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
    ('IdiotBox',
     'http://www.mattbors.com/newstrip.html',
     '<img src="strips/(.*?)" ',
     'http://www.mattbors.com/strips/%s'),
    ('Allan Sieber',
     'http://talktohimselfshow.zip.net/',
     '<IMG.*?src="(http://talktohimselfshow.zip.net/images/.*?)".*>',
     'cache:%s'),
    ('Pathetic Geek Stories',
     'http://www.patheticgeekstories.com/',
     '<img src="(archives/recentstrips/.*?)" ',
     'http://www.patheticgeekstories.com/%s'),
    ('Sinfest',
     'http://www.sinfest.net/',
     '<p align="center"><img src="(http://sinfest.net/comikaze/comics/.*?)" ',
     '%s'),
    ]


def getURL(url):
  for _ in range(5):
    try:
      d = urllib.urlopen(url).read()
    except:
      d = ""
      continue
    break
  return d


def cache(url):
  global debug
  url_name, ext = os.path.splitext(url)
  cache_name = sha.new(url_name).hexdigest() + ext
  cache_url = "http://fserb.com.br/comicscache/" + cache_name
  if debug:
    print "Caching: %s (%s)" % (url, cache_name),
  if os.path.isfile('cache/'+cache_name):
    if debug:
      print "hit"
    return cache_url
  if debug:
    print "retrieve"
  for _ in range(5):
    try:
      urllib.urlretrieve(url, 'cache/'+cache_name)
    except:
      continue
    break
  return cache_url


def getNewComics():
  global debug
  ret = []
  errors = []

  def getSingle(title, url, regexp, linkp):
    ans = ()
    try:
      page = getURL(url)
      link = linkp % re.findall(regexp, page)[0]
      if link.startswith('cache:'):
          link = cache(link[6:])
      ans = (title, link, datetime.datetime.now())
      if debug:
        print (ans[0], ans[1])
    except:
      if debug:
        print "error:", title
      errors.append(title)
    finally:
      ret.append(ans)

  for c in comics:
    thread.start_new_thread(getSingle, c)

  while len(ret)<len(comics):
    time.sleep(1)


  return ([ x for x in ret if x ], errors)


def getFSPComics():
  for name, url in fspcomics.fspcomics():
    if debug:
      print "UOL:", (name, url)
    yield (name, url, datetime.datetime.now())


def loadEntries():
  return [ (e.title.encode('utf-8'), e.link, e.date)
        for e in feedparser.parse("comics.xml").entries ]


def main():
  global debug
  if len(sys.argv) > 1:
    debug = 'd' in sys.argv[1]
    remove_errors = 'e' in sys.argv[1]
  else:
    debug = False
    remove_errors = False

  socket.setdefaulttimeout(5)
  old = loadEntries()
  new, errors = getNewComics()
  #new.extend(getFSPComics())

  links = [ x[1] for x in old ]

  if errors:
    err = ['Error in comics:<ul>']
    err.extend('<li>%s' % x for x in errors)
    err.append('</ul>')
    err = ''.join(err)
    if not err in links:
      old.insert(0, ('Comics status', err, datetime.datetime.now()))

  for n in new:
    if not n[1] in links:
      old.insert(0,n)

  if debug:
    print
    print "RSS Output:"
    print

  items = []
  for title, link, date in old[:50]:
    if debug:
      if type(date) == unicode:
        d = datetime.datetime.strptime(date,
                         '%a, %d %b %Y %H:%M:%S GMT')
      else:
        d = date
      print '%04d-%02d-%02d - %s' % (d.year,
                       d.month,
                       d.day,
                       title)
    if title == "Comics status":
      if not remove_errors:
        items.append( RSS2.RSSItem( title = title,
                      link = link,
                      description = link + errmsg,
                      guid = RSS2.Guid(link),
                      pubDate = date) )
    else:
      items.append( RSS2.RSSItem( title = title,
                    link = link,
                    description = '<img src="%s">' % link,
                    guid = RSS2.Guid(link),
                    pubDate = date) )

  rss = RSS2.RSS2(
    title = "Comics",
    link = "http://fserb.com.br/comics.xml",
    description = "Comics feeds for the masses",
    lastBuildDate = datetime.datetime.now(),
    items = items)

  rss.write_xml(open("comics.xml", "w"), encoding='utf-8')

errmsg = """
<br>
Your friendly comics administrator will take care of that
as soon as possible. :)
"""

if __name__ == "__main__":
  main()
