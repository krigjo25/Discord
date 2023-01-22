
# Python Responsories
import random as r

# Discord Responsories
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command

#   Importing local libraries
from pylib.systemModule.databasePython import MariaDB
from dictionaries.gameDictionaries import  GameOver

class MathGames():

    '''
        #   Author : krigjo25
        #   Date   :  12.01-23

        #   Collection of Classic WordGames
    '''

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed(color=Color.dark_purple(), description='')

        return

    #   Database connection
    def DatabaseConnection(self, database ,table,  arg):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Connecting to the Database
            #   Creating a new word with joining the elements of the iterator

        '''
        #   Initializing variables & classes
        #db = MariaDB(database =)
        database = database

        #   Selecting from table
        query = f'SELECT {arg} FROM {table}'
        word = db.SelectTable(database, query)

        #   Closing the connection
        db.closeConnection()

        #   Clean up
        del db
        del query
        del database

        return word

    async def GameLevel(self, ctx):

        '''
            #   Choosing the difficulty level of the game
            #   The level has to be greater than 0
        '''

        while True:

            try :

                self.embed.title = 'Choose a level'
                prompt = await self.bot.wait_for('message', timeout=60)
                prompt = str(prompt.content).lower()

                if prompt >= 1 : return prompt
                elif prompt == None: raise TypeError('Input required')
                elif prompt < 0 : raise ValueError('Choose an integer grater than 0')

            except (ValueError, TypeError) as e:
                print(e)
                continue


    def GenerateIntegers(self, lvl):

        match lvl:
            case 1: return r.randint(0, 10)
            case 2: return r.randint(0,20)
            case 3: return r.randint(0,30)
            case 4: return r.randint(0,40)
            case 5: return r.randint(0,50)
            case 6: return r.randint(0,60)
            case 7: return r.randint(0,70)
            case 8: return r.randint(0,80)
            case 9: return r.randint(0,90)
            case 10: return r.randint(0,100)


        return

    def Operators(self, lvl):

        if lvl > 0 and lvl < 10:
            n = x + y
            mf = f"{x} + {y} = "

        if lvl > 19:

            dictionary = {  1:'+',
                            2:'-',
                            3:'/',
                            4:'*',
                            }

            r.shuffle(dictionary)

            arg = []
            rint = r.randint(1, len(dictionary))

            x = self.GenerateIntegers(lvl)
            y = self.GenerateIntegers(lvl)

            match dictionary[rint]:
                case "+":
                    n = x + y
                    mf = f"{x} + {y} = "
            
                case "-":
                    n = x - y
                    mf = f"{x} - {y} = "

                case "/":

                    n = x / y
                    mf = f"{x} / {y} = "

                case "*":
                    n = x * y
                    mf = f"{x} * {y} = "

        if lvl > 99:

            dictionary = {  1:'+',
                            2:'-',
                            3:'/',
                            4:'*',
                            5:"//",
                            6:"**",
                            6:"%",
                            }

            r.shuffle(dictionary)

            arg = []
            rint = r.randint(1, len(dictionary))

            x = self.GenerateIntegers(lvl)
            y = self.GenerateIntegers(lvl)

            match dictionary[rint]:

                case "+":
                    n = x + y
                    mf = f"{x} + {y} = "
            
                case "-":
                    n = x - y
                    mf = f"{x} - {y} = "

                case "/":

                    n = x / y
                    mf = f"{x} / {y} = "

                case "*":
                    n = x * y
                    mf = f"{x} * {y} = "

                case "//":

                    n = x // y
                    mf = f"{x} // {y} = "

                case "**":

                    n = x ** y
                    mf = f"{x} ** {y} = "

                case "%":

                    n = x % y
                    mf = f"{x} % {y} = "

        arg.append(n)
        arg.append(mf)

        #   Returning the 
        return arg

    #   Games
    @command(name="lip")
    async def LittleProffessor(self):

        #   Game Configurations
        #   Prompting a level input
        lvl = self.GameLevel()

        #   Calculating the answer
        arg = self.Operators(lvl)

        #   Initializing variables
        score = 0
        etempt = 3

        while True:

            try :
                #   Prompting the user for the output
                prmpt = int(input(f"{arg[1]}"))

            except ValueError as e:

                #   Decrease the score by one
                etempt -= 1
                print('EEE')
                if etempt == 0: return print(f'Correct number : {arg[0]} \n Score : {score}')

            else:

                if prmpt == arg[0]:

                    #   Adding one point to score
                    score += 1

                    #   Creating a new math problem to be solved
                    x = r.randint(0,10)
                    y = r.randrange(0,10)

                    #   Calculating the answer
                    arg = self.Operators(lvl)


                elif prmpt != arg[0]:

                    print('EEE')
                    etempt -= 1
                    arg = self.Operators(lvl)

                #   Breaking out of the loop
                if etempt <= 0: return print(f'Correct number : {arg[0]} \n Score : {score}/9')
                elif score == 9: return print(f'Score : {score}')

    @command(name="int")
    async def GuessTheNumber(self, ctx):

        #   Initializing variables
        tempt = 3
        lg = f"less than :**{l}** greater than **{g}**\n"

        #   Declare lists
        l = []
        g = []
        t = len(l) + len(g)
        

        #   Game Configurations
        lvl = self.GameLevel()
        n = self.GenerateIntegers(lvl)

        self.embed.description = f' lvl choosen : {lvl}\n attempts :**{i}** attempts, sir.\n'
        await ctx.send(embed=self.embed)

        while True:

            
            try :
                #   Prompting the user
                x = await self.bot.wait_for('message')
                x = int(x.content)

            except (ValueError, TypeError) as e: continue

            else:

                if x > n:
                    l.append(x)
                    self.embed.title = f'**attempts left :** {i} | {lg}'
                    self.embed.description = GameOver.CustomAnswer(n, x)
                    await ctx.send(embed=self.embed)

                elif x > n:

                    g.append(x)
                    self.embed.description = GameOver.CustomAnswer(n, x)
                    await ctx.send(embed=self.embed)

                else:
                    self.embed.description = GameOver.CustomAnswer(n, x)
                    await ctx.send(embed=self.embed)

                if i == 0:

                    #   Prepare and send the embed message
                    self.embed.title = 'The Game is over'
                    self.embed.description = f'{GameOver.IncorrectAnswer()}'
                    self.embed.add_field(name='**Game Summary**', value=f'You guessed **{c}** of **{t}** times\n<{l} | {g}>\nThe correct answer were {x}', inline=False)
                    await ctx.send(embed=self.embed)

            #   Clear and save space
            del lvl
            del n
            del t
            del l
            del g

            self.embed.clear_fields()

            return
