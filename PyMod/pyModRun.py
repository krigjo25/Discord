
#   Python Repositories
import requests

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
from pylib.postModerationModule.moderatorModule.moderator import ChannelModeration, MemberModeration, ManageModeration

# Importing .evn file
load_dotenv()

class DiscordSetup():

    def __init__(self):

        self.intents= Intents().none()
        #self.appinfo = AppInfo()
        self.bot = DiscordBot(intents=self.intents)

        return

    def SystemSetup(self):

        #   System Configuration

        #   Intents
        self.intents.bans = True                    #   Allows the bot to ban / unban members
        self.intents.guilds = True                  #   Allows the bot to interect with guilds
        self.intents.members = True                 #   Allows the bot to interact with members
        self.intents.messages = True                #   Allows the bot to send messages Guild & DM
        self.intents.presences = True               #   Allows the bot to track member activty
        self.intents.message_content =True          #   Allows the bot to send embeded message
        self.intents.guild_reactions = True         #   Allows the bot to add reactions with-in the guild  
        self.intents.emojis = True                  #   emoji, sticker related events

        #   App Info 
        #self.appinfo.bot_public = False              #   Sets wheter the bot should be public or not 
        #self.appinfo.name = 'Pymodergf'
        #self.appinfo.verify_key = getenv('PyModToken')
        #self.appinfo.description = 'Test' #'I\'m your discord moderator command assistant, My intention is just to assist you in your discord server'
        #self.appinfo.privacy_policy_url = 'https://krigjo25.com/pymod/privacupolicy'
        #self.appinfo.terms_of_service_url = 'https://krigjo25.com/pymod/termsofservice'

        #print(self.appinfo)
        # Bot Profile

        #   Add Cogs
        self.bot.add_cog(ErrorHandler(self.bot))
        self.bot.add_cog(FrequentlyAskedQuestions(self.bot))

        return

    def ModerationSetup(self):

        #   Moderation - Module
        self.bot.add_cog(Administrator(self.bot))

        #   Role Moderation
        self.bot.add_cog(RoleModeration(self.bot))
        self.bot.add_cog(RolePermissions(self.bot))

        #   Other modules
        self.bot.add_cog(MemberModeration(self.bot))
        self.bot.add_cog(ChannelModeration(self.bot))
        self.bot.add_cog(ManageModeration(self.bot))


        return

    def MiscModuleSetup(self):

        #   Community module
        self.bot.add_cog(CommunityModule(self.bot))

        return

def RunBot ():

        # necsessary values from .env
        disc = DiscordSetup()
        botKey = getenv('PyModToken')

        disc.SystemSetup()
        disc.MiscModuleSetup()
        disc.ModerationSetup()

        disc.bot.run(botKey)

if __name__ == '__main__':
    RunBot()