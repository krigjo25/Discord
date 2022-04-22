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
            #   Slice it down so you just get the four first letters
            #   Send a philliosofically answer

        """

        #   Initializing classes
        d = PhiliosopicAnswer()

        quiz = await self.bot.wait_for('message', timeout=100)

        # Creating a string of the question which is asked
        quiz = str(quiz.content).lower().replace(" ", "")
        msg = str(quiz.content)
        
        #   Prepare & send the embed
        self.embed.title = ':8ball: Ask the Philiospher a question'
        self.embed.description = f' Please write to me what you have in mind.'
        await ctx.send(embed=self.embed)

        if quiz[0:3] == 'how':answer = d.PhiliosopicAnswer()
        elif quiz[0:4] == 'what':answer = d.PhiliosopicAnswer()
        else:answer = d.DumbFacts()

        #   Prepare and send the embed
        self.embed.title = ':8ball: ask the Oracle'
        self.embed.description = f' You asked the Oracle\n \"***{msg}***\"\n the response \n{answer}'
        await ctx.send(embed=self.embed)