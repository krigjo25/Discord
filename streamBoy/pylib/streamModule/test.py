import feedparser
import re
from PIL import Image
import requests
from bs4 import BeautifulSoup

url = 'https://www.smp.no/kultur/i/z733lK/ny-cd-og-ny-jobb-for-annbjoerg-lien'
rssNews = feedparser.parse(url)
entries =  rssNews.entries

for artnr, article in enumerate(entries):

        summary = article.get('summary', 'There is no summary for this article')
        im = Image.open(requests.get(article.img_url, stream=True).raw)
        updated = rssNews.feed.get('updated', ' No Date to be shown')
        value = rssNews.feed.get('value' 'No values')
        author= rssNews.feed.get('author', 'Unkown')


        if summary != 'There is no summary for this article':
                print (f"\n{article.title} | nr. {artnr}\n{summary}\nLast Update:{updated}\n link:{article.link}\n By :{author}\n" )

        #if artnr == 3:
        #        break

print(article)