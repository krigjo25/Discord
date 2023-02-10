#   Python Repositories
#import requests

from os import getenv
from pyexpat.errors import messages

#   Dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord import Intents, AppInfo

# library Repositories

#   System module

from pylib.systemModule.discordBot import DiscordBot                                         #   The Bot Client
from pylib.systemModule.commandError import ErrorHandler                                     #   Error Handling Module
from pylib.systemModule.faq import FrequentlyAskedQuestions                                  #   Help module

#   Community Module
from pylib.communityModule.community import CommunityModule                                  #   Community module


# Bot Utility

    # Moderation Utility
from pylib.postModerationModule.moderatorModule.roleModeration import RoleModeration
from pylib.postModerationModule.moderatorModule.rolePermissions import RolePermissions
from pylib.postModerationModule.administratorModule.administrator import Administrator
from pylib.postModerationModule.moderatorModule.moderator import ChannelModeration, MemberModeration

# Importing .evn file
load_dotenv()

class DiscordSetup():

    """
        #   Discord bot configuration
        #   Cogs for the bot
    """
    def __init__(self):

        #self.appinfo = AppInfo()
        self.intents = Intents()
        self.bot = DiscordBot(intents=self.SystemConiguration())

        return

    def SystemConiguration(self):

        """
            #   Bot itents
        """
        #   Bot intents
        self.intents.bans = True                    #   Allows the bot to ban / unban members
        self.intents.guilds = True                  #   Allows the bot to interect with guilds
        self.intents.emojis = True                  #   emoji, sticker related events
        self.intents.members = True                 #   Allows the bot to interact with members
        self.intents.messages = True                #   Allows thmessages Guild & DM
        self.intents.presences = True               #   Allows the bot to track member activty
        self.intents.message_content =True          #   Allows the bot to send embeded message
        self.intents.guild_reactions = True         #   Allows the bot to add reactions with-in the guild  

        return self.intents

    def SystemSetup(self):

        #   Add Cogs
        self.bot.add_cog(ErrorHandler(self.bot))
        self.bot.add_cog(FrequentlyAskedQuestions(self.bot))

        return

    def ModerationSetup(self):

        #   Admin - Module
        self.bot.add_cog(Administrator(self.bot))

        #   Role Moderation
        self.bot.add_cog(RoleModeration(self.bot))
        self.bot.add_cog(RolePermissions(self.bot))

        #   Other modules
        self.bot.add_cog(MemberModeration(self.bot))
        self.bot.add_cog(ChannelModeration(self.bot))


        return

    def MiscModuleSetup(self):

        #   Community module
        self.bot.add_cog(CommunityModule(self.bot))

        return