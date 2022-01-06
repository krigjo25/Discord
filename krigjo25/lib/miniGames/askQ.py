

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
        msg = quiz
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
       


        facts = {
                    0:'The earth is oval',
                    1:f'{ctx.author} is your username',
                    2:'life is why',
                    3:'it just is',
                    4:'The opposite sides of a die will always add up to seven.',
                    5:'The King of Hearts is the only king in a deck of cards without a mustache.',
                    6:'There exist no answers for your questions, if you look with-in you know its true',
                    7:'Alaska is the only state whose name is on one row on a keyboard.',
                    8:'A "jiffy" is about one trillionth of a second.',
                    9:'The ocean is blue',
                    10:'Mulan has the highest kill-count of any Disney character.',
                    11:'The infinity sign is called a lemniscate.'
                }

        #   Randomize the answer
        shuffle(facts)
        i = randrange(0,7)
        j = randrange(0,10)

        shuffle(philiosopicAnswer)

        #   Retrieve the key
        fact = facts.get(x)
        quiz = quiz[x].lower()

        answer = philiosopicAnswer.get(i)
        # creating an embeded message
        self.embed.title = ':8ball: ask the Oracle'
        
        if quiz == 'how':
            self.embed.description = f' You asked the Oracle\n {msg}\n the response from the 8ball \n{answer}'
            await ctx.send(embed=self.embed)

        elif quiz == 'what':
            self.embed.description = f'{answer}'
            await ctx.send(embed=self.embed)

        
        else:
            await ctx.send(f'You asked the Oracle\n {msg}\n the response from the 8ball \n{fact}')