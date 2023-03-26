#   Importing Responsories
import os
import random as r

from dotenv import load_dotenv

#   Discord library
import discord as d
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command

#   Importing local libraries
from lib.system.modal import Socrates
from lib.system.databasePython import MariaDB
from lib.dictionary.game import JumbleCategory, GameOver, ScrabbleGame
from lib.dictionary.tools import APITools

load_dotenv()

class WordGames(Cog):

    """
        A collection of word games

        >   Creation Date   : 12.01-23
        >   Last update     : 23.02-23

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        Copyright (C) 2023  Kristoffer Gjøsund
    """

    word = d.SlashCommandGroup(name = "word", description = "Word games")

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed(color=Color.dark_purple(), description='')

    @word.command()
    async def jumble(self, ctx:d.ApplicationContext):

        """
            Jumble game

            >   Creation date   : 12.01-23
            >   Last update     : 26.02-23
            Copyright (C) 2023  Kristoffer Gjøsund
        """
        
        sub = ""
        category = [i for i in MariaDB(database= os.getenv("database")).SelectTable("categories", "categories")]
        for i in category: sub += f"**{i}**, ".capitalize()

        jumble = JumbleCategory()#  Initializing JumbleCategories

        #   Configure the jumble Settings
        sec = 60.0
        TEMP = 5

        while True:

            #   Prepare and send the Welcome message
            self.embed.color = Color.dark_purple()
            self.embed.title = 'Game Configuration Jumble Game'
            self.embed.description = f'You have {sec} sec to solve a puzzle, you grant {TEMP} attempts\nPlease select one of the categories below:\n\n{sub}'
            await ctx.send(embed=self.embed)

            self.embed.clear_fields()
            del sub

            #   Prepare and retrieve the category
            prompt = await ctx.bot.wait_for('message', timeout=sec)
            prompt = str(prompt.content).lower()

            try :

                if len(prompt) < 2: raise ValueError("Category has to contain more than one character")
                if prompt not in category: raise ValueError("Category does not exist")

            except Exception as e:

                self.embed.color = Color.dark_red()
                self.embed.title = 'An exception occured'
                self.embed.description = f'{e}\nTry again.'
                await ctx.send(embed = self.embed)

            break
        

        if prompt in category[0]: answer = APITools().NinjaRandomWord()

        else:

            try : category = MariaDB(database=os.getenv("database")).SelectRow("categories", prompt )#   Fetch sub categories from database

            except Exception as e:

                self.embed.color = Color.dark_red()
                self.embed.title = 'An Exception Has Occured'
                self.embed.description = f'{e}'
                await ctx.send(embed = self.embed)

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
            prompt = await ctx.bot.wait_for('message', timeout=sec)
            prompt = str(prompt.content).capitalize()

            #   Fetching the answer from the database
            answer = MariaDB(database=os.getenv("database")).SelectColumn(category[1], "roles", prompt, "characters")
            answer = answer[r.randrange(0, len(answer))]#   Randomizing the answer  

        word = []
        score = 0#  Initializing a score
        virvel = jumble.JumbleGenerator(answer)

        while True:# Jumble game

            self.embed.title = 'Jumble Game'
            self.embed.color = Color.dark_purple()
            self.embed.description = f'Guess the jumbled word (q to quit): *{virvel}*'
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            prompt = await ctx.bot.wait_for('message', timeout=sec)#    Prompting the user for a word

            try :

                if str(prompt.content).isalpha(): prompt = str(prompt.content)
                else: raise Exception("Jumble words is not integers")

            except Exception as e:

                TEMP -= 1#  Decreace attempt by one
                
                self.embed.title = 'An Exception Has Occured'
                self.embed.color = Color.dark_purple()
                self.embed.description = f'{e}, Try again'
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

                word.append(prompt)
                continue

            string = "" # Declear a string
            array = ["q", "quit", "exit", "leave"]
            
            if prompt in array:

                for i in word: string += f"**{i}**,"

                #   GameOver message
                self.embed.title = f"{GameOver.IncorrectAnswer('jumble')}"
                self.embed.color = Color.dark_red()
                self.embed.description = f"**Game Summary**\nWords tried : ({string})\n\nThe correct answer : **{answer}**"
                await ctx.send(embed=self.embed)
                break

            word.append(prompt)

            if prompt == answer:

                score += 1# Updating the score
                for i in word: string += f"{i}, "# Creating a string with the attempted words

                #   Prepare & send the embed message
                self.embed.title = f'Game Summary'
                self.embed.color = Color.dark_purple()
                self.embed.description = f'words tried : ( *{string}* )\nCounted {TEMP}/5 attempts.\n{GameOver().CorrectAnswer("jumble")}'
                await ctx.send(embed=self.embed)

                #   Fetching the answer from the database
                answer = MariaDB(database=os.getenv("database")).SelectColumn(category[1], "roles", prompt, "characters")
                answer = answer[r.randrange(0, len(answer))]#   Randomizing the answer 
                virvel = jumble.JumbleGenerator(answer)

            else: TEMP -= 1

            if TEMP == 0:

                for i in word: string += f"{i}, "# Creating a string with the attempted words
                self.embed.title = 'Jumble Game'
                self.embed.color = Color.dark_purple()
                self.embed.description = f"**Game Summary**\nWords tried : ({string})\nThe correct answer : **{answer}**"
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
                break

            if score == 5: break

        #   Save space and clear fields
        del TEMP, word, virvel
        del prompt, answer, category
        del sub
        return

    @word.command()
    async def socrates(self, ctx:d.ApplicationContext):

        """
            An Philiosophic 8ball

            >   Creation date   :  12.01-23
            >   Last update     : 26.02-23
            Copyright (C) 2023  Kristoffer Gjøsund
        """

        #   Prepare & send the embed
        self.embed.title = ':8ball: Ask the Philiospher a question'
        self.embed.description = f' Please write to me what you have in mind.'
        await ctx.send(embed=self.embed)

        modal = Socrates(title = "Ask Socrates")
        await ctx.send_modal(modal)

        return

    @word.command()
    async def scrabble(self, ctx:d.ApplicationContext):

        """
            The scrabble game

            >   Creation Date   : 12.01-23
            >   Last update     : 26.02-23
            Copyright (C) 2023  Kristoffer Gjøsund
        """

        self.embed.title = f'{ctx.author}'
        self.embed.color = Color.dark_purple()
        self.embed.description = f'How many members are going to be playing?'
        await ctx.respond(embed=self.embed)

        n = await ctx.bot.wait_for('message', timeout = 60.0, check = lambda m: m.author.id == ctx.author.id )#    Prompting the user for an integer

        try :#  Check if the prompted player sent an integer
                if str(n.content).isdigit(): n = int(n.content)
                else: raise ValueError("Please insert a integer ")
                if n < 1: raise ValueError("The number has to be greater than zero")

        except Exception as e:
            self.embed.title = f'{ctx.author}'
            self.embed.color = Color.dark_red()
            self.embed.description = f'{e}'
            await ctx.respond(embed = self.embed)
            return

        word = []
        score = []

        while True:#    Prompting the user for player name

            for i in range(n): # Prompts player name for the members
                self.embed.title = f'Scrabble Game'
                self.embed.color = Color.dark_purple()
                self.embed.description = f'Type in the names of the players'
                await ctx.send(embed=self.embed)

                prompt = await ctx.bot.wait_for('message', timeout = 60.0)

                try :#  If the player name exists with-in the guild, append the name
                    for i in ctx.guild.members:
                        if str(prompt.content) == i.name: word.append({'name':str(prompt.content), 'word':''})
                    
                    
                except Exception as e:#   raise an exception, how?
                    self.embed.title = f'An Exception Has Occured'
                    self.embed.color = Color.dark_red()
                    self.embed.description = f'{e}, try again'
                    await ctx.respond(embed = self.embed)
                    break

            for i in range(n):#   Prompts the words for the participating players
                for i in word:

                    self.embed.title = f'Scrabble Game'
                    self.embed.color = Color.dark_purple()
                    self.embed.description = f'Type in a desired word, {i["name"]}'
                    await ctx.send(embed=self.embed)
    
                    prompt = await ctx.bot.wait_for('message', timeout = 60.0)# Find a way to check the author

                    try:#   If the prompted message is alphabetical character append the word

                        if str(prompt.content).isalpha(): i["word"] = str(prompt.content)
                        else: raise Exception(" A word contains only alphabetical characters")

                    except Exception as e:
                        self.embed.title = f'An Exception Has Occured'
                        self.embed.color = Color.dark_red()
                        self.embed.description = f'{e}, start over again'
                        await ctx.respond(embed = self.embed)
                        break

            if n == 1: word.append({'name': 'PyGame', 'word': APITools().NinjaChoice()})

            for i in word: score.append([i['name'], i['word'], ScrabbleGame().ComputeScore(i['word'])])#   Calculating the score

            max = [score[0][0], score [0][1], score[0][2]]
            tie = 0

            for i in range(1, len(score)):# Linear algorithm

                if score[i][2] > max[2]: max = [score[i][0], score[i][1], score[i][2]]
                elif score[i][2] == max[2]:#    If score is eaqual to max
                    tie += 1

            break

        if len(score) == tie:#  If everyone has equal ammount of points 
                        
            self.embed.title = f'Tie!'
            self.embed.description = f'{GameOver.TowTie()}'
            await ctx.respond(embed=self.embed)

        else:#  Else there has to be a winner
            self.embed.title = f'The Winner Is : {max[0]}!'
            self.embed.description = f'**Game Summary**\n {max[0]}, used the word {max[1]}, which gave **{max[0]}** {max[2]} points'
            await ctx.respond(embed=self.embed)

        del word, score, n, max#    Clear some memory
        return

class ReactionGames(Cog):

    """
        A collection of reaction games

        >   Creation Date   : 26.02-23
        >   Last update     : 

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        Copyright (C) 2023  Kristoffer Gjøsund
    """

    reaction = d.SlashCommandGroup(name = "reaction", description = "Reaction Games")

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed(color=Color.dark_purple(), description='')

    @reaction.command()
    async def rockscissorsandpaper(self, ctx:d.ApplicationContext):

        '''
            Rock, Scissors & paper game

            >   Creation Date   : 26.02-23
            >   Last update     :
            Copyright (C) 2023  Kristoffer Gjøsund

        '''

        x = ['\U0001FAA8', '\U00002702', '\U0001F4C4']# List with rock scissors and paper
        x = x[r.randrange(0, len(x) - 1)]#Select one in the list randomly

        #   Prepare, Send and Add reaction to the message
        self.embed.title = ' Rock Scissors & Paper Game'
        self.embed.description = 'Choose one of the following reaction below'
        msg = await ctx.respond(embed=self.embed)
        for i in x:  await msg.add_reaction(i)#    add reaction to the embed message
        print("test")

        try : 
            prompt, member = await ctx.bot.wait_for('reaction_add', timeout = 60.0, check = lambda m: m.author.id == ctx.author.id)
            prompt = str(prompt)
    
        except Exception as e :

            #   Prepare, Send the exception
            self.embed.title = 'An Exception Has Occured'
            self.embed.description = f'{e}'
            await ctx.respond(embed=self.embed)
            return

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
