
#   Python Responsories
import time

#   Selenium Responsories
from selenium.webdriver import Chrome, Firefox, Edge, Safari
from selenium.webdriver.chrome.options import Options

class R2():

        """     R2
            Voting with-out prompting

        """
    def __init__(self):
        self.EdgeDriver = Edge()
        self.SafariDriver = Safari()
        self.firefoxDriver = Firefox()
        self.chromeDriver = Chrome('D:\\Jottacloud\\Projects\\Coding\\Discord\\ScrapingBots\\webDriver\chromedriver')

        return

    #   Voting 
    def Vote(self):

        #   Initializing variables
        link = 'https://eaff.eu/bg/online-festival-vote-choice/30'


        self.chromeDriver.get(link)

        time.sleep(1)

        self.chromeDriver.close()

        return

while True:
    r2 = R2
    r2.Vote()