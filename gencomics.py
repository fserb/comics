#!/usr/bin/env python2.5
"""
Generates comics.xml RSS feed

Dependencies:
- feedparser
- PyRSS2Gen

Add comics:
- http://www.smbc-comics.com
- http://www.dieselsweeties.com
- http://www.explosm.net/comics
- http://wondermark.com
- http://www.medium-large.com/
- http://www.daniellecorsetto.com/gws.html
- http://www.partiallyclips.com
http://overcompensating.com
http://nobodyscores.loosenutstudio.com/
http://www.questionablecontent.net
http://www.chrisyates.net/reprographics/index.php
Wagner & Beethoven

Remove comics:
- sinfest

TODO:
- add support for ALT tags
- include link for the original page
- simplify RSS code
- separate language comics
- update config file to YAML?
"""

import PyRSS2Gen as RSS2
import feedparser

import datetime
import os
import re
import socket
import sys
import thread
import time
import urllib

from comics_list import comics

Baselink = 'http://fserb.com.br/comics.xml'


def getURL(url):
  """ Try to fetch a URL and fail silently.

  Args:
    url: url to be fetched

  Returns:
    URL content
  """
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
  """ Special type for FSP

  TODO: move to comics_list
  """
  ret = []
  for e in feedparser.parse("http://leandrosiqueira.com/quadrinhos/rss/").entries:
    try:
      img = re.findall('img src="(.*?)"', e.description)[0]
      ret.append( (e.title, img, datetime.datetime.now()))
      #print "%s: %s" % (e.title.split('-',1)[0], img)
    except:
      pass
  return ret[:10]


def loadEntries():
  """ Load old entries.from RSS
  """
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
    link = Baselink,
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
