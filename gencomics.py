#!/usr/bin/env python
"""
Generates comics.xml RSS feed

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
from collections import defaultdict

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

  def getSingle(title, url, regexp, linkp, textexp=None):
    ans = ()
    try:
      page = getURL(url)
      if regexp:
        link = linkp % re.findall(regexp, page)[0]
      else:
        link = ""
      if textexp:
        text = re.findall(textexp, page, re.S)[0]
        ans = (title, link, datetime.datetime.now(), text)
        print '%s: %s *' % (ans[0], ans[1])
      else:
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
  for e in feedparser.parse("http://www.luizirber.org/rss/fsp.xml").entries:
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
  ret = []
  for e in feedparser.parse("comics.xml").entries:
    o = (e.title.encode('utf-8'), 
         e.link,
         e.date,
         e.description)
    ret.append(o)
  return ret


def main():
  socket.setdefaulttimeout(5)
  old = loadEntries()
  new = []
  new.extend(getFSPComics())
  new.extend(getNewComics())

  links = [ x[1] for x in old ]

  for n in new:
    if not n[1] in links:
      if len(n) == 3:
        desc = '<img src="%s">' % n[1]
      else:
        if n[1]:
          desc = '<img src="%s">' % n[1]
        else:
          desc = ''
        desc += '<p>%s' % n[3]

      old.insert(0, (n[0], n[1], n[2], desc))

  firstocc = defaultdict(lambda: len(old))
  for i, (title, _, _, _) in enumerate(old):
    firstocc[title] = min(firstocc[title], i)

  firstocc = set(firstocc.values())

  items = []
  for i, (title, link, date, description) in enumerate(old):
    if i > 75 and i not in firstocc:
      continue
    items.append( RSS2.RSSItem( title = title,
                                link = link,
                                description = description,
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
