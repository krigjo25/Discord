#   Discord Repositories
from discord import Intents

#   library Repositories - System module
from pylib.systemModule.discordBot import DiscordBot                                         #   The Bot Client
from pylib.systemModule.commandError import ErrorHandler                                     #   Error Handling Module
from pylib.systemModule.faq import FrequentlyAskedQuestions                                  #   Help module

#   Moderation Utility
from pylib.moderation.post_moderation import Administrator, ChannelModeration, RoleModeration, MiscModeration, MemberModeration

class DiscordSetup():

    """
        #   Discord bot configuration
        #   Cogs for the bot
    """

    def __init__(self):

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
        #self.intents.auto_moderation_configuration = True #
        #self.intents.auto_moderation_execution = True
        #self.intents.integrations = True
        #self.intents.webhooks = True
        #self.intents.invites = True
        #self.intents.voice_states = True
        #self.intents.guild_typing = True
        #self.intents.dm_typing = True
        #self.intents.dm_reactions = True
        #self.intents.message_content = True
        #self.intents.scheduled_events = True
        return self.intents

    def SystemSetup(self):

        #   Add Cogs
        self.bot.add_cog(ErrorHandler(self.bot))
        self.bot.add_cog(FrequentlyAskedQuestions(self.bot))

        return

    def ModerationSetup(self):

        self.bot.add_cog(Administrator(self.bot))
        self.bot.add_cog(MiscModeration(self.bot))
        self.bot.add_cog(MemberModeration(self.bot))
        self.bot.add_cog(ChannelModeration(self.bot))
        


        return
