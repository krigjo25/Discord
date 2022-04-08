#   Python Resposories
from os import getenv
from random import randint, randrange
from dotenv import load_dotenv

#   Discord Resposories
import aiohttp
from discord.utils import get
from discord.colour import Color
from discord.embeds import Embed
from discord.ext.commands import Cog, command
from discord.permissions import PermissionOverwrite

#  Local resposories

from pylib.systemModule.databasePython import mariaDB

load_dotenv()

class Community(Cog, name='Community Module'):
    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())


#   Bot Info
    @command(name="botinfo")
    async def BotInfo(self, ctx, args=None):
        svr = len(self.bot.guilds)
        botMaster = self.bot.get_user(340540581174575107)
        botName = 'pyStream'
        if args == None:

            self.embed.title = f':notebook: About {botName}'
            self.embed.url=f'https://github.com/krigjo25/Discord/blob/main/{botName}/read-me.md'
            self.embed.description = ''
            self.embed.add_field(name = ':rotating_light: Released', value=getenv('BotCreated'), inline=True)
            self.embed.add_field(name = ' :new: Updated', value=getenv('BotUpdated'), inline=True)
            self.embed.add_field(name = ':person_with_probing_cane: Current Version', value= getenv('BotVersion'), inline=True)
            self.embed.add_field(name = ':toolbox: Responsory', value=getenv('Responsory'), inline=True)
            self.embed.add_field(name = ':cloud: Hosted', value=getenv('HOSTED'), inline=True)
            self.embed.add_field(name = ':man: Master', value=f'My master goes by the name, {botMaster} :flag_no:', inline=True)
            self.embed.add_field(name = ':arrows_counterclockwise: Server Counting', value=f'Watching {svr} \nDiscord Servers', inline=True)
            self.embed.add_field(name = ':thought_balloon: To do list', value = '[Future projects](https://github.com/krigjo25/Discord/projects/1)', inline=True)
            await ctx.send(embed = self.embed)
            self.embed.clear_fields()

        if args == 'log':


            changelog = f'''
            Changelog for current version {getenv('BotVersion')}

            :new: Whats new:

                *   |   
                *   |
                *   | 

            :tools: Fixes / changes made
                
                *   |
                *   |
                *   |

            
            Hope you will have fun with the new updates.

            sincerely,
                {botMaster} :flag_no:
            '''
            self.embed.title = 'Whats new?'
            self.embed.url=f'https://github.com/krigjo25/{botName}/blob/main/read%20me.md'
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
            botUser = self.bot.user

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
            if member != botUser:
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

    @command (name='dnd')
    async def AwayFromKeyBoard(self, ctx, *, reason):

        """                     AwayFromKeyBoard
            This function creates a status update for a given member of the server
            The player should not be able to retrieve notifications from the server,
            Not get mentions.
            The mentioner, should retrieve a message, from the bot 
            "I regret to inform you the member you asking for is busy at the moment. due to (reason)"
        """
        #   initializing classes
        db = mariaDB
        database = getenv('database')

        # Declearing the user & reason arguments
        argTwo = str(reason)
        argOne = str(ctx.author)

        #   Inserting a new record into the database
        db.newRecord(database, argOne, argTwo)

        #   Closing the connection
        db.closeConnection()

        #   retrieve the channel if it exists
        svr = ctx.guild
        ch = get(svr.channels, name ='afk-channel')

        #   Overwriting the permission for the channel
        permission =  {
            svr.default_role:PermissionOverwrite(   send_messages=False, 
                                                    add_reactions=True,
                                                    read_messages=True)
        }
        if not ch:
            await svr.create_text_channel(f'afk-channel', overwrites=permission)

        #   Send a message to the channel
        await ch.send(f'{argOne} has just gone in Do not disturb mode. Due to {argTwo}')


    @command (name='back')
    async def BackToKeyBoard(self, ctx):

        """         BackToKeyBoard

            The user will be removed from the database,
            the user can be mentioned again.

        """

        #   initializing classes
        db = mariaDB
        database = getenv('database1')

        # Declearing the user argument
        user = str(ctx.author.name)

        db.DelRecord(database, user)

        #   Closing the connection
        db.closeConnection()

        #   retrieve the channel if it exists
        svr = ctx.guild
        ch = get(svr.channels, name ='afk-channel')

        #   Send a message to the channel
        await ch.send(f'{user} just came back from dnd mode')

        return