
#   Python Repositories
from os import getenv

#   Dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord import Intents
from pylib.postModerationModule.moderatorModule.moderator import RolePermissions

# library Repositories

#   System module

from pylib.systemModule.discordBot import DiscordBot                                         #   The Bot Client
from pylib.systemModule.commandError import ErrorHandler                                     #   Error Handling Module
from pylib.systemModule.faq import FrequentlyAskedQuestions                                  #   Help module

#   Community Module
from pylib.communityModule.community import CommunityModule                                  #   Community module


# Bot Utility

    # Moderation Utility

from pylib.postModerationModule.administratorModule.administrator import Administrator
from pylib.postModerationModule.moderatorModule.moderator import RoleModeration, ChannelModeration, GeneralModeration, MemberModeration

# Importing .evn file
load_dotenv()

class DiscordSetup():

    def __init__(self):

        self.intents= Intents().none()
        self.bot = DiscordBot(intents=self.intents)

        return

    def SystemSetup(self):

        #   System Configuration

        self.intents.bans = True                #   Allows the bot to ban / unban members
        self.intents.emojis = True              #   Allows the bot to use emojis in the server
        self.intents.guilds = True              #   Allows the bot to interect with guilds
        self.intents.members = True             #   Allows the bot to interact with members
        self.intents.messages = True            #   Allows the bot to send messages Guild & DM
        self.intents.presences = True           #   Allows the bot to track member activty
        self.intents.message_content =True      #   Allows the bot to send embeded messages

        self.intents.reactions = True

        self.bot.add_cog(ErrorHandler(self.bot))
        self.bot.add_cog(FrequentlyAskedQuestions(self.bot))

        return

    def ModerationSetup(self):

        #   Moderation - Module
        self.bot.add_cog(Administrator(self.bot))
        self.bot.add_cog(RoleModeration(self.bot))
        self.bot.add_cog(RolePermissions(self.bot))

        self.bot.add_cog(MemberModeration(self.bot))
        self.bot.add_cog(ChannelModeration(self.bot))
        self.bot.add_cog(GeneralModeration(self.bot))


        return

    def MiscModuleSetup(self):

        #   Community module
        self.bot.add_cog(CommunityModule(self.bot))

        return

def RunBot ():

        # necsessary values from .env
        disc = DiscordSetup()
        botKey = getenv('PyMod')

        disc.SystemSetup()
        disc.MiscModuleSetup()
        disc.ModerationSetup()

        disc.bot.run(botKey)

if __name__ == '__main__':
    RunBot()