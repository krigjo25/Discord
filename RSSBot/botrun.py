
#   Python Responsories
from os import getenv

#   Dotenv Responsories
from dotenv import load_dotenv

#   pylib Responsories
from pylib.systemModule.discordBot import DiscordBot        #   Discord Client
from pylib.systemModule.discordSetup import DiscordSetup    #   DiscordSetup

#   Discord Responsories
from discord import Intents

load_dotenv()

def Runbut ():
    
     # necsessary values from .env
    botKey = getenv('BotToken')

    #   Intents
    intents = Intents.all()

    #intents.members = True          # 
    #intents.messages = True         #
    #intents.presences = True        #
    #intents.guild_reactions = True  #

    #   Iniztalate classes
    setupbut = DiscordSetup()
    but = DiscordBot(intents=intents)

    setupbut.CommunityModule()
    setupbut.SystemConfigurations()
    setupbut.PostModerationModule()
    but.run(botKey)

if __name__ == '__main__':
    Runbut()
