import feedparser

def CNNNews():
    d = feedparser.parse('http://rss.cnn.com/rss/edition_world.rss')
    print (d.feed.description)

CNNNews()