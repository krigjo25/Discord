
from os import getenv
from dotenv import load_dotenv

from pylib.systemModule.botSetup import DiscordSetup

load_dotenv()

def runBot ():
        
        #   Initializing classes
        disc = DiscordSetup()

        botKey = getenv('PyRessToken')

        disc.SystemSetup()
        disc.MiscModulesSetup()
        disc.NationalNewsSetup()
        disc.InternationalNewsSetup()

        disc.bot.run(botKey)

if __name__ == '__main__':
    runBot()