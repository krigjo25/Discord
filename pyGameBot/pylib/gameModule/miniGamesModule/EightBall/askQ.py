#   Discord library
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command

#   Custom Library
from pylib.dictionaries.gameDictionaries import GameDictionary

class EightBall(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple(), description='')

    @command(name='ask')

    async def EightBall(self, ctx, quiz):
        """     EightBall()

            #   Ask a question with what, how or why
            #   Slice it down so you just get the four first letters
            #   Send a philliosofically answer

        """
        #   Classes
        d = GameDictionary()
        
        # Creating a string of the question which is asked
        #quiz = str(quiz)
        msg = quiz

        # Slicing to get the four first characters
        x = slice(4)

        quiz = quiz[x].lower()

        self.embed.title = ':8ball: ask the Oracle'

        if quiz == 'how':
            answer = d.PhiliosopicAnswer()
            self.embed.description = f' You asked the Oracle\n \"{msg}\"\n the response \n{answer}'
            await ctx.send(embed=self.embed)

        elif quiz == 'what':
            answer = d.PhiliosopicAnswer()
            self.embed.description = f'You asked the Oracle\n\"{msg}\"\n the response \n{answer}'
            await ctx.send(embed=self.embed)

        
        else:
            answer = d.DumbFacts()
            self.embed.description = f'You asked the Oracle\n\"{msg}\"\n the response \n{answer}'
            await ctx.send(embed=self.embed)