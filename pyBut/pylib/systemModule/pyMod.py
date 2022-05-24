
#   Client
from pylib.systemModule.discordBot import DiscordBot

# Bot Utility

    # Moderation Utility
from pylib.postModerationModule.moderatorModule.moderator import Moderator                  #   Moderator Module
from pylib.postModerationModule.administratorModule.administrator import Administrator          #   Administrator module

class PyMod():

    def __init__(self):

        self.bot = DiscordBot()

        return

    def PyMod(self):

    #   Moderation - Module
        self.bot.add_cog(Moderator(self.bot))
        self.bot.add_cog(Administrator(self.bot))

        return