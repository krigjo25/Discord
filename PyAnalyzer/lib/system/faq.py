
#   Discord Repositories
from discord.embeds import Embed
from discord import Color
from discord.ext.commands import command, Cog

class FrequentlyAskedQuestions(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple())

#   Frequently Asked Question

    @command(name='faq', pass_context=True)
    async def FrequentlyAskedQuestions(self,ctx, args=None):

        self.embed.title = 'Frequently Asked Questions:question:'
        self.embed.description = ' Usage ** ?help (Category)** for more details\n\n'
        
        await ctx.send(embed=self.embed)
        self.embed.clear_fields()

        return