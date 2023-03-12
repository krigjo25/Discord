# Python Responsories
import random as r

# Discord Responsories
import discord as d
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog

#   Local responsories
from pylib.dictionaries.gameDictionaries import  GameOver, MathDictionary

class MathGames(Cog):

    """
        Copyright (C) 2023  Kristoffer Gjøsund

        A collection of Mathimatical games

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
    """

    def __init__(self, bot):

        self.bot = bot
        self.embed = Embed(color=Color.dark_purple(), description='')

        return

    math = d.SlashCommandGroup(name = "math", description = "Math Games")

    def GenerateIntegers(self, lvl): return r.randrange(0, lvl * 10)

    def GameConfiguration(self, lvl):

        """
            Game Configurations

            >   Creation Date   : 23.02-23
            >   Last update     :
        """

        x = self.GenerateIntegers(lvl)
        y = self.GenerateIntegers(lvl)

        if lvl < 10: o = MathDictionary().Operators(1)
        elif lvl > 49: o = MathDictionary().Operators(2)
        elif lvl > 69: o = MathDictionary().Operators(3)
        elif lvl > 79: o = MathDictionary().Operators(4)
        elif lvl > 89: o = MathDictionary().Operators(5)
        elif lvl > 99: o = MathDictionary().Operators(6)

        match o:

            case "+":
                n = x + y
                string = f"{x} + {y} = "
            
            case "-":
                 n = x - y
                 string = f"{x} - {y} = "

            case "/":
                n = x / y
                string = f"{x} / {y} = "

            case "*":
                n = x * y
                string = f"{x} * {y} = "
            
            case "//":
                n = x // y
                string = f"{x} // {y} = "

            case "**":
                n = x ** y
                string = f"{x} ** {y} = "

            case "%":
                n = x % y
                string = f"{x} % {y} = "

        arg = []#   Initializing an array & appending into list
        arg.append(n)
        arg.append(string)
        arg.append(5)

        #   Clear some space
        del x, y, n, o
        del string, lvl

        return arg#   Returning the argument

    @math.command()#    Games
    async def littleprofessor(self, ctx: d.ApplicationContext):

        """
            Copyright (C) 2023  Kristoffer Gjøsund

            Little Professor Game

            >   Creation Date   : 23.02-23
            >   Last update     : 
        """

        self.embed.title = "Little Professor"
        self.embed.description = f' Please choose a level'
        await ctx.respond(embed = self.embed)

        while True:#    Configure the game

            lvl = await ctx.bot.wait_for('message', timeout = 60.0, check = lambda m: m.author.id == ctx.author.id)#   Requesting a level from the user

            try:

                if str(lvl.content).isdigit():lvl = int(lvl.content)#   Checking if level is an integer
                else: raise ValueError("Level requires integers not alphabetical characters / glypths")

                if lvl < 0: raise ValueError("The level can not be less than one")
                else: break

            except Exception as e:

                self.embed.title = "An Exception Has Occured"
                self.embed.description = f' {e}'
                await ctx.respond(embed = self.embed)
                continue
        
        arg = self.GameConfiguration(lvl) #   Calculating the answer

        score = 0   #  Initializing the score
        TEMP = arg[2]   #  Initializing user attempts

        while True: #   Littleproffessor Game

            self.embed.title = "Little professor"
            self.embed.description = f' {arg[1]}'
            await ctx.respond(embed = self.embed)

            prmpt = await ctx.bot.wait_for('message', timeout = 60.0, check = lambda m: m.author.id == ctx.author.id)# Prompt the user for a message

            try :

                if str(prmpt.content).isdigit():prmpt = int(prmpt.content)
                else: raise Exception("The requested answer must be integers")

            except Exception as e:

                #   Decrease the score by one
                TEMP -= 1

                self.embed.title = "An Exception Has Occured"
                self.embed.description = f'{e}, try again'
                await ctx.send(embed = self.embed)
                continue

            if prmpt == arg[0]:

                
                score += 1#   Adding one point to score
                arg = self.GameConfiguration(lvl)
                self.embed.title = "Correct !"
                self.embed.description = f'**Game Summuary**\nScore : {score}/5\n attempts left: {TEMP}\n{GameOver().CorrectAnswer("littleprofessor")}'
                await ctx.send(embed = self.embed)

                if score == 5:

                    self.embed.title = "Game Over"
                    self.embed.description = f'**Game Summuary**\nScore : {score}/5\n{GameOver().CorrectAnswer("littleprofessor")}'
                    await ctx.send(embed = self.embed)
                    break

            else :

                TEMP -= 1 # Decrease the attempt by one

                if TEMP < 1:#   Breaking out of the loop

                    self.embed.title = "Game Over"
                    self.embed.description = f'**Game Summuary**\nCorrect number : {arg[0]}\nScore : {score}/9\n{GameOver().IncorrectAnswer("littleprofessor")}'
                    await ctx.send(embed = self.embed)
                    break

                else :# Notify the user its incorrect

                    self.embed.title = 'EEE'
                    self.embed.description = f'{GameOver().IncorrectAnswer("littleprofessor")}'
                    await ctx.send(embed = self.embed)

        #   Clear some space
        del score, TEMP, arg
        del prmpt, lvl

        return

    @math.command()
    async def guessthenumber(self, ctx:d.ApplicationContext):

        """
            Copyright (C) 2023  Kristoffer Gjøsund

            Little Professor Game

            >   Creation Date   : 23.02-23
            >   Last update     : 
        """
        self.embed.title = "Welcome to Guess The Number"
        self.embed.description = f' Please choose a level'
        await ctx.respond(embed = self.embed)

        while True: #   Choose a level

            lvl = await ctx.bot.wait_for('message', timeout = 60.0, check = lambda m: m.author.id == ctx.author.id)#   Requesting a level from the user
            print(lvl)
            try:

                if str(lvl.content).isdigit(): lvl = int(lvl.content)
                else: raise ValueError("The level has to be an integer")

                if lvl < 1: raise ValueError("The level can not be less than one")
                else: break

            except Exception as e:

                self.embed.title = "An Exception Has Occured"
                self.embed.description = f' {e}\n try again'
                await ctx.send(embed = self.embed)
                continue

        #   Game Configurations
        TEMP = 10# Game attemps
        gints = ""

        ints = []#   Declare lists
        n = self.GenerateIntegers(lvl)# Generate a random integer based on level

        self.embed.title = "Guess The Number"
        self.embed.description = f'Game Level : **{lvl}**\nUser attempts : **{TEMP}**\nGuess a number between 0-{lvl*10}'
        await ctx.send(embed = self.embed)

        while True:

            if TEMP <= 0:

                #   Prepare and send the embed message
                self.embed.description = f"Attempts : {TEMP}/3\n{gints}\nThe correct answer were {n}\n{GameOver().IncorrectAnswer()}"
                await ctx.send(embed=self.embed)
                break

            x = await ctx.bot.wait_for('message', timeout = 60.0, check = lambda m: m.author.id == ctx.author.id)#   Requesting an integer from the user

            try :

                if str(x.content).isdigit(): x = int(x.content)
                else: raise ValueError("The level has to be an integer")

            except (ValueError, TypeError) as e:

                self.embed.title = "An error arised"
                self.embed.description = f' {e}\n try again'
                await ctx.send(embed = self.embed)

                continue

            ints.append(x)
            TEMP -= 1#   Decrease the attempt by 1
            for i in ints: gints += f"{i}, "

            if x < n:self.embed.description = f"**Game Summary**\nAttempts left: {TEMP}/5\nIntegers guessed: {gints}\nGuess a number between 0 - {lvl*10}\n{GameOver().IncorrectAnswer('integer', x, n)}"
            elif x > n: self.embed.description = f"**Game Summary**\nAttempts left: {TEMP}/\nIntegers guessed: {gints}\nGuess a number between 0 - {lvl*10}\n\n{GameOver().IncorrectAnswer('integer', x, n)}"
            else: self.embed.description = f"**Game Summary**\nAttempts left: {TEMP}/10\n Integers guessed: {gints}\n{GameOver().CorrectAnswer('integer')}"

            await ctx.send(embed=self.embed)

            if x == n : break

        #   Clear and save space
        del lvl, n, x
        del ints, TEMP

        return

    @math.after_invoke
    async def clear_memory(self, ctx: d.ApplicationContext):

        """
            clearing the chace data

            >   Creation Date   : 23.02-23
            >   Last update     :
        """
        #   Clearing embeds
        self.embed.clear_fields()
        self.embed.remove_image()
        self.embed.remove_author()
        self.embed.remove_footer()
        self.embed.description = ""
        self.embed.remove_thumbnail()
        self.embed.color = d.Colour.dark_purple()

        del ctx #   Clearing some memory
        return