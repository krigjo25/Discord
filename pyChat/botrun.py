
from os import getenv
from dotenv import load_dotenv

from pylib.systemModule.botSetup import DiscordSetup

load_dotenv()

def RunBot ():

        #   Initializing classes
        disc = DiscordSetup()

        disc.SystemSetup()

        botKey = getenv('PyChatToken')

        disc.bot.run(botKey)


if __name__ == '__main__':
    RunBot()