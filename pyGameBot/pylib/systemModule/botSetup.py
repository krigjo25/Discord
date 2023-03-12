from discord import Intents#   Discord Repositories

#   System module
from pylib.systemModule.discordBot import DiscordBot                                #   The Client
from pylib.systemModule.commandError import ErrorHandler                            #   Error Handling Module
from pylib.systemModule.frequentlyaskedquestions import FrequentlyAskedQuestions    #   Help module

from pylib.community.community import Community                                     #   Community module

#   miniGames Module
from pylib.minigames.mathgames import MathGames
from pylib.minigames.wordGames import WordGames
from pylib.minigames.wordGames import ReactionGames

class DiscordSetup():

    """
        Copyright (C) 2023  Kristoffer Gjøsund

        The Discord bot setup

        >   Creation Date   : 12.01-23
        >   Last update     : 23.02-23

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
    """
    def __init__(self):

        self.intents = Intents()
        self.bot = DiscordBot(intents=self.SystemConiguration())

        return

    def SystemConiguration(self):

        #   Bot intents
        self.intents.guilds = True                  #   Allows the bot to interect with guilds
        self.intents.emojis = True                  #   emoji, sticker related events
        self.intents.members = True                 #   Allows the bot to interact with members
        self.intents.messages = True                #   Allows the messages Guild & DM
        self.intents.presences = False               #   Allows the bot to track member activty
        self.intents.message_content =True          #   Allows the bot to send embeded message
        self.intents.guild_reactions = True         #   Allows the bot to add reactions with-in the guild  

        return self.intents


    def SystemSetup(self):
        
        self.bot.add_cog(ErrorHandler(self.bot))
        self.bot.add_cog(FrequentlyAskedQuestions(self.bot))

        return

    def CommunityModule(self):

        self.bot.add_cog(Community(self.bot))

        return

    def GamersModule(self):

        self.bot.add_cog(WordGames(self.bot))
        #self.bot.add_cog(ReactionGames(self.bot))
        self.bot.add_cog(MathGames(self.bot))

        return