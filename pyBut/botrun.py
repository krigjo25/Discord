
from os import getenv
from dotenv import load_dotenv

from pylib.systemModule.pyRess import PyRess
from pylib.systemModule.pyGame import PyGame
from pylib.systemModule.pyMod import PyMod
from pylib.systemModule.botSetup import DiscordSetup


load_dotenv()
def RunBot ():
        
        #   Initializing classes
        rss = PyRess()
        pygame = PyGame()
        pymod = PyMod()
        disc = DiscordSetup()
        botKey = getenv('PyMod')

        rss.InternationalNewsSetup()
        rss.NationalNewsSetup()

        pymod.PyMod()

        pygame.PyGame()        
        disc.SystemSetup()
        disc.MiscModuleSetup()
        disc.bot.run(botKey)


if __name__ == '__main__':
    RunBot()