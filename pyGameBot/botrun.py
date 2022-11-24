
from os import getenv
from dotenv import load_dotenv

from pylib.systemModule.botSetup import DiscordSetup

load_dotenv()
def RunBot ():
        
        #   Initializing classes
        disc = DiscordSetup()
        botKey = getenv('PyGameBot')

        disc.SystemSetup()
        disc.GamersModule()
        disc.CommunityModule()

        disc.bot.run('PyGame')


if __name__ == '__main__':
    RunBot()