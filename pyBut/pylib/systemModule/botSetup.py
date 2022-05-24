
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

class DiscordSetup():

    def __init__(self):

        #self.appinfo = AppInfo()
        self.intents = Intents()
        self.bot = DiscordBot(intents=self.SystemConiguration())

        return

    def SystemConiguration(self):

        #   Bot intents
        self.intents.bans = True                    #   Allows the bot to ban / unban members
        self.intents.guilds = True                  #   Allows the bot to interect with guilds
        self.intents.emojis = True                  #   emoji, sticker related events
        self.intents.members = True                 #   Allows the bot to interact with members
        self.intents.messages = True                #   Allows thmessages Guild & DM
        self.intents.presences = True               #   Allows the bot to track member activty
        self.intents.message_content =True          #   Allows the bot to send embeded message
        self.intents.guild_reactions = True         #   Allows the bot to add reactions with-in the guild  

        return self.intents

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

    def MiscModuleSetup(self):

        #   Community module
        self.bot.add_cog(CommunityModule(self.bot))

        return
