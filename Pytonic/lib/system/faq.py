
#   Discord Repositories
import discord as d

from discord import Color
from discord.embeds import Embed
from discord.ext.commands import Cog

class FrequentlyAskedQuestions(Cog):

    """
        Discord command menu

        >   Creation Date   : 26.03-23
        >   Last update     : 26.03-23

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        Copyright (C) 2023  Kristoffer Gjøsund
    """

    help = d.SlashCommandGroup(name = 'help', description = 'Frequently asked questions')

    @help.after_invoke
    async def clear_memory(self, ctx: d.ApplicationContext):

        """
            Clearing data chace

            >   Creation Date   : 23.02-23
            >   Last update     :
        """

        self.embed.clear_fields()
        self.embed.remove_image()
        self.embed.remove_author()
        self.embed.remove_footer()
        self.embed.description = ""
        self.embed.remove_thumbnail()
        self.embed.color = d.Colour.dark_purple()

        del ctx #   Clearing some memory
        return

    def __init__(self,bot):

        self.bot = bot
        self.embed = Embed(color=d.Colour.dark_purple())

    @help.command()
    async def frequentlyaskedquestion(self, ctx:d.ApplicationContext, arg = None):

        """
            Available bot commands

            >   Creation Date   : 23.02-23
            >   Last update     : 26.03-23
        """

        arg = str(arg).lower().replace(" ", "")

        arr = [ 
                "gamersmodule", "wordgames", "mathgames", "reactiongames", 
                "moderationmodule", "administrator module",
                
                "communitymodule"]

        if arg not in arr:
            self.embed.title = 'Frequently Asked Questions:question:'
            self.embed.add_field(name=':people_holding_hands: Community Module', value='Ever heard of the guy whom joined a community? \n He were never seen again.', inline=True)
            self.embed.add_field(name=':signal_strength: Gamers Module',value='An Irishman arrived at J.F.K. Airport and wandered around the terminal with tears streaming down his cheeks...', inline=True)

            if ctx.author.guild_permissions.manage_channels: self.embed.add_field(name = "Moderator Module")
            if ctx.author.guild_permissions.administrator: self.embed.add_field(name=':signal_strength: Administrator Module',value='An Irishman arrived at J.F.K. Airport and wandered around the terminal with tears streaming down his cheeks...', inline=True)

        else:

            match arg:
                case "gamersmodule" : self.embed = self.GamersModule()
                case "wordgames" : self.embed = self.GamersModule(arg)
                case "mathgames" : self.embed = self.GamersModule(arg)
                case "reactiongames" : self.embed = self.GamersModule(arg)

                case "communitymodule" : self.embed = self.CommunityModule()

                case "administrator module": embed = self.AdministratorModule(ctx)
                case "moderator module": self.embed = self.ServerMod()

        await ctx.respond(embed= self.embed)

        del arg

        return

    def CommunityModule(self):

        self.embed.title=':people_holding_hands: Community Module'
        self.embed.description = 'Available commands'
        self.embed.add_field(name='/community botinfo \n(optional parameter: log)', value='- how did the bot fail the exam? She was a bit rusty', inline=True)
        self.embed.add_field(name='/community list', value ='list of members', inline=True)
        self.embed.add_field(name='?meme', value='(optional parameter : reddit) - What do you call a gamer whom works at an abortion clinic? :rofl:\n Spawn Camper ', inline=True)

        return self.embed

    def GamersModule(self, arg = None):

        self.embed.title = 'Gamers Module'
        self.embed.description = 'Games created with Python'
        
        if arg == "mathgames":

            self.embed.add_field(name='/math guessthenumber', value=' - Guess the number', inline=True)
            self.embed.add_field(name='/math littleprofessor', value='- Little Proffessor', inline=True)
        
        elif arg == "wordgames":

            self.embed.add_field(name='/word eightball', value='- Ask a Philisopher a question', inline=True)
            self.embed.add_field(name=':question: /word jumble', value=' - unscrabble a jumble', inline=True)
            self.embed.add_field(name=':question: /word scrabble', value=' - unscrabble a jumble', inline=True)

        elif arg == "reactiongames":
            self.embed.add_field(name='/reaction rockscissorpaper', value='- :rock:, :scissors:, :page_facing_up:', inline=True)

        else: 
            self.embed.add_field(name ='Math Games', value =' Such as guess the number, little proffessor')
            self.embed.add_field(name ='Word Games', value =' Such as Eightball, Jumble, Scrabble, Rock, Scissors and paper')
            self.embed.add_field(name ='Reaction Games', value =' Such as Rock, Scissors and paper')

        del arg#    Clear some argument

        return self.embed

    def ServerMod(self, ctx:d.ApplicationContext):#   Server Moderation

        self.embed.title = 'Moderator Module'
        self.embed.color = Color.dark_purple()

        if ctx.author.guild_permissions.kick_members: pass
        elif ctx.author.guild_permissions.manage_roles:pass

        elif ctx.author.guild_permissions.manage_channels:

            self.embed.add_field(name=f'/channel Delete', value='- Deletes a channel from the server ', inline=True)
            self.embed.add_field(name=f'/channel Clear', value= '- Clears the given channel Chat:bangbang:', inline=True)
            self.embed.add_field(name=f'/channel Create', value='- Create a new channel default : hidden ', inline=True)

        elif ctx.author.guild_permissions.moderate_members: pass

        else: self.embed.add_field(name=f'No commands available', value = " ")

        return self.embed

    #   Server Adminsistration
    async def AdministratorModule(self, ctx:d.ApplicationContext): 
        
        self.embed.title=':people_holding_hands: Community Module'
        self.embed.description = 'Available commands'
        self.embed.add_field(name='/ban list', value=' List of banned members', inline=True)
        self.embed.add_field(name='/ban member', value ='ban a member from the server', inline=True)
        self.embed.add_field(name='/ban unban', value='unban a member from the server', inline=True)
        #self.embed.add_field(name='/ban auditlog', value=' view the auditlog', inline=True)

        return self.embed

