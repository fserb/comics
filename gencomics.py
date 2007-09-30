#!/usr/bin/python2.4
# Generate comics.xml

import re, urllib, thread, time, socket, datetime
import feedparser
import PyRSS2Gen as RSS2


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
    ( "PC Weenies",
      "http://www.pcweenies.org/",
      'SRC="/(images/toons/pc.*?)"',
      "http://www.pcweenies.org/%s" ),
    ( 'Wulffmorgenthaler',
      'http://www.wulffmorgenthaler.com/',
      'src="(striphandler.*?)"',
      'http://www.wulffmorgenthaler.com/%s' ),
    ( 'Cubicle Gangsters',
      'http://www.cubiclegangsters.com/xml/comics.rss.xml',
      '<guid>(http://www.cubiclegangsters.com/comics/.*?)</guid>',
      '%s' ),
    ( 'A Softer World',
      'http://www.asofterworld.com/',
      '<IMG SRC="(http://www.asofterworld.com/.*?)"',
      '%s' ),
    ( 'Butter Nut Squash',
      'http://www.butternutsquash.net/assets/pages/bns-current.html',
      '<img src="../(library.*?)"',
      'http://www.butternutsquash.net/assets/%s' ),
    ( 'User Friendly',
      'http://ars.userfriendly.org/cartoons/',
      'src="(http://www.userfriendly.org/cartoons/archives/.*?)"',
      '%s' ),
    ]

def getNewComics():

    ret = []

    def getSingle(title, url, regexp, link):
        try:
            for _ in range(5):
                try:
                    d = urllib.urlopen(url).read()
                except:
                    d = ""
                    continue
                break
        
            x = re.findall(regexp, d)[0]
        
            ans = (title, link % x, datetime.datetime.now())
            #print ans
            ret.append(ans)
        except:
   	    ret.append(()) 
    for c in comics:
        thread.start_new_thread(getSingle, c)

    while len(ret)<len(comics):
        time.sleep(1)
            
    return [ x for x in ret if x ]

def loadEntries():
    return [ (e.title, e.link, e.date) for e in feedparser.parse("comics.xml").entries ]


def main():
    socket.setdefaulttimeout(5)
    new = getNewComics()
    old = loadEntries()

    links = [ x[1] for x in old ]
    
    for n in new:
        if not n[1] in links:
            old.insert(0,n)
            #print n

    items = []
    for title, link, date in old[:50]:
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
    
    rss.write_xml(open("comics.xml", "w"))
    

if __name__ == "__main__":
    main()
