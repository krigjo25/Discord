import feedparser
import re
from bs4 import BeautifulSoup

rssNews = feedparser.parse('http://rss.cnn.com/rss/edition.rss')
entries =  rssNews.entries
for artnr, article in enumerate(entries):
        summary = article.get('summary', 'None to show')
        image = article.get('image', 'No images')
        updated = rssNews.feed.get('updated', ' No Date to be shown')
        value = rssNews.feed.get('value' 'No values')
        author= rssNews.feed.publisher_detail.name#.get('author', 'Unkown')
        print (f"\n{article.title} | nr. {artnr}\n {image}\n{summary}\nLast Update:{updated}\n link:{article.link}\n By :{author}\n" )
        if artnr == 3:
                break
print(article)