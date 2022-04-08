#   Python Repositories
from os import getenv

#   Dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord import Intents

# library Repositories

#   System module

from pylib.systemModule.help import HelpCommand                             #   Help module
from pylib.systemModule.discordBot import DiscordBot                        #   The Client
from pylib.systemModule.commandError import ErrorHandler                    #   Error Handling Module

#   Community Module
from pylib.communityModule.community import Community                       #   Community module

#   Support Module
#from pylib.streamModule.

#   Stream Module


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
    bot.add_cog(HelpCommand(bot))
    bot.add_cog(ErrorHandler(bot))

    #   Community - module
    bot.add_cog(Community(bot))

    #   Stream - Module

    #   Youtube


    #   Spotify


    #   SoundCloud

    bot.run(botKey)

if __name__ == '__main__':
    botSetup()