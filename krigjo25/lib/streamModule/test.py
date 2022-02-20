import feedparser
from bs4 import BeautifulSoup

        #   Creating the feed
rssNews = feedparser.parse('http://rss.cnn.com/rss/edition.rss')
entries =  rssNews['entries']

        # looping through the RSS feed
for article in entries:
            
            #   Calling the soupd module
    soup = BeautifulSoup(article.summary)
    thumbNail = soup.find('img')['src']
        
print(article)
print(thumbNail)