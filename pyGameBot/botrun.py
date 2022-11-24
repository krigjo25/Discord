
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

        disc.bot.run('OTc2NDgyOTUwNTgzNTUwMDAy.Gkt_29.igwWfxxjsThJAs7bDv2osREIV-UYw4hzDH-Kbo')


if __name__ == '__main__':
    RunBot()