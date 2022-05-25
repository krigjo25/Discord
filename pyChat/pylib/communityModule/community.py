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

        #   Initializing variables
        svr = len(self.bot.guilds)
        botMaster = self.bot.get_user(340540581174575107)
        botName = 'PyChat'

        if args == None:

            self.embed.title = f':notebook: About {botName}'
            self.embed.url=f'https://github.com/krigjo25/Discord/blob/main/{botName}/read-me.md'
            self.embed.description = ''
            self.embed.add_field(name = ':rotating_light: Released', value=getenv('BotCreated'), inline=True)
            self.embed.add_field(name = ' :new: Updated', value=getenv('BotUpdated'), inline=True)
            self.embed.add_field(name = ':person_with_probing_cane: Current Version', value= getenv('BotVersion'), inline=True)
            self.embed.add_field(name = ':toolbox: Responsory', value=getenv('Responsory'), inline=True)
            self.embed.add_field(name = ':cloud: Hosted', value=getenv('HOSTED'), inline=True)
            self.embed.add_field(name = ':man: Master', value=f' {botMaster} :flag_no:', inline=True)
            self.embed.add_field(name = ':arrows_counterclockwise: Server Counting', value=f'Watching {svr} \nDiscord Servers', inline=True)
            await ctx.send(embed = self.embed)
            self.embed.clear_fields()

        if args == 'log':

            self.embed.title = 'Whats new?'
            self.embed.url=f'https://github.com/krigjo25/Discord/blob/main/{botName}/RSSBot.md'
            changelog = f'*** What is new ***\n{CommunityFunctions.ReadChangelog()}'

            await ctx.send(changelog)
            self.embed.clear_fields()

        return

class CommunityFunctions(Cog):

    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    def ReadChangelog(self):

        with open('Pybut/changelog.md', 'r') as f:

            changelog = f.read(415)

            #   Closing the document
            f.close()

        return changelog