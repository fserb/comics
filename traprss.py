import sys
import datetime

import feedparser
import PyRSS2Gen as RSS2

class Saver(object):
  def __init__(self):
    self.buffer = []

  def write(self, t):
    self.buffer.append(t)

  def flush(self): pass

def trytrap():
  if len(sys.argv) > 1 and sys.argv[1] == '-':
    sys.argv.remove('-')
  else:
    trap()

def trap():
  sys.stdout = Saver()
  sys.stderr = sys.stdout
  pass


def untrap(name):
  if sys.stdout == sys.__stdout__:
    return
  ent = []
  for e in feedparser.parse(name).entries:
    ent.append( RSS2.RSSItem( title = e.title,
                              link = e.link,
                              description = e.description,
                              guid = e.guid,
                              pubDate = e.date))

  ent = ent[:10]

  d = datetime.datetime.now()
  s = d.strftime('%d %b %Y - %H:%M')
  ent.insert(0,  RSS2.RSSItem( title = s,
                               link = "",
                               description = (''.join(sys.stdout.buffer)
                                              .replace('\n','<br>')),
                               guid = RSS2.Guid(s),
                               pubDate = d))

  rss = RSS2.RSS2(
    title = "Debug",
    link = "http://fserb.com.br/"+name,
    description = "Debug info",
    lastBuildDate = d,
    items = ent)

  rss.write_xml(open(name, "w"), encoding='utf-8')

  sys.stdout = sys.__stdout__
  sys.stderr = sys.__stderr__


if __name__ == '__main__':
  try:
    trap()
    print 2
    untrap('x.xml')
  except:
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    raise
