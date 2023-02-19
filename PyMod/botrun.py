#    Python responsories
from os import getenv
from dotenv import load_dotenv

#    Custom library
from pylib.systemModule.botSetup import DiscordSetup

load_dotenv()

def RunBot ():
        botKey = getenv('Token')  #  Bot Token
        
        disc = DiscordSetup()
        disc.SystemSetup()
        disc.ModerationSetup()

        disc.bot.run(botKey)

if __name__ == '__main__':
    RunBot()
