import feedparser

def trackNews():
    newsFeed = feedparser.parse('http://rss.cnn.com/rss/edition.rss')
    entry = newsFeed.entries[1]
    print(len(newsFeed.entries))
    print(entry.title)

trackNews()