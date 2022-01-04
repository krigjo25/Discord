

# Discord library
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command

# Python library
from random import shuffle,randrange, randint

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

        # Slicing to get the four first characters
        x = slice(4)

        # Dictonary for "8ball"
        philiosopicAnswer = {  
                                0:'What do you sense about it?',
                                1:'What would you do about it?',
                                2:'What are you really, deep down?',
                                3:'Just let it go, its not your issue.',
                                4:'Just let your self, experience the question',
                                5:'Visualize the question, and the answer will arrive.',
                                6:'If an human is a genious, then The best answers always comes from with-in, just believe in your self enough',
                                7:'As Socrets once said, you already know the answer of the question, since you had an idea of asking the question',
                                8:'Would you be able to let it go?',

                            }
       


        fact = {
                    0:'The earth is oval',
                    1:'You\'re a discord user',
                    2:'life is why',
                    3:'it just is',
                    4:'a',
                    5:'b',
                    6:'v',
                    7:'f',
                }

        #   Randomize the answer
        shuffle(fact)
        i = randrange(0,7)

        shuffle(philiosopicAnswer)

        #   Retrieve the key
        fact = fact.get(i)
        quiz = quiz[x].lower()
        answer = philiosopicAnswer.get(i)
        print(quiz)
        # creating an embeded message
        self.embed.title = ':8ball: ask the Oracle'
        
        if quiz == 'how':
            self.embed.description = f'{answer}'
            await ctx.send(embed=self.embed)

        elif quiz == 'why':
            self.embed.description = f'{fact}'
            await ctx.send(embed=self.embed)

        elif quiz == 'what':
            self.embed.description = f'{answer}'
            await ctx.send(embed=self.embed)

        
        else:
            await ctx.send(f' I suggest you learn english first.')