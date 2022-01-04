from os import name
import discord

from discord.embeds import Embed
from discord.utils import get
from discord.ext.commands import Cog
from discord.reaction import Reaction
from discord.permissions import PermissionOverwrite
from discord.ext.commands import command

class Support(Cog, name='Support module'):
    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed()

    @command(name='issue')

    async def ReportIssue(self, ctx, issue):
        pass

    @command(name='*tickets')

    async def CreateTickets(self, ctx):
        pass

    @command(name='report')

    async def ReportSituation(self, ctx):
        self.CreateTickets()