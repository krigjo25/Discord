
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
    async def BotInfo(self, ctx, arg=None):
        
        svr = len(self.bot.guilds)
        Master = self.bot.get_user(340540581174575107)

        if arg == None:

            self.embed.title = ':notebook: About PyGame'
            self.embed.url = 'https://github.com/krigjo25/Discord/blob/main/pyGame/readme.md'
            self.embed.description = 'About The bot'
            self.embed.add_field(name = ':rotating_light: Released', value=getenv('BotCreated'), inline=True)
            self.embed.add_field(name = ' :new: Updated', value=getenv('BotUpdated'), inline=True)
            self.embed.add_field(name = ':person_with_probing_cane: Current Version', value= getenv('BotVersion'), inline=True)
            self.embed.add_field(name = ':toolbox: Responsory', value='https://github.com/krigjo25/Discord/blob/main/RSSBot/.md#Responsories', inline=True)
            self.embed.add_field(name = ':cloud: Hosted', value=getenv('HOSTED'), inline=True)
            self.embed.add_field(name = ':man: Master', value=f'{Master} :flag_no:', inline=True)
            self.embed.add_field(name = ':arrows_counterclockwise: Server Counting', value=f'Watching {svr} \nDiscord Servers', inline=True)

        elif arg == 'log':


            self.embed.title = "What is new?"
            self.embed.url = "https://github.com/krigjo25/Discord/blob/main/pyGameBot/changelog.md"
            self.embed.description = f"{self.ReadChangelog()}"

        await ctx.send(embed = self.embed)

        #   Clear space and fields
        del arg

        self.embed.clear_fields()

        return

    @command(name='meme', pass_context= True)
    async def GetRedditMeme(self, ctx):

        """
            #   Author : Krigjo25
            #   Date : 01.23-23

            #   Generates a random Meme from reddit

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

            #   Clearing some space
            del res
            del post

            self.embed.clear_fields()
            self.embed.remove_image()

        return

    @command (name='randint')
    async def randomInt(self, ctx, arg, argTwo):

        """
            #   Author : Krigjo25
            #   Date : 01.23-23

            #   Generates a random integer between given arguments
            #   Gamers Module,
            #   Community module
        """

        try : 
            arg = int(arg)
            arg2 = int(argTwo)
            
        except Exception as e: print(e)

        else: x = randint(arg, arg2)

        await ctx.send(x)

        return

    def ReadChangelog(self):

        # Updating read max 32 lines

        with open('pyGameBot/changelog.md', 'r') as f:

            changelog = f.read()

            f.close()

        return changelog
