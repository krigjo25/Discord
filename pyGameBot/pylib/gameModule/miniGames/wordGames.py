#   Importing Responsories
import sys
import random as r

from os import getenv
from dotenv import load_dotenv

#   Discord library
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command

#   Importing local libraries
from pylib.systemModule.databasePython import MariaDB
from dictionaries.gameDictionaries import Philosopher, JumbleCategory, GameOver,ReactionGame, ScrabbleGame

load_dotenv()

class WordGames(Cog):

    '''
        #   Author : krigjo25
        #   Date   :  12.01-23

        #   Collection of Classic WordGames
    '''

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed(color=Color.dark_purple(), description='')

    #   Game Configurations
    async def GameLevel(self, ctx):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Checking if the prompted integer is less than 1

        '''

        try :


            #   Prepare and send the Welcome message
            self.embed.title = 'Jumble Game'
            self.embed.description = f'Please choose a level'
            await ctx.send(embed = self.embed)

            #   Wait for an answer and handling the string
            lvl = await self.bot.wait_for('message', timeout=60)
            lvl = int(lvl.content).lower()

            if lvl < 1: raise ValueError('The level can not be less than one')

        except Exception as e : print(type(e))

        else:

            match lvl:

                case 1: count = 60.0
                case 5: count = 30.0
                case 10: count = 15.0

        #   Delete and save space
        del lvl

        self.embed.clear_fields()

        return count

    #   Database connection
    def DatabaseConnection(self, database ,table,  arg):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Connecting to the Database
            #   Creating a new word with joining the elements of the iterator

        '''
        #   Initializing variables & classes
        db = MariaDB(database= database)
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

    @command(name="jumble")
    async def JumbleGame(self, ctx):


        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Welcome the user to the game & Prompting for category
            #   Promting for a sub category
            #   Randomizing the dictionary word
            #   Request a solve
            #   Creating a new word with joining the elements of the iterator

        '''

        #   Initializing the classes
        db = MariaDB(database= getenv("db2"))
        jumble = JumbleCategory()

        #   Configure the jumble Settings
        word = []
        sec = self.GameLevel()

        #   Prepare and send the Welcome message
        self.embed.title = 'Jumble Game'
        self.embed.description = f'Welcome to the jumble Game\n Yo have {sec} sec to solve the puzzle, please select one of the categories below:\n'

        for category, sub in jumble.JumbleCategories():
            self.embed.add_field(name = f'{category}', value=f'{sub}',inline=True)

        await ctx.send(embed=self.embed)

        #   Clear fields

        self.embed.clear_fields()

        #   Prepare and retrieve the category
        category = await self.bot.wait_for('message', timeout=sec)
        category = str(category.content).lower()


        #  Walt Disney
        match category:

            case "walt disney":

                #   Prepare and send embed message
                self.embed.title = f'Selected Category : {category}'
                self.embed.description = f' please select one of the sub-category below:\n {categories.SubTitle(category)}'
                await ctx.send(embed=self.embed)
        
                #   Clearing the fields
                self.embed.clear_fields()
        
                #   Assigning message from the user and handle it
                prompt = await self.bot.wait_for('message', timeout=sec)
                prompt = str(prompt.content).lower().replace(" ", "")

                answer = jumble.RetrieveDisneyJumble(sub, category)
                answer = str(answer[0])

                virvel = jumble.JumbleGenerator(answer)

                self.embed.title = f'The jumbled Character is seen in \'img\'\n You have **{sec}** sec to resolve which Character it is '
                self.embed.description = f'{virvel}'
                await ctx.send(embed = self.embed)

                #   Clearing the fields
                del prompt
                del category
                self.embed.clear_fields()

        while True:

            try :

                #   Prompting the user for a word
                prompt = await self.bot.wait_for('message', timeout=sec)
                prompt = str(prompt.content)

                #   Append the word
                word.append(prompt)
                virvel = jumble.JumbleGenerator(answer)

            except Exception as e: 
                print(e)


            #   Combining the answers
            if prompt == answer:

                word.append(prompt)

                #   Prepare & send the embed message
                self.embed.title = f'Game Summary'
                self.embed.description = f'words tried : **{word}**\nCounted {len(word)} attempts.\n{GameOver.CorrectAnswer()}'

                return await ctx.send(embed=self.embed)
            else:
                #   Append the word
                word.append(prompt)
                virvel = jumble.JumbleGenerator(answer)

            #   Retruning when reaches zero
            #if tempt == 0: return print(f"{GameOver.IncorrectAnswer()}\nGame Summary\nWords tried : **{word}**\n\nThe correct answer : **{answer}**")

    @command(name="ask")
    async def EightBall(self, ctx):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Prompt the user for an answerAsk a question with what, how or why
            #   Combine the answers
            #   Send a philliosofically answer

        '''

        #   Initializing array
        arr = ['what', 'how', 'why',]

        #   Prepare & send the embed
        self.embed.title = ':8ball: Ask the Philiospher a question'
        self.embed.description = f' Please write to me what you have in mind.'
        await ctx.send(embed=self.embed)

        #   Wait for an answer and handling the string
        prompt = await self.bot.wait_for('message', timeout=60)
        prompt = str(prompt.content).lower()
        prompt = prompt.split(" ")

        try :

            #   Raising valueError
            #   Iterating through the array
            for i in prompt:

                #   Iterating through the array element
                for j in i:

                    #   if the condition is met raise
                    if str(j).isdigit() : raise ValueError('Numeric inputs is not valid.')

        except Exception as e : sys.exit(e)

        else:

            #   Checking for certain words in prompted message.
            if "how" in prompt or "what" in prompt[0] : answer = Philosopher().Answer()
            else: answer = Philosopher().DumbFacts() 

            #   Prepare and send the embed
            self.embed.title = ':8ball: ask the Oracle'
            self.embed.description = f' You asked the Oracle\n \"***{prompt}***\"\n the response \n{answer}'
            await ctx.send(embed=self.embed)

            #   Clear fields and save space

            del arr
            del prompt
            del answer
            self.embed.clear_fields()

            return

    @command(name="rsp")
    async def RockScissorPaper(self, ctx):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Prompt the user for a string
            #   Combine the answers
            #   Send a philliosofically answer

        '''

        #   Initializing classes
        rsp = ReactionGame()

        #   Initializing an array with Rock, Scissors, Paper
        arr = ['\U0001FAA8', '\U00002702', '\U0001F4C4',]

        #   Prepare, Send and Add reaction to the message
        self.embed.title = ' Rock Scissors & Paper Game'
        self.embed.description = 'Choose one of the following reaction below'
        message = await ctx.send(embed=self.embed)

        for i in arr:
            await message.add_reaction(arr[i])

        def emojiCheck(reaction, member):

            reaction = str(reaction)
            member == ctx.author.name 
            return member !=self.bot.user and reaction

        try :

            prompt, member = await self.bot.wait_for('reaction_add', timeout=30.0, check=emojiCheck)

        except Exception as e : sys.exit(e)

        else:

            prompt = str(prompt)
            x = rsp.RockScissorPaper()

            #   Print out the winner
            if prompt == x:

                #   Prepare and send the embed
                self.embed.title = 'Tie'
                self.embed.description = f"{rsp.TowTie()}"
                await ctx.send(embed = self.embed)

            else:

                #   If the user win
                self.embed.title = "The winner is.."
                if prompt == '\U0001F4C4' and x =='\U0001FAA8': self.embed.description = f"{rsp.Player(prompt,x)}"
                if prompt == '\U0001FAA8' and x =='\U00002702': self.embed.description = f"{rsp.Player(prompt,x)}"
                if prompt == '\U00002702' and x =='\U0001F4C4': self.embed.description = f"{rsp.Player(prompt,x)}"

                 #   if the bot wins
                if x == '\U0001F4C4' and prompt =='\U0001FAA8': self.embed.description = f"{rsp.Computer(x)}"
                if x == '\U0001FAA8' and prompt =='\U00002702': self.embed.description = f"{rsp.Computer(x)}"
                if x == '\U00002702' and prompt =='\U0001F4C4': self.embed.description = f"{rsp.Computer(x)}"

                await ctx.send(embed = self.embed)

                #   Clear fields
                del x
                del rsp
                del arr
                del member
                del prompt
                del message

                self.embed.clear_fields()
                
                return

    def Scrabble(self):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Prompts the words for each player
            #   Calculating the score for both words
            #   Printing the winner

            #   Player required : 1 - 2
        '''

        try:

            #   Prompts the words for both players
            word = [str(input("Player 1: ")), str(input("Player 2: "))]

            for i in str(word):
                if i.isdigit(): raise ValueError('Can not contain digits')

            for i in word:

                if i == '':
                    word.remove(i)
                    string = f'{ScrabbleGame().PlayerComputer()}'
                    print(string)
                    word.append()
            print(word)

        except Exception as e:  print(e)

        else:

            score = [ScrabbleGame().ComputeScore(word[0]), ScrabbleGame().ComputeScore(word[1])]

            #  Checking whom Scored Highest and print the winner
            if score[0] > score[1]: print("Player 1 is the winner")
            elif score[0] < score[1]: print("Player 2 is the winner")
            else: print(GameOver().TowTie())

            #   Clean up
            del word
            del score
        
        return
