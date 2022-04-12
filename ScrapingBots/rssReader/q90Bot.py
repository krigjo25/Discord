
#   pylib Responsories
from pylib.q90Reader import Q90

def runBot():

    #   Initializing class
    rss = Q90()

    url= 'https://rss.nytimes.com/services/xml/rss/nyt/NYRegion.xml'
    rss.LoadXML(url)

    rss.praseXML(url)

    return

if __name__ == '__main__':
    runBot()