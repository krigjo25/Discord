
# Python Responsories
from random import randrange, randint

# Discord Responsories
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command

# pylib Responsories
from pylib.dictionaries.gameDictionaries import GameDictionary, GameError


import random as r

class MathGame(Cog):

    #   Initializing Classes
    d = GameError()
    gd = GameDictionary()
        
    def __init__(self, bot):
        self.bot = bot
        self.embed = Embed(color=Color.dark_purple(), description='')
        self.error = GameError()
        self.gameDictionarry = GameDictionary()
        return


    async def GameLevel(self, ctx):

        '''
            Choosing the difficulty level,
            the level has to be a positive integer

        '''
        while True:

            try :

                lvl = int(input('level : '))
                #   Prepare & send the embed
                self.embed.title = 'Choose a level'
                await ctx.send(embed=self.embed)

                #   Wait for an answer and handling the string
                lvl = await self.bot.wait_for('message', timeout=60)
                lvl = int(lvl.content)

                if lvl > 0: return lvl

            except (ValueError, TypeError) as e:
                self.embed.title = 'GameError'
                self.embed.description = f'Type in an integer, not a string'
                await ctx.send(embed=self.embed)

            else: 
                self.embed.title = 'GameError'
                self.embed.description = f'Invalid level'
                await ctx.send(embed=self.embed)
                continue


    def GenereateRandomizedInteger(self, mode, arg):

        if mode == 'Guess the number':

            match arg:
                case 1: return r.randint(1, 10)
                case 2: return r.randint(1, 20)
                case 3: return r.randint(1, 30)
                case 4: return r.randint(1, 40)
                case 5: return r.randint(1, 50)
                case 6: return r.randint(1, 60)
                case 7: return r.randint(1, 70)
                case 8: return r.randint(1, 80)
                case 9: return r.randint(1, 90)
                case 10: return r.randint(1, 100)
                case 11: return r.randint(1, 150)
                case 12: return r.randint(1, 200)
                case 13: return r.randint(1, 250)


        if mode == 'Little Professor':

            match arg:
                case 1: return r.randint(1, 9)
                case 2: return r.randint(10, 99)
                case 3: return r.randint(100, 999)
                case 4: return r.randint(1000, 9999)
                case 5: return r.randint(10000, 99999)
                case 6: return r.randint(100000, 9999999)

            if arg == 1 or 4: return r.randint(1, 9)
            elif arg == 2 or 5: return r.randint(10, 99)
            elif arg == 3 or 6: return r.randint(99, 100)

    def GameConfigurations(self, mode, lvl):

        
        if lvl > 0 and lvl < 3:

            # Calculating the integers
            x = self.GenereateRandomizedInteger(mode, lvl)
            y = self.GenereateRandomizedInteger(mode, lvl)

            #   Game Configurations
            operator = '+'
            n = x + y
            i = 3

        return i, operator, n

    @command(name='int')
    async def GuessTheNumber(self, ctx):

        #   Prompting a level input & randomizing the n
        #   Game Config
        lvl = self.GameLevel()
        i,o,n = self.GameConfigurations('Guess the number', lvl)

        #   Declare variable which contain the list
        lList = []
        gList = []
        
        lessOrGreater = f'less than :**{lList}** greater than **{gList}**\n'

        self.embed.description = f' lvl choosen : {lvl}\n attempts :**{i}** attempts, sir.\n'
        await ctx.send(embed=self.embed)

        while True:

            #   Prompting the user
            try :
                x = await self.bot.wait_for('message')
                x = int(x.content)

            except (ValueError, TypeError) as e: print(e)

            else:

                i -= 1

                #   Comparing the values
                if x > n:
                    lList.append(x)
                    self.embed.title = f'**attempts left :** {i} | {lessOrGreater}'
                    self.embed.description = MathGame.gd.CustomAnswer(n, x)
                    await ctx.send(embed=self.embed)

                elif x > n:

                    gList.append(x)
                    self.embed.description = MathGame.gd.CustomAnswer(n, x)
                    await ctx.send(embed=self.embed)

                else:
                    self.embed.description = MathGame.gd.CustomAnswer(n, x)
                    await ctx.send(embed=self.embed)

                if i == 0:

                    #   Prepare and send the embed message
                    self.embed.title = 'The Game is over'
                    self.embed.description = f'{MathGame.gd.GameOver}'
                    self.embed.add_field(name='**Game Summary**', value=f'You guessed **{i}** of **3** times\n<{lList} | {gList}>\nThe correct answer were {x}', inline=False)
                    await ctx.send(embed=self.embed)
        return

    def LittleProfessor(self):

        #   Prompting a level input
        lvl = self.GameLevel()

        #   Game Configurations
        score = 0
        i, mathO, n = self.GameConfigurations('Little Professor', lvl)

        while True:

            try :
                #   Prompting the user for the output
                prmpt = int(input(f'{x} {mathO} {y} ='))

            except ValueError:

                #   Decrease the score by one

                i -= 1
                print('EEE')

                if i == 0: return print(f'Correct number : {n} \n Score : {score}/10')

            else:

                if prmpt == n:

                    #   Adding one point to score
                    score += 1

                    #   Creating a new math problem to be solved
                    x = r.randint(0,10)
                    y = r.randrange(0,10)
                    n = x + y

                elif prmpt != n: 

                    print('EEE')
                    i -= 1

                #   Breaking out of the loop
                if i <= 0: return print(f'Correct number : {n} \n Score : {score}/10')
                elif score == 10: return print(f'Score : {score}')
                return
