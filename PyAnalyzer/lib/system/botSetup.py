#   Discord Repositories
from discord import Intents

#   Library Repositories

#   System module
from lib.system.discordBot import DiscordBot                        #   The Client
from lib.system.commandError import ErrorHandler                    #   Error Handling Module
from lib.system.faq import FrequentlyAskedQuestions                 #   Help module

#   Analysis modules
from lib.pyAnalyzer.channels import ChannelAnalysis
from lib.pyAnalyzer.members import MemberAnalysis
from lib.pyAnalyzer.analysis import ServerAnalysis


class DiscordSetup():

    def __init__(self):

        self.intents = Intents()
        self.bot = DiscordBot(intents=self.SystemConiguration())

        return

    def SystemConiguration(self):

        #   Bot intents
        self.intents.bans = False                   #   Disalow the bot to ban / unban members
        self.intents.guilds = True                  #   Allows the bot to interect with guilds
        self.intents.emojis = True                  #   emoji, sticker related events
        self.intents.members = True                 #   Allows the bot to interact with members
        self.intents.messages = True                #   Allows the messages Guild & DM
        self.intents.presences = True               #   Allows the bot to track member activty
        self.intents.message_content =True          #   Allows the bot to send embeded message
        self.intents.guild_reactions = True         #   Allows the bot to add reactions with-in the guild  

        return self.intents

    def SystemSetup(self):

        self.bot.add_cog(FrequentlyAskedQuestions(self.bot))
        self.bot.add_cog(ErrorHandler(self.bot))

        return

    def Analyzer(self):

        self.bot.add_cog(ServerAnalysis(self.bot))
        self.bot.add_cog(MemberAnalysis(self.bot))
        self.bot.add_cog(ChannelAnalysis(self.bot))

        return