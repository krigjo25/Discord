
from os import getenv
from dotenv import load_dotenv

from pylib.systemModule.botSetup import DiscordSetup

load_dotenv()
def RunBot ():
        
        #   Initializing classes
        disc = DiscordSetup()
        botKey = getenv('BotTokenTest')

        disc.SystemSetup()

        disc.bot.run(botKey)


if __name__ == '__main__':
    RunBot()