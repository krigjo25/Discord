#    Python responsories
from os import getenv
from dotenv import load_dotenv

#    Custom library
from pylib.systemModule.botSetup import DiscordSetup

load_dotenv()

def RunBot ():

        """
                #        
        """
        # necsessary values from .env
        botKey = getenv('Token')

        DiscordSetup().SystemSetup()
        DiscordSetup().MiscModuleSetup()
        DiscordSetup().ModerationSetup()

        DiscordSetup().bot.run(botKey)

if __name__ == '__main__':
    RunBot()