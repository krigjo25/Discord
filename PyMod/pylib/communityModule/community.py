#   Python Repositories
from os import getenv
from random import randint, randrange, shuffle
from dotenv import load_dotenv

#   Discord Repositories
import aiohttp
from discord.utils import get
from discord.colour import Color
from discord.embeds import Embed
from discord.ext.commands import Cog, command
from discord.permissions import PermissionOverwrite

#  pyLib Repositories

from pylib.systemModule.databasePython import MariaDB

load_dotenv()

class CommunityModule(Cog, name='Community Module'):
    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())


#   Bot Info
    @command(name="botinfo")
    async def BotInfo(self, ctx, args=None):

        '''
            Retrive infomation about the bot
        '''

        botName = 'PyMod'
        svr = len(self.bot.guilds)
        botMaster = self.bot.get_user(340540581174575107)

        if args == None:

            self.embed.title = f':notebook: About {botName}'
            self.embed.url=f'https://github.com/krigjo25/Discord/blob/main/{botName}/readme.md'
            self.embed.description = ''
            self.embed.add_field(name = ':rotating_light: Released', value=getenv('BotCreated'), inline=True)
            self.embed.add_field(name = ':new: Updated', value=getenv('PyModUpdated'), inline=True)
            self.embed.add_field(name = ':person_with_probing_cane: Current Version', value= getenv('PyModV'), inline=True)
            self.embed.add_field(name = ':toolbox: Responsory', value=getenv('Responsory'), inline=True)
            self.embed.add_field(name = ':cloud: Hosted', value=getenv('Hosted'), inline=True)
            self.embed.add_field(name = ':man: Master', value=f'My master goes by the name, {botMaster} :flag_no:', inline=True)
            self.embed.add_field(name = ':arrows_counterclockwise: Server Counting', value=f'Watching {svr} \nDiscord Servers', inline=True)
            self.embed.add_field(name = ':thought_balloon: To do list', value = '[Future projects](https://github.com/krigjo25/Discord/projects/1)', inline=True)
            #self.embed.add_field(name = 'Bot latency', values = f'**{round(self.bot.latency * 10000)}** MS!', inline=True)
            await ctx.send(embed = self.embed)

            self.embed.clear_fields()
            self.embed.url= ''

        if args == 'log':

            self.embed.title = 'Change log'
            self.embed.url=f'https://github.com/krigjo25/Discord/blob/main/{botName}/changelog.md'
            self.embed.description = f'*** What is new ***\n{CommunityFunctions.ReadChangelog()}'
            

            await ctx.send(embed= self.embed)

            self.embed.clear_fields()
            self.embed.url= ''


        return

#   Online members
    @command(name='memberlist', pass_context=True)
    async def MembersList(self, ctx):

        '''
            Retrive List of server members
        '''

        #   Initialize variables
        svr = ctx.guild

        self.embed.title = 'Server Members'
        
        #   Fetching members
        for member in svr.members:
            
            #   Intializing variables
            nick = str(member.nick)
            status = str(member.status)

            #   Add emoji to status
            if status == 'online':status = ':heart_on_fire:'
            elif status == 'idle':status = ':dash:' 
            elif status == 'dnd':status = ':technologist:'
            elif status == 'offline':status = ':sleeping:'

            #   Fetch user nick
            if nick == 'None':nick = ' '
            else:nick = f'Nick : {member.nick}\n'

            if member.bot == False:
                self.embed.add_field(name=f'{member.name}#{member.discriminator}',value=f'{nick} Status : {status} ', inline=False)

        await ctx.send(embed = self.embed)
        self.embed.clear_fields()

#   Random Meme
    @command(name='meme', pass_context= True)
    async def GetRedditMeme(self, ctx):

        """" GetRedditMeme
                Generates a random meme from reddit
        """

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

#   Random Number
    @command (name='randint')
    async def randomInt(self, ctx, arg, argTwo):

        """
            randomInt

            Generates a random integer 
            between arg and argTwo

        """

        arg = int(arg)
        arg2 = int(argTwo)
        x = randint(arg, arg2)

        await ctx.send(x)

        return

#   Random Yes / No / Maybe

    @command (name='yesnomaybe')
    async def YesNoMaybe(self, ctx):

        '''
            Randomly choosing between yes, no maybe
        '''

        #   Creating a list to keep the words in
        dictionary = ['Yes', 'No']

        #   Randomizing the words
        x = randint(0,1)
        shuffle(dictionary)

        #   Prepare and send the embed
        self.embed.title = f"{dictionary[x]}"
        await ctx.send(embed=self.embed)

        return 

    @command(name='ping')
    async def PingBot(self, ctx):

                    #   Prepare & Send embeded message
        self.embed.title = f'Bot Latency : **{round(self.bot.latency * 1000)}** MS!'
        self.embed.description = ''
        await ctx.send(embed=self.embed)

    #   List Roles
    @command(name='liro')
    async def ListRoles(self, ctx):

        '''
            1   Retrieve roles from roles list
            2 :x:   Check if its a member or bot role (only member roles)
            3 :x:  Mentioned
            4   send embed into the channel
        '''

        #   Initializing variables
        svr = ctx.guild
        roles = svr.roles
        i = []
        x = 0
        

        for role in roles:

            x += 1
            self.embed.add_field(name = f'Role No {x}', value=f'{role.mention}')

        #   Prepare, send & Clean up embed
        self.embed.title = 'Server roles'
        await ctx.send(embed=self.embed)

        self.embed.clear_fields()

        return

class CommunityFunctions():


    def ReadChangelog():

        #   Opens the changelog
        with open('PyMod/changelog.md', 'r') as f:

            #   Read x bytes
            changelog = f.read(415)

        #   Closing the document
            f.close()

        return changelog