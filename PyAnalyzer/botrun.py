#   Importing responsories needed for the project
from os import getenv
from dotenv import load_dotenv

from lib.system.botSetup import DiscordSetup


load_dotenv()
def RunBot ():
        
        #   Initializing classes
        disc = DiscordSetup()

        disc.Analyzer()
        disc.SystemSetup()
        disc.bot.run(getenv("Token"))


if __name__ == '__main__':
    RunBot()