#   Discord library
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command

#   Custom Library
from lib.dictionaries.systemmessages import Dictionaries

class EightBall(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple(), description='')

    @command(name='ask')
    #   Ask a question with what, how or why
    #   Slice it down so you just get the four first letters
    #   Send a philliosofically answer
    async def AskQuestion(self, ctx, quiz):
        
        # Creating a string of the question which is asked
        quiz = str(quiz)
        msg = quiz
        # Slicing to get the four first characters
        x = slice(4)

        quiz = quiz[x].lower()

        self.embed.title = ':8ball: ask the Oracle'
        
        if quiz == 'how':
            answer = Dictionaries.PhiliosopicAnswer()
            self.embed.description = f' You asked the Oracle\n {msg}\n the response \n{answer}'
            await ctx.send(embed=self.embed)

        elif quiz == 'what':
            answer = Dictionaries.PhiliosopicAnswer()
            self.embed.description = f'You asked the Oracle\n {msg}\n the response \n{answer}'
            await ctx.send(embed=self.embed)

        
        else:
            answer = Dictionaries.DumbFacts()
            self.embed.description = f'You asked the Oracle\n {msg}\n the response \n{answer}'
            await ctx.send(embed=self.embed)