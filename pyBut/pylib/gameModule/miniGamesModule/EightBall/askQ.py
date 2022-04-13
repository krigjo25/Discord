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
        #   Prepare and send the embed
        self.embed.title = ':8ball: ask the Oracle'
        self.embed.description = f' Type in your question for the oracle'
        await ctx.send(embed=self.embed)

        quiz = await self.bot.wait_for('message')
        #   Classes
        d = PhiliosopicAnswer()
        
        # Creating a string of the question which is asked
        quiz = str(quiz.content).capitalize()
        msg = quiz
        print(msg, quiz)

        # Slicing to get the four first characters
        x = slice(4)
  
        if quiz[x] == 'How' or quiz[x] == 'What':
            answer = d.PhiliosopicAnswer()

        else:
            answer = d.DumbFacts()

        #   Prepare and send the embed
        self.embed.title = ':8ball: ask the Oracle'
        self.embed.description = f' You asked the Oracle\n ***\"***{msg}***\"***\n the response \n{answer}'
        await ctx.send(embed=self.embed)