#   Python Repositories
from os import getenv

#   Dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord import Intents


# pyBut Repositories


#   System module

from pylib.systemModule.help import HelpCommand, InternationalModule, NationalModule                                     #   Help module
from pylib.systemModule.discordBot import DiscordBot                                #   The Client
from pylib.systemModule.commandError import ErrorHandler                          #   Error Handling Module

#   Community Module
from pylib.communityModule.community import CommunityModule                       #   Community module

#   RSS-Feed Module

#   World News
from pylib.rssModule.international.cnn.cnnMisc import CnnMisc
from pylib.rssModule.international.cnn.cnnWorld import CnnWorld
from pylib.rssModule.international.cnn.cnnSports import CnnSport

#   National news
from pylib.rssModule.national.usNational import NationalNews
#from pylib.rssModule.gameNews.gameRadar import GamesRadar
#from pylib.rssModule.gameNews.metacritic import Metacritic
#from pylib.rssModule.gameNews.destructoid import Destructoid
#from pylib.rssModule.gameNews.gameInformer import GameInformer
#from pylib.rssModule.gameNews.nintendoLife import NintendoLife
#from pylib.rssModule.gameNews.christCenteredGamer import ChristCenteredGamer


# Importing .evn file
load_dotenv()


def botSetup ():
    
     # necsessary values from .env
    botKey = getenv('BotTokenTest')
    

            #   Discord configs
    intents= Intents().default()        #  Only allows Default intents
    
    #intents.members = True             #  Allows the bot to track member updates, fetch members
    #intents.messages = True            #  Allows the bot to send messages
    #intents.presences = True           #  Allows the bot to track member activty
    #intents.reactions = True           #  Allows the bot to react to a message

    #   Initializing classes

    bot = DiscordBot(intents=intents)

    #   System Module

    #   Help command
    bot.add_cog(HelpCommand(bot))
    bot.add_cog(InternationalModule(bot))
    bot.add_cog(NationalModule(bot))

    bot.add_cog(ErrorHandler(bot))

    #   Community - module
    bot.add_cog(CommunityModule(bot))
    #   International news
        #   Cnn News
    bot.add_cog(CnnMisc(bot))
    bot.add_cog(CnnWorld(bot))
    bot.add_cog(CnnSport(bot))

    #   NationalNews
    bot.add_cog(NationalNews(bot))

    bot.run(botKey)
    
    #rss.LoadXML(url)
    #rss.praseXML(url)
if __name__ == '__main__':
    botSetup()