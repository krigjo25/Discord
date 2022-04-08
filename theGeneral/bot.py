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
from pylib.systemModule.discordBot import DiscordBot                     #   The Client
from pylib.systemModule.commandError import ErrorHandler                  #   Error Handling Module

#   Community Module
from pylib.communityModule.community import Community                     #   Community module



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
    botKey = getenv('BotTokenTest')
    

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
    
    #   Moderation - Module
    #bot.add_cog(Anti-Spam(bot))
    bot.add_cog(Moderator(bot))
    bot.add_cog(Administrator(bot))

    bot.run(botKey)

if __name__ == '__main__':
    botSetup()