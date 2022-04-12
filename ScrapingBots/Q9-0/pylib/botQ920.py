
#   Python Responsories
import csv
import time
import xml.etree.ElementTree as ET

#   Selenium Responsories
from selenium.webdriver import Chrome, Firefox, Edge, Safari

from selenium.webdriver.chrome.options import Options

import requests

class Q90():

    """         Created following tutorials

            Q9-0 Votes in competitions, scrapes XML files 
            Working as RSS reader
    """

    #   Initializing the configurations for Chrome Crawler
    chromeOptions = Options()                               #   Calling the Options class
    chromeOptions.headless = True                           #   Does not open the browser

    def __init__(self):

        #self.EdgeDriver = Edge('D:\\Jottacloud\\Projects\\Coding\\Discord\\ScrapingBots\\webDriver\edgedriver', options=self.edgeOptions)
        #self.firefoxDriver = Firefox('D:\\Jottacloud\\Projects\\Coding\\Discord\\ScrapingBots\\webDriver\firefoxdriver', options=self.firefoxOptions)
        self.chromeDriver = Chrome('D:\\Jottacloud\\Projects\\Coding\\Discord\\ScrapingBots\\webDriver\chromedriver', options=self.chromeOptions)
        self.name = 'Q92-0 Crawler'

        return

    def CompetitionVote(self):

        """
                Q9-0 
        Voting with-out prompting

        """

        #   Initializing variables
        link = 'https://eaff.eu/bg/online-festival-vote-choice/30'
        
        self.chromeDriver.get(link)

        time.sleep(1)

        #   Closing the driver
        self.chromeDriver.close()

        return