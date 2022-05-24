
#   miniGames Module
from pylib.gameModule.miniGamesModule.EightBall.askQ import EightBall                             #   EightBall
from pylib.gameModule.miniGamesModule.jumbleGame.jumble import JumbleGame                         #   Jumble Game
from pylib.gameModule.miniGamesModule.integerGame.guessTheNumber import GuessTheNumber            #   Guess the number
from pylib.gameModule.miniGamesModule.reactionsGames.rockPaperScissors import ReactionGame    #   Rock, Scissors & Paper

from pylib.systemModule.discordBot import DiscordBot


class PyGame():

    def __init__(self):

        self.bot = DiscordBot()

        return

    def PyGame(self):

        #   Game-Module
            #   miniGames
        self.bot.add_cog(EightBall(self.bot))
        self.bot.add_cog(JumbleGame(self.bot))
        self.bot.add_cog(GuessTheNumber(self.bot))
        #self.bot.add_cog(ReactionGame(self.bot))

        return