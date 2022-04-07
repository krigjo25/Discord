#   Python Repositories
from os import getenv

#   Dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord import Intents

# library Repositories

#   System module


from pylib.systemModule.welcome import Welcome                            #   Welcome Module 
from pylib.systemModule.help import HelpCommand                           #   Help module
from pylib.systemModule.krigjo25bot import DiscordBot                     #   The Client
from pylib.systemModule.commandError import ErrorHandler                  #   Error Handling Module

#   Community Module
from pylib.communityModule.community import Community                     #   Community module

#   RSS-Feed Module

#   Cnn News
from pylib.streamModule.rssFeed.cnnNews import CnnWorld, CnnMisc

#   Music module

#   Video-Stream

#   miniGames Repositories
from pylib.gameModule.miniGamesModule.askQ import EightBall                          #   EightBall
from pylib.gameModule.miniGamesModule.jumble import JumbleGame                       #   Jumble Game
from pylib.gameModule.miniGamesModule.int import GuessTheNumber                      #   Guess the number
from pylib.gameModule.miniGamesModule.reactGame import RockScissorPaper              #   Rock, Scissors & Paper

# Bot Utility

    #   Bot Anti-spam
#from lib.BotModerationModule.antiSpam import AntiSpam

    # Moderation Utility
from pylib.postModerationModule.moderator import Moderator                #   Moderator Module
from pylib.postModerationModule.administrator import Administrator        #   Administrator module


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

    #   System Module
    bot.add_cog(Welcome(bot))
    bot.add_cog(HelpCommand(bot))
    bot.add_cog(ErrorHandler(bot))

    #   Community - module
    bot.add_cog(Community(bot))

    #   Game-Module
    #   miniGames
    bot.add_cog(EightBall(bot))
    bot.add_cog(JumbleGame(bot))
    bot.add_cog(GuessTheNumber(bot))
    bot.add_cog(RockScissorPaper(bot))
    
    #   Moderation - Module
    #bot.add_cog(Anti-Spam(bot))
    bot.add_cog(Moderator(bot))
    bot.add_cog(Administrator(bot))

    #   Stream - Module

    #   Youtube


    #   Spotify


    #   SoundCloud


    #   RSS-Feeds

    #   Cnn News
    bot.add_cog(CnnMisc(bot))
    bot.add_cog(CnnWorld(bot))
    #bot.add_cog(CnnSport(bot))
    #bot.add_cog(CnnEntertainment(bot))

    #   BBC News

    #   Pandamic News

    #   Games News

    bot.run(botKey)

if __name__ == '__main__':
    botSetup()