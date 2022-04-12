import feedparser
import re
from PIL import Image
import requests
from bs4 import BeautifulSoup

url = 'https://www.smp.no/kultur/i/z733lK/ny-cd-og-ny-jobb-for-annbjoerg-lien'
rssNews = feedparser.parse('http://rss.cnn.com/rss/edition_sport.rss')
entries =  rssNews.entries
print(entries)


for artnr, article in enumerate(entries):
        print(article)
#   Searching for selected list items
        summary = article.get('summary', 'There is no summary for this article')
        updated = rssNews.feed.get('updated', ' No Date to be shown')

        if summary != 'There is no summary for this article':
                print(f'{artnr}. {article.title}\n', f'{summary[0:96]}\n ')

            #   Drop the loop when the counter is reached
                if artnr == 5:
                        break