
#   Python Repositories
from os import getenv

#   Dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord import Intents

# library Repositories

#   System module
from pylib.systemModule.welcome import Welcome                              #   Welcome Module 
from pylib.systemModule.help import HelpCommand                             #   Help module
from pylib.systemModule.discordBot import DiscordBot                        #   The Client
from pylib.systemModule.commandError import ErrorHandler                    #   Error Handling Module

#   Community Module
from pylib.communityModule.community import CommunityModule                       #   Community module

#   miniGames Module
from pylib.gameModule.miniGamesModule.EightBall.askQ import EightBall                             #   EightBall
from pylib.gameModule.miniGamesModule.jumbleGame.jumble import JumbleGame                         #   Jumble Game
from pylib.gameModule.miniGamesModule.integerGame.guessTheNumber import GuessTheNumber            #   Guess the number
from pylib.gameModule.miniGamesModule.reactionsGames.rockPaperScissors import RockScissorPaper    #   Rock, Scissors & Paper

# Bot Utility

    #   Bot Anti-spam
#from lib.BotModerationModule.antiSpam import AntiSpam

    # Moderation Utility
from pylib.postModerationModule.moderatorModule.moderator import Moderator                  #   Moderator Module
from pylib.postModerationModule.administratorModule.administrator import Administrator          #   Administrator module


# Importing .evn file
load_dotenv()

class DiscordSetup():

    def __init__(self) -> None:
        self.intents= Intents().all()               #  Only allows Default intents
        self.bot = DiscordBot(intents=self.intents)

        return

    def SystemSetup(self):

        #   System Configuration
        #self.intents.members = True             #  Allows the bot to track member updates, fetch members
        #self.intents.messages = True            #  Allows the bot to send messages
        #self.intents.presences = True           #  Allows the bot to track member activty
        #self.intents.reactions = True           #  Allows the bot to react to a message

        self.bot.add_cog(Welcome(bot))
        self.bot.add_cog(HelpCommand(bot))
        self.bot.add_cog(ErrorHandler(bot))

        return

    def AdministrationSetup(self):

    #   Moderation - Module
        self.bot.add_cog(Moderator(bot))
        self.bot.add_cog(Administrator(bot))
        return

    def miniGamesSetup(self):

        #   Game-Module
            #   miniGames
        self.bot.add_cog(EightBall(bot))
        self.bot.add_cog(JumbleGame(bot))
        self.bot.add_cog(GuessTheNumber(bot))
        self.bot.add_cog(RockScissorPaper(bot))

        return

    def MiscModuleSetup(self):

        #   Community module
        self.bot.add_cog(CommunityModule(bot))

        return

    def RSSBotStartConfiguration (self):
        
        #   Necsessary values from .env
        botKey = getenv('BotToken')

        #   Initializing functions
        self.SystemSetup()
        self.miniGamesSetup()
        self.MiscModuleSetup()
        self.AdministrationSetup()

        #   Run the bot
        self.bot.run(botKey)

if __name__ == '__main__':

    bot = DiscordSetup()
    bot.RSSBotStartConfiguration()