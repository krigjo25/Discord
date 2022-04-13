
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

        self.bot.add_cog(Welcome(self.bot))
        self.bot.add_cog(HelpCommand(self.bot))
        self.bot.add_cog(ErrorHandler(self.bot))

        return

    def AdministrationSetup(self):

    #   Moderation - Module
        self.bot.add_cog(Moderator(self.bot))
        self.bot.add_cog(Administrator(self.bot))
        return

    def miniGamesSetup(self):

        #   Game-Module
            #   miniGames
        self.bot.add_cog(EightBall(self.bot))
        self.bot.add_cog(JumbleGame(self.bot))
        self.bot.add_cog(GuessTheNumber(self.bot))
        self.bot.add_cog(RockScissorPaper(self.bot))

        return

    def MiscModuleSetup(self):

        #   Community module
        self.bot.add_cog(CommunityModule(self.bot))

        return

def RSSBotStartConfiguration ():
        
        # necsessary values from .env
        bot = DiscordSetup()
        botKey = getenv('BotTokenTest')

        bot.SystemSetup()
        bot.miniGamesSetup()
        bot.MiscModuleSetup()
        bot.AdministrationSetup()


        bot.bot.run(botKey)
        
        #rss.LoadXML(url)
        #rss.praseXML(url)

if __name__ == '__main__':
    RSSBotStartConfiguration()