
#   Python Repositories
from os import getenv

#   Dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord import Intents

#   System module
from pylib.systemModule.help import HelpCommand, InternationalModule, NationalModule                                     #   Help module
from pylib.systemModule.discordBot import DiscordBot                                #   The Client
from pylib.systemModule.commandError import ErrorHandler                          #   Error Handling Module

#   Community Module
from pylib.communityModule.community import CommunityModule                       #   Community module

#   RSS-Feed Module

#   World News

#   CNN
from pylib.rssModule.international.cnn.cnnWorld import CNNWorld
#from pylib.rssModule.international.cnn.cnnSports import CNNSport
from pylib.rssModule.international.cnn.cnnMisc import CNNMiscellaneous

#   CNBC
from pylib.rssModule.international.cnbc.cnbcWorld import CNBCWorld
#from pylib.rssModule.international.cnn.cnnSports import CNBCSport
from pylib.rssModule.international.cnbc.cnbcMisc import CNBCMiscellaneous
#   National news
from pylib.rssModule.national.usNational import USANational



# Importing .evn file
load_dotenv()

class DiscordSetup():

    def __init__(self) -> None:
        self.intents= Intents().default()               #  Only allows Default intents
        self.bot = DiscordBot(intents=self.intents)

        return

    def SystemSetup(self):

        #   System Configuration
        #self.intents.members = True             #  Allows the bot to track member updates, fetch members
        #self.intents.messages = True            #  Allows the bot to send messages
        #self.intents.presences = True           #  Allows the bot to track member activty
        #self.intents.reactions = True           #  Allows the bot to react to a message

        #   Help command
        self.bot.add_cog(HelpCommand(self.bot))
        self.bot.add_cog(InternationalModule(self.bot))
        self.bot.add_cog(NationalModule(self.bot))

        self.bot.add_cog(ErrorHandler(self.bot))

        return

    #   RSS Module
    def InternationalNewsSetup(self):

        #   Cnn News
        self.bot.add_cog(CNNWorld(self.bot))
#        self.bot.add_cog(CNNSport(self.bot))
        self.bot.add_cog(CNNMiscellaneous(self.bot))

        #   CNBC News
        self.bot.add_cog(CNBCWorld(self.bot))
        self.bot.add_cog(CNBCMiscellaneous(self.bot))

        return

    def NationalNewsSetup(self):

        #   America
        self.bot.add_cog(USANational(self.bot))

        return

    def miscSetup(self):

        self.bot.add_cog(CommunityModule(self.bot))

        return

def RSSBotStartConfiguration ():
        
        # necsessary values from .env
        disc = DiscordSetup()
        botKey = getenv('BotTokenTest')

        disc.miscSetup()
        disc.SystemSetup()
        disc.NationalNewsSetup()
        disc.InternationalNewsSetup()

        disc.bot.run(botKey)
        
        #rss.LoadXML(url)
        #rss.praseXML(url)

if __name__ == '__main__':
    RSSBotStartConfiguration()