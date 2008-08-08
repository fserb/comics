#!/usr/bin/env python2.5
"""
Generates comics.xml RSS feeds

add:
http://truckbearingkibble.com/comic
http://abstrusegoose.com/
http://www.timesfreepress.com/news/rss/bennett/
http://www.socialsignal.com/noise-to-signal

remove:
sinfest
"""

import re, urllib, thread, time, socket, datetime, sys, sha, os
import feedparser
import PyRSS2Gen as RSS2

#import fspcomics

Baselink = 'http://fserb.com.br/comics.xml'

comics = [
  ( "Dilbert",
    "http://feeds.feedburner.com/DilbertDailyStrip",
    '&lt;img src="(http://dilbert.com/dyn/str_strip/.*?)"',
    "%s" ),
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
   'http://www.viruscomix.com/rss.xml',
   '<link>(http://www.viruscomix.com/.*?\.jpg)</link>',
   '%s'),
  ('See Mike Draw',
   'http://seemikedraw.wordpress.com/feed/',
   '<media:content url="(http://seemikedraw.files.wordpress.com.*?)"',
   '%s'),
  ('Cectic',
   'http://cectic.com/',
   '<img id="comic" .*?src="(.*?)"',
   'http://cectic.com/%s'),
    ]


def getURL(url):
  for _ in range(2):
    try:
      d = urllib.urlopen(url).read()
    except:
      d = ""
      continue
    break
  return d

def getNewComics():
  ret = []

  def getSingle(title, url, regexp, linkp):
    ans = ()
    try:
      page = getURL(url)
      link = linkp % re.findall(regexp, page)[0]
      ans = (title, link, datetime.datetime.now())
      print '%s: %s' % (ans[0], ans[1])
    except:
      print "%s: error" % title
    finally:
      ret.append(ans)

  for c in comics:
    thread.start_new_thread(getSingle, c)

  timelapse = 0
  while len(ret)<len(comics):
    time.sleep(1)
    timelapse += 1
    if timelapse >= 60:
      break


  return [ x for x in ret if x ]


def getFSPComics():
  ret = []
  for e in feedparser.parse("http://leandrosiqueira.com/quadrinhos/rss/").entries:
    try:
      img = re.findall('img src="(.*?)"', e.description)[0]
      ret.append( (e.title, img, datetime.datetime.now()))
      print "%s: %s" % (e.title.split('-',1)[0], img)
    except:
      pass
  return ret[:10]


def loadEntries():
  return [ (e.title.encode('utf-8'), e.link, e.date)
        for e in feedparser.parse("comics.xml").entries ]


def main():
  socket.setdefaulttimeout(5)
  old = loadEntries()
  new = []
  new.extend(getFSPComics())
  new.extend(getNewComics())

  links = [ x[1] for x in old ]

  for n in new:
    if not n[1] in links:
      old.insert(0,n)

  items = []
  for title, link, date in old[:100]:
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


if __name__ == "__main__":
  import traprss
  traprss.trytrap()
  try:
    main()
  finally:
    traprss.untrap("comics_debug.xml")
