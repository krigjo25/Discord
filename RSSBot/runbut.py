
#   Python Responsories
from os import getenv

#   Dotenv Responsories
from dotenv import load_dotenv

#   pylib Responsories
from pylib.systemModule.discordBot import DiscordBot        #   Discord Client
from pylib.systemModule.discordSetup import DiscordSetup    #   DiscordSetup


load_dotenv()

def Runbut ():
    
     # necsessary values from .env
    botKey = getenv('BotTokenTest')
    

    #   Iniztalate classes
    setupbut = DiscordSetup()
    but = DiscordBot()

    setupbut.CommunityModule()
    setupbut.SystemConfigurations()
    setupbut.PostModerationModule()

    but.run(botKey)

if __name__ == '__main__':
    Runbut()
