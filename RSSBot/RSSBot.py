#   Python Repositories
from os import getenv

#   Dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord import Intents


# library Repositories

#   System module

from pylib.systemModule.help import HelpCommand                           #   Help module
from pylib.systemModule.discordBot import DiscordBot                     #   The Client
from pylib.systemModule.commandError import ErrorHandler                  #   Error Handling Module

#   Community Module
from pylib.communityModule.community import Community                       #   Community module

#   RSS-Feed Module

#   World News
#   CNN
from pylib.rssModule.international.cnn.misc import CnnMisc
from pylib.rssModule.international.cnn.world import CnnWorld
from pylib.rssModule.international.cnn.sports import CnnSport

#   BBC

#   Game News
from pylib.rssModule.gameNews.gameSpot import GameSpot
#from pylib.rssModule.gameNews.gameRadar import GamesRadar
#from pylib.rssModule.gameNews.metacritic import Metacritic
#from pylib.rssModule.gameNews.destructoid import Destructoid
#from pylib.rssModule.gameNews.gameInformer import GameInformer
#from pylib.rssModule.gameNews.nintendoLife import NintendoLife
#from pylib.rssModule.gameNews.christCenteredGamer import ChristCenteredGamer

#   National news

#   USA
#from pylib.rssModule.national.unitedStatesofAmerica import UnitedStatesofAmerica

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

    #   retrieving the module
    bot = DiscordBot(intents=intents)

    #   System Module
    bot.add_cog(HelpCommand(bot))
    bot.add_cog(ErrorHandler(bot))

    #   Community - module
    bot.add_cog(Community(bot))

    #   Cnn News
    bot.add_cog(CnnMisc(bot))
    bot.add_cog(CnnWorld(bot))
    bot.add_cog(CnnSport(bot))

    #   Games News
    bot.add_cog(GameSpot(bot))
#    bot.add_cog(Metacritic(bot))
#    bot.add_cog(Destructoid(bot))
#    bot.add_cog(GameInformer(bot))
#    bot.add_cog(NintendoLife(bot))
#    bot.add_cog(ChristCenteredGamer(bot))


    #   NationalNews
    #bot.add_cog(UnitedStatesofAmerica(bot))


    bot.run(botKey)

if __name__ == '__main__':
    botSetup()