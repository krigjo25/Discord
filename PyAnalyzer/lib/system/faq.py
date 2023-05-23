#   Discord Repositories
import discord as d
from discord import Colour
from discord.embeds import Embed
from discord.ext.commands import command, Cog

class FrequentlyAskedQuestions(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Colour.dark_purple())
        self.prefix = "/"

        return

    #   Frequently Asked Question

    help = d.SlashCommandGroup(name= 'help', description='Bot Documentation')

    @help.after_invoke
    async def clear_memory(self, ctx: d.ApplicationContext):

        """
            Clearing data chace

            >   Creation Date   : 26.03-23
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


    @help.command()
    async def faq(self, ctx:d.ApplicationContext, arg = d.Option(str, 'server / members')):

        """

            Bot Documentation

            >   Creation Date   : 26.03-23
            >   Last update     : 21.02-23

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

        arr = ['server', 'channel', 'member']

        if arg in arr:

            match arg:
                case "server": self.embed = self.ServerAnalysis()
                case "channel": self.embed = self.ChannelAnalysis()
                case "member": self.embed = self.MemberAnalysis()
                case 'administrator': self.embed = self.AdministratorAnalysis()
        else:

            self.embed.title = 'Frequently Asked Questions:question:'
            self.embed.add_field(name= 'Server Analysis', value = '/help faq server')
            self.embed.add_field(name= 'Member Analysis', value = '/help faq member')

            if ctx.author.guild_permissions.administrator:
                self.embed.add_field(name = f'Administrator Analysis', value = '/help faq administrator')

        await ctx.respond(embed=self.embed)


        return

    def ServerAnalysis(self): 

        '''
            #   Commands for Server Analysis
        '''
        
        self.embed.title = 'Server Analysis'
        self.embed.add_field(name = f'{self.prefix}analysis server', value = 'Run a server analysis')
        self.embed.add_field(name = f'{self.prefix}analysis role', value = 'Run a role Analysis')
        self.embed.add_field(name = f'{self.prefix}analysis channel', value = 'Run a Channel Analysis')
        self.embed.add_field(name = f'{self.prefix}analysis bot', value = 'Run a Bot Analysis')
        self.embed.add_field(name = f'{self.prefix}analysis auditlog', value = 'Run Audit log Analysis')

        return self.embed

    def ChannelAnalysis(self): 

        '''
        #   Commands for Channel Analysis
        '''
        self.embed.title = 'Frequently Asked Questions:question:'

        self.embed.add_field(name= f'{self.prefix}analysis Post', value = 'Run a Post Analysis')
        #self.embed.add_field(name= f'{self.prefix}analysis emoji', value = 'Run a Emoji Analysis')
        #self.embed.add_field(name= f'{self.prefix}analysis reaction', value = 'Run a Reaction Analysis')
        #self.embed.add_field(name= f'{self.prefix}analysis sticker', value = 'Run a Sticker Analysis')

        return self.embed
    
    def MemberAnalysis(self):

        '''
        #   Commands for Member Analysis
        '''
        self.embed.title = 'Frequently Asked Questions:question:'
        self.embed.add_field(name= f'{self.prefix}analysis member (member name)', value = 'Run aMember Profile Analysis')
        self.embed.add_field(name= f'{self.prefix}analysis top', value = 'Top Members')

        return self.embed

    def AdministratorAnalysis(self):

        self.embed.title = "Administrator module"
        self.embed.add_field(name = f'{self.prefix}analysis auditlog', value = 'Run Audit log Analysis')
        return self.embed