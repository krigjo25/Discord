#   Python Repositories
from os import getenv
import random

#   Dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord import Intents

# pyLib Repositories

#   System module
from pylib.systemModule.help import HelpCommand                                             #   Help module
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


def botSetup ():

     #  Necsessary values from .env
    botKey = getenv('BotTokenTest')
    

            #   Discord configs
    intents= Intents().default()         #  Allows default intents
    
    intents.members = True           #  Retrieve guild Members
    #intents.messages = True         #  Allows the bot to send messages
    #intents.presences = True        #
    #intents.guild_reactions = True  #

    #   retrieving the module
    bot = DiscordBot()#intents=intents)

    #   System Modules
    bot.add_cog(HelpCommand(bot))
    bot.add_cog(ErrorHandler(bot))

    #   Community - module
    bot.add_cog(Community(bot))

    #   miniGames
    bot.add_cog(EightBall(bot))
    bot.add_cog(JumbleGame(bot))
    bot.add_cog(GuessTheNumber(bot))
    bot.add_cog(RockScissorPaper(bot))

    bot.run(botKey)

if __name__ == '__main__':
    botSetup()