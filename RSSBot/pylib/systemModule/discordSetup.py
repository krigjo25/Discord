
#   Discord Repositories
from discord import Intents

#   Python Responsories
from os import getenv

#   Dotenv Responsories
from dotenv import load_dotenv

#   System module
from pylib.systemModule.welcome import Welcome                            #   Welcome Module 
from pylib.systemModule.help import HelpCommand                           #   Help module
from pylib.systemModule.discordBot import DiscordBot                     #   The Client
from pylib.systemModule.commandError import ErrorHandler                  #   Error Handling Module

#   Community Module
from pylib.communityModule.community import Community                     #   Community module


#   Moderation Utility
from pylib.postModerationModule.moderatorModule.moderator import Moderator                #   Moderator Module
from pylib.postModerationModule.administratorModule.administrator import Administrator        #   Administrator module
load_dotenv()

class DiscordSetup():

    def __init__(self) -> None:
        self.bot = DiscordBot()


    def SystemConfigurations(self):

        self.bot.add_cog(Welcome(self.bot))
        self.bot.add_cog(HelpCommand(self.bot))
        self.bot.add_cog(ErrorHandler(self.bot))

        return

    def CommunityModule(self):

        self.bot.add_cog(Community(self.bot))

        return

    def PostModerationModule(self):
    
        self.bot.add_cog(Moderator(self.bot))
        self.bot.add_cog(Administrator(self.bot))

        return
