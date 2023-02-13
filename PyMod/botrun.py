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
        #  Bot Token
        botKey = getenv('Token')

        #  Adding the cogs
        
        disc = DiscordSetup()
        disc.SystemSetup()
        disc.MiscModuleSetup()
        disc.ModerationSetup()

        disc.bot.run(botKey)

if __name__ == '__main__':
    RunBot()