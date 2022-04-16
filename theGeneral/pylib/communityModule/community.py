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
        svr = len(self.bot.guilds)
        botMaster = self.bot.get_user(340540581174575107)
        botName = 'pyButt'
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

            self.embed.title = 'Whats new?'
            self.embed.url=f'https://github.com/krigjo25/Discord/blob/main/{botName}/RSSBot.md'
            changelog = f'*** What is new ***\n{CommunityFunctions.ReadChangelog()}'

            await ctx.send(changelog)
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
    async def YesNoMaybe(self, ctx, arg):

        arg = str(arg)

        if arg == 'yes' or arg == 'No' or arg == 'Maybe':

            #   Creating a list to keep the words in
            dictionary = ['Yes', 'No', 'Maybe']

            #   Randomizing the words
            x = randint(0,2)
            shuffle(dictionary)

            #   Prepare and send the embed
            self.embed.title = f"{dictionary[x]}"
            await ctx.send(embed=self.embed)

            return 

#   Going busy
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
        db = MariaDB
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
        db = MariaDB
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

class CommunityFunctions(Cog):

    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    def ReadChangelog(self):

        with open('Pybut/changelog.md', 'r') as f:

            changelog = f.read()

            #   Closing the document
            f.close()

        return changelog