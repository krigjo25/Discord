
from os import getenv
from dotenv import load_dotenv

from pylib.systemModule.botSetup import DiscordSetup

load_dotenv()
def RunBot ():

        # necsessary values from .env
        disc = DiscordSetup()
        botKey = getenv('PyModToken')

        disc.SystemSetup()
        disc.MiscModuleSetup()
        disc.ModerationSetup()

        disc.bot.run(botKey)

if __name__ == '__main__':
    RunBot()