#   Importing responsories needed for the project
from os import getenv
from dotenv import load_dotenv

from lib.system.botSetup import DiscordSetup


load_dotenv()
def RunBot ():
        
        #   Initializing classes

        disc = DiscordSetup()
        botKey = getenv('PyAnalyzeToken')

        disc.Analyzer()
        disc.SystemSetup()
        disc.bot.run('OTAzNjE5NzU5NTg3ODUyMzM4.YXvnew.D9Y7_8HfDPiaJTN6aci4HBSbRj0')


if __name__ == '__main__':
    RunBot()