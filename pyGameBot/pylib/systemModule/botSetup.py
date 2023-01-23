#   Python Repositories
from os import getenv
import random

#   Dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord import Intents

# pyLib Repositories

#   System module
#   System module

from pylib.systemModule.discordBot import DiscordBot                                                    #   The Client
from pylib.systemModule.commandError import ErrorHandler                                                 #   Error Handling Module
from pylib.systemModule.frequentlyaskedquestions import FrequentlyAskedQuestions                         #   Help module



from pylib.systemModule.discordBot import DiscordBot                                        #   The Client#
from pylib.systemModule.commandError import ErrorHandler                                    #   Error Handling Module

#   Community Module
from pylib.communityModule.community import CommunityModule                                     #   Community module

#   miniGames Module
from pylib.minigames.intGames import MathGames
from pylib.minigames.wordGames import WordGames

# Importing .evn file
load_dotenv()

class DiscordSetup():

    def __init__(self):

        #self.appinfo = AppInfo()
        self.intents = Intents()
        self.bot = DiscordBot(intents=self.SystemConiguration())

        return

    def SystemConiguration(self):

        #   Bot intents
        self.intents.guilds = True                  #   Allows the bot to interect with guilds
        self.intents.emojis = True                  #   emoji, sticker related events
        self.intents.members = True                 #   Allows the bot to interact with members
        self.intents.messages = True                #   Allows the messages Guild & DM
        self.intents.presences = False               #   Allows the bot to track member activty
        self.intents.message_content =True          #   Allows the bot to send embeded message
        self.intents.guild_reactions = True         #   Allows the bot to add reactions with-in the guild  

        return self.intents


    def SystemSetup(self):
        
        self.bot.add_cog(ErrorHandler(self.bot))
        self.bot.add_cog(FrequentlyAskedQuestions(self.bot))

        return

    def CommunityModule(self):

        self.bot.add_cog(CommunityModule(self.bot))

        return

    def GamersModule(self):
            #   miniGames
        self.bot.add_cog(WordGames(self.bot))
        self.bot.add_cog(MathGames(self.bot))

        return