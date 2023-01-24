
# Python Responsories
import random as r

# Discord Responsories
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command

#   Importing local libraries
from pylib.systemModule.databasePython import MariaDB
from pylib.dictionaries.gameDictionaries import  GameOver, MathDictionary

class MathGames(Cog):

    '''
        #   Author : krigjo25
        #   Date   :  12.01-23

        #   Collection of Classic Math Games
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

    def GameConfigurationLittleproffessor(self, lvl):

        #   Initializing an array
        arg = []

        #   Initializing x, y & o
        o = 0
        x = self.GenerateIntegers(lvl)
        y = self.GenerateIntegers(lvl)

        if lvl < 10:

            #   Math Question
            n = x + y
            mf = f"{x} + {y} = "

            #   Attempts
            tempt = 5

        elif lvl > 19:

            #   Generate integers, math question
            x = self.GenerateIntegers(lvl)
            y = self.GenerateIntegers(lvl)
            o = MathDictionary.Operators()

            #   Attempts
            tempt = 5

            match o:
    
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

        elif lvl > 99:

            x = self.GenerateIntegers(lvl)
            y = self.GenerateIntegers(lvl)
            o = MathDictionary.Operators()

            match o:

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

        #   Appending to the list
        arg.append(n)
        arg.append(mf)
        arg.append(tempt)

        #   Clear some space
        del x, y, n, o
        del mf, lvl, tempt

        #   Returning the argument
        return arg

    #   Games
    @command(name="lip")
    async def LittleProffessor(self, ctx):

        self.embed.title = "Little professor"
        self.embed.description = f' Please choose a level'
        await ctx.send(embed = self.embed)

        #   Checking if the answer is an integer
        while True:

            try:

                lvl = await self.bot.wait_for('message', timeout=60)
                lvl = int(lvl.content)

                if lvl > 0: break
                else: raise ValueError("The level can not be less than one")

            except Exception as e:

                self.embed.title = "An error arised"
                self.embed.description = f' {e}\n try again'
                await ctx.send(embed = self.embed)
                continue

        #   Calculating the answer
        arg = self.GameConfigurationLittleproffessor(lvl)

        #   Initializing variables
        score = 0
        etempt = arg[2]

        while True:

            try :

                self.embed.title = "Little professor"
                self.embed.description = f' {arg[1]}'
                await ctx.send(embed = self.embed)
                
                prmpt = await self.bot.wait_for('message', timeout=60)
                prmpt = int(prmpt.content)

            except ValueError as e:

                #   Decrease the score by one
                etempt -= 1

                if etempt <= 0:

                    self.embed.title = "Game Over"
                    self.embed.description = f'**Game Summuary**\nCorrect number : {arg[0]}\nScore : {score}/9'
                    await ctx.send(embed = self.embed)
                    break

                self.embed.title = "EEE"
                self.embed.description = f'Try again'
                await ctx.send(embed = self.embed)

                
            else:

                if prmpt == arg[0]:

                    #   Adding one point to score
                    score += 1

                    if score == 9:

                        self.embed.title = "Game Over"
                        self.embed.description = f'**Game Summuary**\nScore : {score}/9'
                        await ctx.send(embed = self.embed)
                        break

                    else:

                        #   Calculating the answer
                        arg = self.GameConfigurationLittleproffessor(lvl)


                else :

                    etempt -= 1

                    #   Breaking out of the loop
                    if etempt <= 0:

                        self.embed.title = "Game Over"
                        self.embed.description = f'**Game Summuary**\nCorrect number : {arg[0]}\nScore : {score}/9'
                        await ctx.send(embed = self.embed)
                        break

                    else :

                        self.embed.title = "EEE"
                        self.embed.description = "try again"
                        await ctx.send(embed = self.embed)




                    arg = self.GameConfigurationLittleproffessor(lvl)
                    print(arg)

        #   Clear some space
        del score, etempt
        del prmpt, arg, lvl

        return

    @command(name="int")
    async def GuessTheNumber(self, ctx):

        self.embed.title = "Welcome to Guess the number"
        self.embed.description = f' Please choose a level'
        await ctx.send(embed = self.embed)

        #   Checking if the answer is an integer
        while True:

            try:

                lvl = await self.bot.wait_for('message', timeout=60)
                lvl = int(lvl.content)

                if lvl > 0: break
                else: raise ValueError("The level can not be less than one")

            except Exception as e:

                self.embed.title = "An error arised"
                self.embed.description = f' {e}\n try again'
                await ctx.send(embed = self.embed)
                continue

        n = self.GenerateIntegers(lvl)

        #   Initializing variables
        tempt = 3
        gints = "Gussed numbers : "

        #   Declare lists
        ints = []

        #   Game Conftemptgurations
        self.embed.title = "Guess the number"
        self.embed.description = f'Game Level : {lvl}\nUser attempts : {tempt}'
        await ctx.send(embed = self.embed)

        while True:

            
            try :

                #   Prompting the user
                print(n)
                x = await self.bot.wait_for('message')
                x = int(x.content)

                t = len(ints)

                ints.append(x)

                for i in ints:
                    gints += f"{i}, "


            except (ValueError, TypeError) as e:

                self.embed.title = "An error arised"
                self.embed.description = f' {e}\n try again'
                await ctx.send(embed = self.embed)

                continue

            else:

                if x == n:

                    #score += 1
                    self.embed.title = "Game Summuary"
                    self.embed.description = f"Attempts left : {tempt}\n{gints}\n{GameOver().CustomAnswer(n, x)}"
                    await ctx.send(embed=self.embed)
                    break

                else:

                    #   Decrease the attempt by 1
                    tempt -= 1

                    if tempt == 0:

                        #   Prepare and send the embed message
                        self.embed.title = 'Game Summuary'
                        self.embed.description = f"Attempts : {t}/{t}\n{gints}\nThe correct answer were {x}\n{GameOver().IncorrectAnswer()}"
                        await ctx.send(embed=self.embed)
                        break
    
                    if x < n:

                        #   Prepare embed message
                        self.embed.title = f'Game Summuary'
                        self.embed.description = f"Attempts left : {tempt}\n{gints}\n{GameOver().CustomAnswer(n, x)}"

                    elif x > n:

                        #   Prepare embed message
                        self.embed.title = f'Game Summuary'
                        self.embed.description = f"Attempts left : {tempt}\n{gints}\n{GameOver().CustomAnswer(n, x)}"

            await ctx.send(embed=self.embed)

        #   Clear and save space
        del lvl
        del n
        del t

        self.embed.clear_fields()

        return
