#   Discord library
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command

#   Custom Library
from pylib.dictionaries.gameDictionaries import PhiliosopicAnswer

class EightBall(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple(), description='')

    @command(name='ask')
    async def EightBall(self, ctx):

        """     EightBall()

            #   Ask a question with what, how or why
            #   Combine the answers
            #   Send a philliosofically answer

        """

        #   Initializing classes
        d = PhiliosopicAnswer()
        
        #   Prepare & send the embed
        self.embed.title = ':8ball: Ask the Philiospher a question'
        self.embed.description = f' Please write to me what you have in mind.'
        await ctx.send(embed=self.embed)

        #   Wait for an answer and handling the string
        quiz = await self.bot.wait_for('message', timeout=60)
        quiz = str(quiz.content).lower()

        #   Combining the answers 
        if 'how' in quiz or 'what' in quiz : answer = d.PhiliosopicAnswer()
        else: answer = d.DumbFacts()

        #   Prepare and send the embed
        self.embed.title = ':8ball: ask the Oracle'
        self.embed.description = f' You asked the Oracle\n \"***{quiz}***\"\n the response \n{answer}'
        await ctx.send(embed=self.embed)