
#   Python Repositories
from os import getenv

#   Dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord import Intents


#   System module
from pylib.systemModule.faq import FrequentlyAskedQuestions, InternationalModule, NationalModule                                        #   Help module
from pylib.systemModule.discordSetup import DiscordBot                                                                        #   The Client
from pylib.systemModule.commandError import ErrorHandler                                                                    #   Error Handling Module

#   Community Module
from pylib.communityModule.community import CommunityModule                                                                 #   Community module

#   RSS-Feed Module

#   World News

#   America

#   CNN
from pylib.rssNews.international.cnn.cnnWorld import CNNWorld
from pylib.rssNews.international.cnn.cnnMisc import CNNMiscellaneous

#   CNBC
from pylib.rssNews.international.cnbc.cnbcWorld import CNBCWorld
from pylib.rssNews.international.cnbc.cnbcMisc import CNBCMiscellaneous

#   Europe
from pylib.rssNews.international.rt.rtWorld import RTWorld
from pylib.rssNews.international.euronews.euroMisc import EuroMisc
from pylib.rssNews.international.euronews.euroworld import EuroWorld
from pylib.rssNews.international.skyNews.skyWorld import SkyNewsWorld
from pylib.rssNews.international.france24.france24World import France24World

#   Asia
from pylib.rssNews.international.wion.wionWorld import WionWorld


#   National news

from pylib.rssNews.national.asiaNational import SouthAsiaNational
from pylib.rssNews.national.europeNational import FranceNational, SovietUnionNational
from pylib.rssNews.national.europeNational import UKNational
from pylib.rssNews.national.americaNational import USANational


# Importing .evn file
load_dotenv()

class DiscordSetup():

    def __init__(self):

<<<<<<< Updated upstream:pyRess/pylib/systemModule/botSetup.py
        self.intents = Intents()
        self.bot = DiscordBot(intents = self.SystemConfigurations())#SystemConfigurations)

        return

    def SystemConfigurations(self):

        self.intents.guilds = True                  #   Allows the bot to interect with guilds
        self.intents.emojis = True                  #   emoji, sticker related events
        self.intents.guild_messages = True                #   Allows thmessages Guild & DM
=======
        #self.appinfo = AppInfo()
        self.intents = Intents()
        self.bot = DiscordBot(intents=self.SystemConiguration())

        return

    def SystemConiguration(self):

        #   Bot intents
        self.intents.guilds = True                  #   Allows the bot to interect with guilds
        self.intents.emojis = True                  #   emoji, sticker related events
        self.intents.members = True                 #   Allows the bot to interact with members
        self.intents.messages = True                #   Allows thmessages Guild & DM
        self.intents.presences = True               #   Allows the bot to track member activty
>>>>>>> Stashed changes:pyRess/pyRess.py
        self.intents.message_content =True          #   Allows the bot to send embeded message
        self.intents.guild_reactions = True         #   Allows the bot to add reactions with-in the guild  

        return self.intents

    def SystemSetup(self):

        #   System Configuration
        #self.intents.messages = True            #  Allows the bot to send messages


        #   Help command
        self.bot.add_cog(ErrorHandler(self.bot))
        self.bot.add_cog(NationalModule(self.bot))
        self.bot.add_cog(InternationalModule(self.bot))
        self.bot.add_cog(FrequentlyAskedQuestions(self.bot))

        return

    #   RSS Module
    def InternationalNewsSetup(self):

        #   BBC News
        #        self.bot.add_cog(BBCWorld(self.bot))

        #   Cnn News
        self.bot.add_cog(CNNWorld(self.bot))
        self.bot.add_cog(CNNMiscellaneous(self.bot))

        #   CNBC News
        self.bot.add_cog(CNBCWorld(self.bot))
        self.bot.add_cog(CNBCMiscellaneous(self.bot))

        #   Euronews World
        self.bot.add_cog(EuroMisc(self.bot))
        self.bot.add_cog(EuroWorld(self.bot))

        #   France 24 World
        self.bot.add_cog(France24World(self.bot))

        #   RT World
        self.bot.add_cog(RTWorld(self.bot))

        #   SkyNews World
        self.bot.add_cog(SkyNewsWorld(self.bot))

        #   Wion World
        self.bot.add_cog(WionWorld(self.bot))

        return

    def NationalNewsSetup(self):

        #   America
        self.bot.add_cog(USANational(self.bot))

        #  Asia
        self.bot.add_cog(SouthAsiaNational(self.bot))

        #   Europe
        self.bot.add_cog(FranceNational(self.bot))
        self.bot.add_cog(SovietUnionNational(self.bot))
        self.bot.add_cog(UKNational(self.bot))
        return

    def Blogs(self):

        #        self.bot.add_cog(Blogs(self.bot))

        return

    def MiscModulesSetup(self):

        self.bot.add_cog(CommunityModule(self.bot))

        return
