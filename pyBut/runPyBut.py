
#   Python Repositories
from os import getenv

#   Dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from pyBut.pylib.systemModule.botSetup import DiscordSetup

# Importing .evn file
load_dotenv()


def RSSBotStartConfiguration ():
        
        # necsessary values from .env
        bot = DiscordSetup()
        botKey = getenv('BotTokenTest')

        bot.SystemSetup()
        bot.miniGamesSetup()
        bot.MiscModuleSetup()
        bot.AdministrationSetup()


        bot.bot.run(botKey)
        
        #rss.LoadXML(url)
        #rss.praseXML(url)

if __name__ == '__main__':
    RSSBotStartConfiguration()