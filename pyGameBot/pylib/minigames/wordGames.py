#   Importing Responsories
import sys
import random as r
import time as t
from os import getenv
from dotenv import load_dotenv

#   Discord library
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command

#   Importing local libraries
from pylib.systemModule.databasePython import MariaDB
from pylib.dictionaries.gameDictionaries import Philosopher, JumbleCategory, GameOver,ReactionGame, ScrabbleGame, Hangman

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

        #   Declare a list
        count = []

        while True:

            try :

                #   Prepare and send the Welcome message
                self.embed.title = 'Game Configurations'
                self.embed.description = f'Please choose a level'
                await ctx.send(embed = self.embed)

                #   Wait for an answer and handling the string
                lvl = await self.bot.wait_for('message', timeout=60)
                lvl = int(lvl.content).lower()

                if lvl < 1: raise ValueError('The level can not be less than one')

            except Exception as e : print(type(e))

            else:

                if lvl < 10: count.append(60.0)
                elif lvl > 9 and lvl < 20: count.append(50.0)
                elif lvl > 19 and lvl < 30: count.append(40.0)
                elif lvl > 29 and lvl < 40: count.append(30.0)
                elif lvl > 39 and lvl < 50: count.append(20.0)
                else:
                    count.append(15.0)

            #   Delete and save space
            del lvl

            self.embed.clear_fields()

            return count

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

        jumble = JumbleCategory()

        #   Configure the jumble Settings
        word = []
        sub = ""
        category = ""

                #   Game Configuration
        while True:

            try :

                #   Prepare and send the Welcome message
                self.embed.title = 'Game Configurations'
                self.embed.description = f'Please choose a level'
                await ctx.send(embed = self.embed)

                #   Wait for level input
                lvl = await self.bot.wait_for('message', timeout=60)
                lvl = int(lvl.content).lower()

                #   Check the level input
                if lvl < 1: raise ValueError('The level can not be less than one')

            except Exception as e : print(type(e))

            else:

                #   Configuring the timer based on level
                if lvl < 10: sec = 60.0
                elif lvl > 9 and lvl < 20: sec = 50.0
                elif lvl > 19 and lvl < 30: sec = 40.0
                elif lvl > 29 and lvl < 40: sec = 30.0
                elif lvl > 39 and lvl < 50: sec = 20.0
                else: sec = 15.0

            break


        for i in MariaDB(database= getenv("db2")).SelectTable(getenv("categories"), "Categories"): category += f"**{i}**\n "

        #   Prepare and send the Welcome message
        self.embed.title = 'Welcome to the Jumble Game'
        self.embed.description = f'You have {sec} sec to solve a puzzle, please select one of the categories below:\n\n{category}'
        await ctx.send(embed=self.embed)

        self.embed.clear_fields()

        #   Prepare and retrieve the category
        prompt = await self.bot.wait_for('message', timeout=sec)
        prompt = str(prompt.content).lower()



        #  Walt Disney
        match prompt:

            case "waltdisney":

                #   Select sub categories
                category = MariaDB(database=getenv("db2")).SelectRow(getenv("categories"), 1)

                for i in category[2:]: sub += f"{i}, "

                #   Prepare and send embed message
                self.embed.title = f'Selected category, {category[1]}'
                self.embed.description = f'{sub}'
                await ctx.send(embed=self.embed)

                self.embed.clear_fields()

                #   Prepare and retrieve the sub category
                prompt = await self.bot.wait_for('message', timeout=sec)
                prompt = str(prompt.content).lower()

                answer = MariaDB(database=getenv("db2")).SelectColumn(category[1], "roles", prompt, "characters")

                #   Clearing some space
                del sub
                del category


        while True:

            #   Declear a string variable
            string = ""

            x = len(answer)
            x = r.randrange(0, x)
        
            virvel = jumble.JumbleGenerator(answer[x])
        
            print(answer[x])

            self.embed.title = 'Jumble Game'
            self.embed.description = f'Guess the jumbled word (q to quit): **{virvel}**\n'
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            try :

                #   Prompting the user for a word
                prompt = await self.bot.wait_for('message', timeout=sec)
                prompt = str(prompt.content)

                #   Clear fields

                if prompt == "q":

                    for i in word: string += f"**{i}**,"

                    self.embed.title = f"{GameOver.IncorrectAnswer()}"
                    self.embed.description = f"**Game Summary**\nWords tried : ({string})\n\nThe correct answer : **{answer}**"
                    await ctx.send(embed=self.embed)
 
                    self.embed.clear_fields()

                    break

            except Exception as e: print(e)

            else:

                word.append(prompt)

                #   Combining the answers
                if prompt == answer[x]:

                    for i in word: string += f"{i} "

                    #   Prepare & send the embed message
                    self.embed.title = f'Game Summary'
                    self.embed.description = f'words tried : ( **{string}** )\nCounted {len(word)} attempts.\n{GameOver().CorrectAnswer()}'
                    await ctx.send(embed=self.embed)

                    break

        #   Save space and clear fields
        #del tmpt
        del word
        del string
        del virvel
        del prompt
        del answer

        return

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
        prompt = await self.bot.wait_for('message', timeout=60.0)
        quiz = str(prompt.content)
        prompt = str(prompt.content).lower().split(" ")

        try :

            for i in prompt:
                for j in i:
                    #   if the condition is met raise
                    if str(j).isdigit() : raise ValueError('Numeric inputs is not valid.')

        except Exception as e : sys.exit(e)

        else:

            #   Checking for certain words in prompted message.
            if "how" in prompt[0] or "what" in prompt[0] : prompt = Philosopher().Answer()
            else: prompt = Philosopher().DumbFacts() 

            #   Prepare and send the embed
            self.embed.title = f':8ball: Answer for {quiz}'
            self.embed.description = f'{prompt}'
            await ctx.send(embed=self.embed)

            #   Clear fields and save space

        del arr
        del quiz
        del prompt

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
        arr = ['\U0001FAA8', '\U00002702', '\U0001F4C4']

        #   Game Configuration
        while True:

            try :

                #   Prepare and send the Welcome message
                self.embed.title = 'Game Configurations'
                self.embed.description = f'Please choose a level'
                await ctx.send(embed = self.embed)

                #   Wait for level input
                lvl = await self.bot.wait_for('message', timeout=60)
                lvl = int(lvl.content).lower()

                #   Check the level input
                if lvl < 1: raise ValueError('The level can not be less than one')

            except Exception as e : print(type(e))

            else:

                #   Configuring the timer based on level
                if lvl < 10: sec = 60.0
                elif lvl > 9 and lvl < 20: sec = 50.0
                elif lvl > 19 and lvl < 30: sec = 40.0
                elif lvl > 29 and lvl < 40: sec = 30.0
                elif lvl > 39 and lvl < 50: sec = 20.0
                else: sec = 15.0

            break

        #   Prepare, Send and Add reaction to the message
        self.embed.title = ' Rock Scissors & Paper Game'
        self.embed.description = 'Choose one of the following reaction below'
        message = await ctx.send(embed=self.embed)

        for i in arr:  await message.add_reaction(i)

        try :

            def emojiCheck(reaction, member):

                reaction, member = str(reaction), ctx.author

                return member !=self.bot.user and reaction

            prompt, member = await self.bot.wait_for('reaction_add', timeout=sec, check= emojiCheck)

        except Exception as e : sys.exit(e)

        else:

            prompt = str(prompt)
            x = rsp.RockScissorPaper()

            #   Check for winner and print out output
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

    @command(name="scrabble")
    async def Scrabble(self, ctx):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Prompts the words for each player
            #   Calculating the score for both words
            #   Printing the winner

            #   Player required : 1 - 2

        '''
        #   Initializing lists
        word = []

        #   Prepare and send the Welcome message
        self.embed.title = 'Welcome to the Scrabble Game'
        await ctx.send(embed=self.embed)

        #   Game Configuration
        while True:

            try :

                #   Prepare and send the Welcome message
                self.embed.title = 'Game Configurations'
                self.embed.description = f'Please choose a level'
                await ctx.send(embed = self.embed)

                #   Wait for level input
                lvl = await self.bot.wait_for('message', timeout=60)
                lvl = int(lvl.content)

                #   Check the level input
                if lvl < 1: raise ValueError('The level can not be less than one')

            except (ValueError, TimeoutError) as e : await ctx.send(e)

            else:

                sec = 0
                #   Configuring the timer based on level
                if lvl < 10: sec = 60.0
                elif lvl > 9 and lvl < 20: sec = 50.0
                elif lvl > 19 and lvl < 30: sec = 40.0
                elif lvl > 29 and lvl < 40: sec = 30.0
                elif lvl > 39 and lvl < 50: sec = 20.0
                else: sec = 15.0

            break

        #   Delete and save space
        self.embed.clear_fields()
        
        while True:

            try:

                #   Prompts the words for both players
                self.embed.title = f'Player one, type in a word {sec} to type a word'
                await ctx.send(embed=self.embed)

                p1 = await self.bot.wait_for('message', timeout=sec)
                p1 = str(p1.content)

                self.embed.title = f'Player two, type in a word, {sec} to type a word'
                await ctx.send(embed=self.embed)

                p2 = await self.bot.wait_for('message', timeout=sec)
                p2 = str(p2.content)

                #   Wait for an answer and handling the string
                word = [p1, p2]


                for i in word:
                    if bool(ScrabbleGame().CheckWord(i)) == False: raise ValueError(f"{i}Not a word in the english dictionary")
                    if bool(i) == False: 
                        word.remove(i)
                        word.append(Hangman().ChooseWord())

            except (ValueError, TypeError, TimeoutError) as e:

                print(e)
                continue

            else:

                score = [ScrabbleGame().ComputeScore(word[0]), ScrabbleGame().ComputeScore(word[1])]

                #  Checking whom Scored Highest
                if score[0] > score[1]: self.embed.title = 'Player 1 is the winner'
                elif score[0] < score[1]: self.embed.title = 'Player 2 is the winner'

                else:

                    #   Prepare and send the Welcome message
                    self.embed.title = 'Game over'
                    self.embed.description = GameOver().TowTie()

            await ctx.send(embed=self.embed)
            
            break

        #   Save some space
        del i
        del p1
        del p2
        del lvl
        del word
        del score

        self.embed.clear_fields()

        return

    @command(name = "hangman")
    async def Hangman(self, ctx):

        #   Initializing variables
        x = 20
        sec = 60.0
        letters = ""

        #   Initializing lists
        l = []

        #   Visualizing the hangman
        hangman = []
        answer = Hangman().ChooseWord()

        #   Game Configuration
        while True:

            try :

                #   Prepare and send the Welcome message
                self.embed.title = 'Game Configurations'
                self.embed.description = f'Please choose a level'
                await ctx.send(embed = self.embed)

                #   Wait for level input
                lvl = await self.bot.wait_for('message', timeout=sec)
                lvl = int(lvl.content)

                #   Check the level input
                if lvl < 1: raise ValueError('The level can not be less than one')

            except Exception as e : print(e)

            else:

                #   Configuring the timer based on level
                if lvl < 10: count = 20
                elif lvl > 9 and lvl < 20: count = 15
                elif lvl > 19 and lvl < 30: count = 10
                elif lvl > 29 and lvl < 40: count = 30
                elif lvl > 39 and lvl < 50: count = 20
                else: count = 5

                x -= count

                break

        self.embed.title = "Hangman game"
        self.embed.description = f"Type in a word"
        await ctx.send(embed = self.embed)

        #   Hangman game
        while True:


            if count == 0:

                #   Prepare and print a message
                self.embed.title = "Game Over"
                self.embed.description = f"**Game Summary**\nGuessed: {letters}\nTotal attempts: {len(letters)}\nPlay again?"
                await ctx.send(embed = self.embed)

                break

            #   Decrease by 1
            count -= 1

            try :


                #   Initializing a variable
                string = ""

                #   Prompting a user for a input
                prompt = await self.bot.wait_for("message", timeout = sec)
                prompt = str(prompt.content)

                #   Error messages
                #   Append prompt in list
                if prompt.isdigit(): raise ValueError("String can not contain digits")
                elif prompt in l: raise TypeError("already guessed")
                else:

                    l.append(prompt)

                    #   Create a string, with the letters and / or words
                    for i in l: letters += f"**{i}**, "
                    total = len(l)
                
            except (ValueError, TypeError, TimeoutError) as e :
 
                #   Prepare and print a message
                self.embed.title = "Game Summary"
                print(len(l))
                self.embed.description = f"Counting x words : **{total}**\nLetters typed in : {letters}\nError Message: **{e}**\nType in a letter again"
                #self.embed.set_thumbnail(url = hangman[x])
                await ctx.send(embed = self.embed)
                
                continue

            else:

                #   Checking if prompt is equal to answer
                if prompt in answer:

                    self.embed.title = "Winner"
                    self.embed.description = f"**Game Summary**\nGuessed {letters}\nTotal attempts: {total}\nPlay again?"
                    await ctx.send(embed = self.embed)

                    break

                else:

                    #   Prepare the embed message
                    self.embed.title = "Game Summary"
                    self.embed.description = f"Counting x words : **{total}**\nLetters typed in : {letters}\nError\n{GameOver().IncorrectAnswer()}"
                    #self.embed.set_thumbnail(url = hangman[x])
                    await ctx.send(embed = self.embed)

                    #   clear fields
                    self.embed.clear_fields()
                    self.embed.remove_thumbnail()

            #   increase value for thumbnail
            x += 1

            #   Clear some space
            del prompt

        #   Clear some space
        del x, count
        del prompt, string
        del answer

        #   Prompting for an answer
        prompt = await self.bot.wait_for("message", timeout = sec)
        prompt = str(prompt.content)

        match prompt:
            case "y": self.Hangman()
            case "Yes": self.Hangman()

        return
