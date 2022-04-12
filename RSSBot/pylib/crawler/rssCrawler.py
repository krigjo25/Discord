
#   Python Responsories
import os

from PIL import Image
from csv import DictWriter
from xml.etree import ElementTree as ET
from urllib.request import urlretrieve

#   Selenium Responsories

import requests

class Q90():
    """         Created following tutorials

            Q9-0 scrapes XML files 
            Working as RSS reader 
    """

    #   Initializing the configurations for Chrome Crawler

    def __init__(self):

                #   File paths
        self.csvPath = 'rssBot/pylib/crawler/docs/csv/topnewsfeed.csv'
        self.xmlPath = 'rssBot/pylib/crawler/docs/xml/topnewsfeed.xml'

        return

    def LoadXML(self, url):

        """         LoadXML()

                Loading the website,
                writing the website into a file with .xml 

        """

        #   Initializing a connection to the xml file
        req = requests.get(url)

        #   Saving the xml
        with open(f'{self.xmlPath}', 'wb') as f:
            f.write(req.content)

        return

    def praseXML(self):

        """         ParseXML
            Prasing through the xml file 
        """

        #   Initializing the ElementTree
        tree = ET.parse(self.xmlPath)
        rootree = tree.getroot()

        content = []

        #   Initializing a Dictionary for the news
        for item in rootree.findall('./channel/item'):
            newsItems = {}

            #   Initializing the child elemets of the content
            for child in item:
                print(child.tag)
                #   Checking for namespace object
                if child.tag == '{http://search.yahoo.com/mrss/}content':

                    newsItems['media'] = child.attrib['url']

                elif child.tag == '{http://www.w3.org/2005/Atom}link' or child.tag == '{http://purl.org/dc/elements/1.1/}creator' or child.tag == '{http://search.yahoo.com/mrss/}credit':
                        pass

                elif child.tag == '{http://search.yahoo.com/mrss/}description' or child.tag == 'guid' or child.tag == 'relatedGames' or child.tag == 'category':
                    pass
                    
                else:
                    print(child.tag)
                    newsItems[child.tag] = child.text.encode('utf-8')

            content.append(newsItems)

        #   Saving the xml file as csv
              #   Column names in .csv
        columns = ['category', 'title', 'pubDate', 'description', 'link', 'media']

        with open(self.csvPath, 'w') as csvf:

            author = DictWriter(csvf, fieldnames = columns)
            author.writeheader()
            author.writerows(content)

        #   After we're done we are cleaning up
        if os.path.exists(self.xmlPath): os.remove(f'{self.xmlPath}') 
        else: print('could not find the OS path')

        if newsItems['media'] != None:
            print( newsItems)

        return

    def openImage(self, url, name):

        imgPath = f'crawler/docs/pic/{name}'
        #   Downloading image
        urlretrieve(url, imgPath, name)

        #   Opens the image
        img = Image.open(name)
        img.show()
        if os.path.exists(self.xmlPath): os.remove(f'{imgPath}')

        return
