
#   Python Repositories
from os import getenv

#   Dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord import Intents

# library Repositories

#   System module
from pylib.systemModule.welcomeModule import Welcome                              #   Welcome Module 
from pylib.systemModule.faq import FrequentlyAskedQuestions                              #   Help module
from pylib.systemModule.discordBot import DiscordBot                        #   The Client
from pylib.systemModule.commandError import ErrorHandler                    #   Error Handling Module

#   Community Module
from pylib.communityModule.community import CommunityModule                       #   Community module

#   miniGames Module
from pylib.gameModule.miniGamesModule.EightBall.askQ import EightBall                             #   EightBall
from pylib.gameModule.miniGamesModule.jumbleGame.jumble import JumbleGame                         #   Jumble Game
from pylib.gameModule.miniGamesModule.integerGame.guessTheNumber import GuessTheNumber            #   Guess the number
from pylib.gameModule.miniGamesModule.reactionsGames.rockPaperScissors import ReactionGame    #   Rock, Scissors & Paper

#   RSSBot
from pylib.rssNews.RSSBot import RSSBot
# Bot Utility

    # Moderation Utility
from pylib.postModerationModule.moderatorModule.moderator import Moderator                  #   Moderator Module
from pylib.postModerationModule.administratorModule.administrator import Administrator          #   Administrator module

# Importing .evn file
load_dotenv()

class DiscordSetup():

    def __init__(self):

        self.intents= Intents().all()               #  Only allows Default intents
        self.bot = DiscordBot(intents=self.intents)

        return

    def SystemSetup(self):

        #   System Configuration
        #self.intents.members = True             #  Allows the bot to track member updates, fetch members
        #self.intents.messages = True            #  Allows the bot to send messages
        #self.intents.presences = True           #  Allows the bot to track member activty
        #self.intents.reactions = True           #  Allows the bot to react to a message

        self.bot.add_cog(Welcome(self.bot))
        self.bot.add_cog(FrequentlyAskedQuestions(self.bot))
        self.bot.add_cog(ErrorHandler(self.bot))

        return

    def AdministrationSetup(self):

    #   Moderation - Module
        self.bot.add_cog(Moderator(self.bot))
        self.bot.add_cog(Administrator(self.bot))

        return

    def miniGamesSetup(self):

        #   Game-Module
            #   miniGames
        self.bot.add_cog(EightBall(self.bot))
        self.bot.add_cog(JumbleGame(self.bot))
        self.bot.add_cog(GuessTheNumber(self.bot))
        #self.bot.add_cog(ReactionGame(self.bot))

        return

    def MiscModuleSetup(self):

        #   Community module
        self.bot.add_cog(CommunityModule(self.bot))

        return

def BotConfiguration ():

        #   Initializing classes

        rss = RSSBot()
        disc = DiscordSetup()
        botKey = getenv('PyMod')

        rss.InternationalNewsSetup()
        rss.NationalNewsSetup()


        disc.SystemSetup()
        disc.miniGamesSetup()
        disc.MiscModuleSetup()
        disc.AdministrationSetup()

        disc.bot.run(botKey)

if __name__ == '__main__':
    BotConfiguration()