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
from pylib.communityModule.community import Community                                       #   Community module

#   miniGames Module
from pylib.gameModule.miniGamesModule.EightBall.askQ import EightBall                       #   EightBall
from pylib.gameModule.miniGamesModule.jumbleGame.jumble import JumbleGame                   #   Jumble Game
from pylib.gameModule.miniGamesModule.integerGame.guessTheNumber import GuessTheNumber              #   Guess the number
from pylib.gameModule.miniGamesModule.reactionsGames.rockPaperScissors import RockScissorPaper       #   Rock, Scissors & Paper

# Importing .evn file
load_dotenv()

class DiscordSetup():

    def __init__(self) -> None:
        self.intents= Intents().default()               #  Only allows Default intents
        self.bot = DiscordBot(intents=self.intents)

        return

class DiscordSetup():

    def __init__(self) -> None:
        self.bot = DiscordBot()


    def SystemConfigurations(self):
        
        self.bot.add_cog(ErrorHandler(self.bot))
        self.bot.add_cog(FrequentlyAskedQuestions(self.bot))

        return

    def CommunityModule(self):

        self.bot.add_cog(Community(self.bot))

        return

    def GamersModule(self):
            #   miniGames
        self.bot.add_cog(EightBall(self.bot))
        self.bot.add_cog(JumbleGame(self.bot))
        self.bot.add_cog(GuessTheNumber(self.bot))
        self.bot.add_cog(RockScissorPaper(self.bot))

        return

def RSSBotStartConfiguration ():
        
        # necsessary values from .env
        disc = DiscordSetup()
        botKey = getenv('BotTokenTest')

        disc.SystemConfigurations()
        disc.CommunityModule()
        disc.GamersModule()

        disc.bot.run(botKey)

if __name__ == '__main__':
    RSSBotStartConfiguration()