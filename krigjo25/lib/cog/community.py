import discord
import aiohttp

from os import getenv
from random import randint, randrange
from dotenv import load_dotenv

from discord.member import Member
from discord.client import Client
from discord.utils import get
from discord.colour import Color
from discord.embeds import Embed
from discord import Status
from discord.ext.commands import Cog, command

load_dotenv()

class Community(Cog, name='Community Module'):
    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())


#   Bot Info
    @command(name="krigjo25")
    async def BotInfo(self, ctx, args=None):
        svr = len(self.bot.guilds)
        owner = self.bot.get_user(340540581174575107)
        if args == None:

            self.embed.title = f':notebook: About {self.bot.user}'
            self.embed.url='https://github.com/krigjo25/Discord/blob/main/krigjo25/read-me.md'
            self.embed.description = ''
            self.embed.add_field(name = ':rotating_light: Released', value=getenv('BotCreated'), inline=True)
            self.embed.add_field(name = ' :new: Updated', value=getenv('BotUpdated'), inline=True)
            self.embed.add_field(name = ':person_with_probing_cane: Current Version', value= getenv('BotVersion'), inline=True)
            self.embed.add_field(name = ':toolbox: Responsory', value=getenv('Responsory'), inline=True)
            self.embed.add_field(name = ':cloud: Hosted', value=getenv('HOSTED'), inline=True)
            self.embed.add_field(name = ':man: Master', value=f'My master goes by the name, {owner} :flag_no:', inline=True)
            self.embed.add_field(name = ':arrows_counterclockwise: Server Counting', value=f'Watching {svr} \nDiscord Servers', inline=True)
            self.embed.add_field(name = ':thought_balloon: To do list', value = '[Future projects](https://github.com/krigjo25/Discord/projects/1)', inline=True)
            await ctx.send(embed = self.embed)
            self.embed.clear_fields()

        if args == 'log':


            changelog = f'''
            Changelog for current version {getenv('BotVersion')}

            :new: Whats new:
                
                *  
                * 
                *  

            :tools: Fixes / changes made
                
                *
                *
                *

            
            Hope you will have fun with the new updates.

            sincerely,
                {owner} :flag_no:
            '''
            self.embed.title = 'Whats new?'
            self.embed.url='https://github.com/krigjo25/krigjo25Bot/blob/main/read%20me.md'
            self.embed.description = f'{changelog}'
            await ctx.send(embed = self.embed)
            self.embed.clear_fields()

        return
#   Online members
    @command(name='memberlist', pass_context=True)
    async def MembersList(self, ctx):


        #   Retriving the server
        svr = ctx.guild

        self.embed.title = 'Server Members'
        
        #   Fetching members
        for member in svr.members:
            
            #   Declare variables
            status = str(member.status)
            nick = str(member.nick)
            user = self.bot.user

            #   Add emoji to status
            if status == 'online':
                status = ':heart_on_fire:'

            elif status == 'idle':
                status = ':dash:'
            
            elif status == 'dnd':
                status = ':technologist:'

            elif status == 'offline':
                status = ':sleeping:'
            
            #   Fetch user nick
            if nick == 'None':
                nick = ' '
            else:
                nick = f'Nick : {member.nick}\n'
            if member != user:
                self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'{nick} Status : {status} ', inline=False)
        await ctx.send(embed = self.embed)
        self.embed.clear_fields()

#   Random Meme
    @command(name='meme', pass_context= True)
    async def GetMeme(self, ctx):

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                post = res['data']['children'] [randrange(0, 24)]
                self.embed.title = post["data"]["title"]
                self.embed.url = 'https://www.urbandictionary.com/define.php?term=Reddit'
                self.embed.set_image(url=post['data']['url'])
                self.embed.description = f'Hot meme porn from  {ctx.author.name}'

                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
                self.embed.set_image(url= '')
        return

#   Random integer
    @command (name='randint')
    async def randomInt(self, ctx, arg, argTwo):

        arg = int(arg)
        arg2 = int(argTwo)
        x = randint(arg, arg2)

        await ctx.send(x)
        