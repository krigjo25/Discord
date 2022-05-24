
#   Python Repositories
from os import getenv
from random import randint, randrange
from dotenv import load_dotenv

#   Discord Repositories
import aiohttp
from discord.colour import Color
from discord.embeds import Embed
from discord.ext.commands import Cog, command

load_dotenv()


class CommunityModule(Cog, name='Community Module'):


    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())


#   Bot Info
    @command(name="botinfo")
    async def BotInfo(self, ctx, *, args=None):

        svr = len(self.bot.guilds)
        Master = self.bot.get_user(340540581174575107)
        botName = 'pyRess'

        if args == None:

            self.embed.title = f':notebook: About {botName}'
            self.embed.url=f'https://github.com/krigjo25/Discord/blob/main/{botName}/readme.md'
            self.embed.description = ''
            self.embed.add_field(name = ':rotating_light: Released', value=getenv('BotCreated'), inline=True)
            self.embed.add_field(name = ' :new: Updated', value=getenv('BotUpdated'), inline=True)
            self.embed.add_field(name = ':person_with_probing_cane: Current Version', value= '0.1.0rb', inline=True)
            self.embed.add_field(name = ':toolbox: Responsory', value='https://github.com/krigjo25/Discord/blob/main/RSSBot/RSSBot.md#Responsories', inline=True)
            self.embed.add_field(name = ':cloud: Hosted', value=getenv('HOSTED'), inline=True)
            self.embed.add_field(name = ':man: Master', value=f'{Master} :flag_no:', inline=True)
            self.embed.add_field(name = ':arrows_counterclockwise: Server Counting', value=f'Watching {svr} \nDiscord Servers', inline=True)

        if args == 'log':


            self.embed.title = 'Change log'
            self.embed.url=f'https://github.com/krigjo25/Discord/blob/main/changelog.md'
            self.embed.description = f'*** What is new ***\n{CommunityFunctions.ReadChangelog()}'
            

        await ctx.send(embed= self.embed)
        self.embed.clear_fields()

        return

#   Online members

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


class CommunityFunctions():

    def ReadChangelog(self):

        with open('changelog.md', 'r') as f:

<<<<<<< Updated upstream
        #   Opens the changelog
        with open('pyRess/changelog.md', 'r') as f:

            changelog = f.read(293)
=======
            changelog = f.read(415)
>>>>>>> Stashed changes

            #   Closing the document
            f.close()

        return changelog