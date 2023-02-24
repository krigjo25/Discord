#   Importing Responsories
import os
import sys
import random as r
import time as t

from dotenv import load_dotenv

#   Discord library
import discord as d
from discord import File
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command

#   Importing local libraries
from pylib.systemModule.databasePython import MariaDB
from pylib.dictionaries.gameDictionaries import Philosopher, JumbleCategory, GameOver, ReactionGame, ScrabbleGame, APITools

load_dotenv()

class WordGames(Cog):

    """
        #   A dictionary for Mathimatical games
        >   By              : krigjo25
        >   Creation Date   : 12.01-23
        >   Last update     : 23.02-23

        A collection of word games
    """

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

                if lvl < 10: count = 60.0
                elif lvl > 9 and lvl < 20: count = 50.0
                elif lvl > 19 and lvl < 30: count = 40.0
                elif lvl > 29 and lvl < 40: count = 30.0
                elif lvl > 39 and lvl < 50: count = 20.0
                else:
                    count = 15.0

            #   Delete and save space
            del lvl

            self.embed.clear_fields()

            return count

    word = d.SlashCommandGroup(name = "word", description = "Word games")
    @word.command()
    async def jumble(self, ctx):


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

        #   Game Configuration Sec and tempt
        while True:

            try :

                #   Prepare and send the Welcome message
                self.embed.color = Color.dark_purple()
                self.embed.title = 'Jumble Game Configurations'
                self.embed.description = f'Please choose a level'
                await ctx.send(embed = self.embed)

                #   Wait for level input
                lvl = await self.bot.wait_for('message', timeout=60.0)
                lvl = int(lvl.content)

                #   Check the level input
                if lvl < 1: raise ValueError('The level can not be less than one')

            except Exception as e :

                self.embed.color = Color.dark_red()
                self.embed.title = 'An exception occured'
                self.embed.description = f"{e}"
                await ctx.send(embed = self.embed)

                print(type(e))

            else:

                tempt = 15
                sec = 60.0

                #   Configuring the timer based on level
                if lvl < 10: sec = 60.0
                elif lvl > 9 and lvl < 20: sec = 50.0
                elif lvl > 19 and lvl < 30: sec = 40.0
                elif lvl > 29 and lvl < 40: sec = 30.0
                elif lvl > 39 and lvl < 50: sec = 20.0
                else: sec = 15.0

            break

        category = [i for i in MariaDB(database= os.getenv("database")).SelectTable("categories", "categories")]

        for i in category:
            sub += f"**{i}**, ".capitalize()
        while True:

            #   Prepare and send the Welcome message
            self.embed.color = Color.dark_purple()
            self.embed.title = 'Game Configuration Jumble Game'
            self.embed.description = f'You have {sec} sec to solve a puzzle, please select one of the categories below:\n\n{sub}'
            await ctx.send(embed=self.embed)

            self.embed.clear_fields()
            del sub

            #   Prepare and retrieve the category
            prompt = await self.bot.wait_for('message', timeout=sec)
            prompt = str(prompt.content).lower()

            try :

                if len(prompt) < 2: raise ValueError("Category has to contain more than one character")
                if prompt not in category: raise ValueError("Category does not exist")

            except Exception as e:

                self.embed.color = Color.dark_red()
                self.embed.title = 'An exception occured'
                self.embed.description = f'{e}\nTry again.'
                await ctx.send(embed = self.embed)

            else: break
        

        if prompt in category[0]: answer = APITools().NinjaChoice()
        else:

            try :

                #   Fetch sub categories from database
                category = MariaDB(database=os.getenv("database")).SelectRow("categories", prompt )

            except Exception as e:

                self.embed.color = Color.dark_red()
                self.embed.title = 'An exception occured'
                self.embed.description = f'{e}'
                await ctx.send(embed = self.embed)
                print(e)

            else:

                sub = ""

                #   Iterate through the categories and add category to variable
                for i in category[2:]: sub += f"{i}, "

                #   Prepare and send embed message
                self.embed.description = f'{sub}'
                self.embed.color = Color.dark_purple()
                self.embed.title = f'Selected category, {category[1]}'
                await ctx.send(embed=self.embed)

                self.embed.clear_fields()

                #   Prepare and retrieve the sub category
                prompt = await self.bot.wait_for('message', timeout=sec)
                prompt = str(prompt.content).capitalize()

                #   Fetching the answer from the database
                answer = MariaDB(database=os.getenv("database")).SelectColumn(category[1], "roles", prompt, "characters")
                answer = answer[r.randrange(0, len(answer))]
                #   Randomizing the answer       
                

            #   Clear some space
            del category, sub
            del prompt

        while True:

            #   Declear a string variable
            string = ""
        
            virvel = jumble.JumbleGenerator(answer)

            print(answer)
            self.embed.title = 'Jumble Game'
            self.embed.color = Color.dark_purple()
            self.embed.description = f'Guess the jumbled word (q to quit): **{virvel}**\n'
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            try :

                #   Prompting the user for a word
                prompt = await self.bot.wait_for('message', timeout=sec)
                prompt = str(prompt.content)


            except Exception as e:

                self.embed.title = 'An Exception occured'
                self.embed.color = Color.dark_purple()
                self.embed.description = f'{e} Try again'
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

            else:

                word.append(prompt)

                match prompt:

                    case "q":

                        for i in word: string += f"**{i}**,"

                        #   GameOver message
                        self.embed.title = f"{GameOver.IncorrectAnswer()}"
                        self.embed.color = Color.dark_red()
                        self.embed.description = f"**Game Summary**\nWords tried : ({string})\n\nThe correct answer : **{answer}**"
                        await ctx.send(embed=self.embed)
 
                        self.embed.clear_fields()

                        break

                    case answer:

                        for i in word: string += f"{i} "

                        #   Prepare & send the embed message
                        self.embed.title = f'Game Summary'
                        self.embed.color = Color.dark_purple()
                        self.embed.description = f'words tried : ( **{string}** )\nCounted {len(word)} attempts.\n{GameOver().CorrectAnswer()}'
                        await ctx.send(embed=self.embed)
                        break

            tempt -1
            if tempt == 0:

                self.embed.title = 'Jumble Game'
                self.embed.color = Color.dark_purple()
                self.embed.description = f"**Game Summary**\nWords tried : ({string})\n\nThe correct answer : **{answer}**"
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
                break

        #   Save space and clear fields
        #del tmpt
        del word, string
        del virvel, prompt
        del answer

        return

    @word.command()
    async def eightball(self, ctx):

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
            self.embed.title = f':8ball: Answer for "{quiz}"'
            self.embed.description = f'{prompt}'
            await ctx.send(embed=self.embed)

            #   Clear fields and save space

        del arr
        del quiz
        del prompt

        self.embed.clear_fields()

        return

    @word.command()
    async def scrabble(self, ctx:d.ApplicationContext):

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
        score = []

        #   Prompts the words for both players
        self.embed.title = f'{ctx.author}'
        self.embed.color = Color.dark_purple()
        self.embed.description = f'How many member are going to be playing?'
        await ctx.respond(embed=self.embed)

        n = await ctx.bot.wait_for('message', timeout = 60.0, check = lambda m: m.author.id == ctx.author.id )

        try : 
                if str(n.content).isdigit(): n = int(n.content)
                else: raise ValueError("Please insert a integer ")

                if n < 1: raise ValueError("The number has to be greater than zero")
            
        except Exception as e:
            self.embed.title = f'{ctx.author}'
            self.embed.color = Color.dark_red()
            self.embed.description = f'{e}'
            await ctx.respond(embed = self.embed)
            return


        while True:

            #   Prompts the words for both players
            self.embed.title = f'{ctx.author}'
            self.embed.color = Color.dark_purple()
            self.embed.description = f'Available dictionaries : :england:, :flag_us: 60sec to type a word'
            await ctx.send(embed=self.embed)

            for i in range(len(n)): word.append(await ctx.bot.wait_for('message', timeout=60.0, check = lambda m: m.author.id == ctx.author.id))

            try : 
                for i in word:
                    if str(i.content).isalpha(): word.append(str(i.content))
                    else: raise ValueError("A word does not contain numbers")
            
            except Exception as e:
                self.embed.title = f'{ctx.author}'
                self.embed.color = Color.dark_red()
                self.embed.description = f'{e}'
                await ctx.respond(embed = self.embed)
                continue

            for i in word: score.append(ScrabbleGame().ComputeScore(i))

            max = score[0]
            for i in range(1, len(score)):# Linear algorithm
                if score[i] > max: max = score[i]

                #   Announce the winner
            
            else:

                #   Prepare and send the Welcome message
                self.embed.title = 'Game over'
                self.embed.color = Color.dark_red()
                self.embed.description = GameOver().TowTie()

            await ctx.respond(embed=self.embed)
            
            break

        del word, score#    Clear some memory

        return

    #   Fixes
    @word.command()
    async def rockscissorsandpaper(self, ctx:d.ApplicationContext):

        '''
            Rock, Scissors & paper game

            #   Prompt the user for a string
            #   Combine the answers
            #   Send a philliosofically answer

        '''

        x = ['\U0001FAA8', '\U00002702', '\U0001F4C4']# List with rock scissors and paper

        #   Prepare, Send and Add reaction to the message
        self.embed.title = ' Rock Scissors & Paper Game'
        self.embed.description = 'Choose one of the following reaction below'
        msg = await ctx.respond(embed=self.embed)

        for i in x:  await msg.add_reaction(i)#    add reaction to the embed message

        try : prompt, member = await ctx.bot.wait_for('reaction_add', timeout = 60.0, check = lambda m: m.author.id == ctx.author.id)
        except Exception as e : 

            #   Prepare, Send and Add reaction to the message
            self.embed.title = ' Rock Scissors & Paper Game'
            self.embed.description = f'{e}'
            await ctx.respond(embed=self.embed)
            return

        prompt = str(prompt)
        x = x[r.randrange(0, len(x))]

        if prompt == x: #   Check for winner and print out output

            #   Prepare and send the embed
            self.embed.title = 'Tie'
            self.embed.description = f"{GameOver().TowTie()}"
            await ctx.send(embed = self.embed)

        else:
 
            self.embed.title = "The winner is.."#   If the user win
            if prompt == '\U0001F4C4' and x =='\U0001FAA8': self.embed.description = f"{GameOver().CorrectAnswer('rockscissorpaper', prompt, x)}"
            elif prompt == '\U0001FAA8' and x =='\U00002702': self.embed.description = f"{GameOver().CorrectAnswer('rockscissorpaper', prompt, x)}"
            elif prompt == '\U00002702' and x =='\U0001F4C4': self.embed.description = f"{GameOver().CorrectAnswer('rockscissorpaper', prompt, x)}"

            #   if the bot wins
            if x == '\U0001F4C4' and prompt =='\U0001FAA8': self.embed.description = f"{GameOver().IncorrectAnswer('rockscissorpaper', x, prompt)}"
            elif x == '\U0001FAA8' and prompt =='\U00002702': self.embed.description = f"{GameOver().IncorrectAnswer('rockscissorpaper', x, prompt)}"
            elif x == '\U00002702' and prompt =='\U0001F4C4': self.embed.description = f"{GameOver().IncorrectAnswer('rockscissorpaper', x, prompt)}"

            await ctx.send(embed = self.embed)

            del x, member, prompt#   Clear fields
            return
