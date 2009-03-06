""" Helper functions to add debug RSS interface.

"""

import PyRSS2Gen as RSS2
import datetime
import feedparser
import sys
import StringIO


def trytrap():
  """
  Avoid trapping output when first argument is "-"
  """
  if len(sys.argv) > 1 and sys.argv[1] == '-':
    sys.argv.remove('-')
  else:
    trap()


def trap():
  """
  Trap stdout and stderr.
  """
  sys.stdout = StringIO.StringIO()
  sys.stderr = sys.stdout


def untrap(name):
  """ We update the debug rss @name with the new debug information.
  """
  # If we never trapped, do nothing.
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
                               description = (sys.stdout.getvalue()
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

  sys.stdout.close()
  sys.stdout = sys.__stdout__
  sys.stderr = sys.__stderr__


if __name__ == '__main__':
  try:
    trap()
    print "some info"
    untrap('x.xml')
  except:
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    raise
