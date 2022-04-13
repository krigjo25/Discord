
#   Discord Repositories
from discord import Intents

#   pylib Repositories

#   System module
from pylib.systemModule.welcome import Welcome                            #   Welcome Module 
from pylib.systemModule.help import HelpCommand                           #   Help module
from pylib.systemModule.discordBot import DiscordBot                     #   The Client
from pylib.systemModule.commandError import ErrorHandler                  #   Error Handling Module

#   Community Module
from pylib.communityModule.community import Community                     #   Community module


    # Moderation Utility
from pylib.postModerationModule.moderator import Moderator                #   Moderator Module
from pylib.postModerationModule.administrator import Administrator        #   Administrator module

class DiscordSetup():

    def __init__(self) -> None:
        self.bot = DiscordBot(intents = self.intents)


    def SystemConfigurations(self):

        #   Intents
        self.intents = Intents.all()
            
        #intents.members = True          # 
        #intents.messages = True         #
        #intents.presences = True        #
        #intents.guild_reactions = True  #

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

