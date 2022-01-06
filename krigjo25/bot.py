#   Python Repositories
from os import getenv

#   Dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord import Intents

# library Repositories
from lib.cog.welcome import Welcome                             #   Welcome Module 
#from lib.cog.support import Support                            #   The Support module
from lib.cog.help import HelpCommand                            #   Help module
from lib.clients.bot import DiscordBot                          #   Client
from lib.cog.community import Community                         #   Community module
from lib.cog.commandError import ErrorHandler                   #   Error Handling Module

#   miniGames Repositories
from lib.miniGames.askQ import EightBall                        #   EightBall
from lib.miniGames.jumble import JumbleGame                     #   Jumble Game
from lib.miniGames.int import GuessTheNumber                    #   Guess the number
from lib.miniGames.reactGame import RockScissorPaper            #   Rock, Scissors & Paper

# Bot Utility

    #   Bot Anti-spam
#from lib.BotModerationModule.antiSpam import AntiSpam

    # Moderation Utility
from lib.moderationModule.moderator import Moderator            #   Moderator Module
from lib.moderationModule.administrator import Administrator    #   Administrator module

# Importing .evn file
load_dotenv()


def botSetup ():
    
     # necsessary values from .env
    botKey = getenv('BotToken')
    

            #   Discord configs
    intents= Intents().all()         #  Allows every intents
    
    #intents.members = True          #  Allows to add a role.
    #intents.messages = True         #  Allows the bot to send messages
    #intents.presences = True        #
    #intents.guild_reactions = True  #

    #   retrieving the module
    bot = DiscordBot(intents=intents)

    #   Adding cogs into the bot
    bot.add_cog(Welcome(bot))
    bot.add_cog(Community(bot))
    bot.add_cog(HelpCommand(bot))
    #bot.add_cog(Support(bot))

    #   miniGames
    bot.add_cog(EightBall(bot))
    bot.add_cog(JumbleGame(bot))
    bot.add_cog(GuessTheNumber(bot))
    bot.add_cog(RockScissorPaper(bot))
    
    #   Moderation
    #bot.add_cog(Anti-Spam(bot))
    bot.add_cog(Moderator(bot))
    bot.add_cog(ErrorHandler(bot))
    bot.add_cog(Administrator(bot))

    bot.run(botKey)

if __name__ == '__main__':
    botSetup()