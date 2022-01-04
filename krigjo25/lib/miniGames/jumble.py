import os
from random import randrange

# dotenv
from dotenv import load_dotenv

#   mariadb
import mariadb

#   Discord Repositories
from discord import channel, utils
from discord.embeds import Embed
from discord.colour import Color
from discord.member import Member
from discord.message import Message
from discord.ext.commands import Cog, command

#   Jumble Repositories
#from lib.jumbles.movies import Movies
from lib.jumbles.disney import Disney
from lib.jumbles.jumble import Jumble
#from lib.jumbles.dcComics import DCComics
#from lib.jumbles.marvelComics import MarvelComics
from lib.jumbles.dictionaries import Dictionaries


#   Asynico Repositories
import asyncio

load_dotenv()

class JumbleGame(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Answer = Dictionaries.CorrectAnswer()
        self.GameOver = Dictionaries.jumbleOver()
        self.modeError = Dictionaries.DifficultyError()
        self.embed = Embed(color=Color.dark_purple(), description='')
        self.conn = mariadb.connect(
                    user = os.getenv('USER'),
                    host = os.getenv('HOST'),
                    port = os.getenv('PORT'),
                    db = os.getenv('DATABASE'),
                    password = os.getenv('PASSWORD')
        )
        self.cur = self.conn.cursor()    

    @command(name='jumble')

    #   Send a welcome message to the user, ask him to select first a category, then a sub category
    #   When a user has selected a subCategory, the program sends out a random word from a dictonary and jumble it before send.
    #   When the user recieves the word, he has 120 seconds on easiest mode to decode it. easy- kimpossible : 60 , 
    
    async def jumble(self,ctx):
        

        # Categories list  x - Database
        titles = [ 
                        
                        [ 
                            'Animations', 
                            '- Disney\n:x:- Marvel-Comics\n- DC-Comics'
                        ],
                        
                    ]
        
        #   Jumble configurations
        word = []
        atNum = 0
        limit = 4
        sec = 60.0

        #   Prepare and send the embeded message
        self.embed.title = 'Jumble Game'
        self.embed.description = f'Welcome to the jumble Game\n You grant {limit} attempts and default time limit : {sec} please select one of the sub-categories below:\n'
            
        # Creating a for loop to handle the list
        for category, sub in titles:
            self.embed.add_field(name = f'{category}', value=f'{sub}',inline=True)
        await ctx.send(embed=self.embed)
        
        #   Clearing the fields
        self.embed.clear_fields()
        
        #   Assigning message from the user and handle it
        subChoice = await self.bot.wait_for('message', timeout=sec)
        subChoice = str(subChoice.content)
        subChoice = subChoice.capitalize()

        #  Disney
        if subChoice == 'Disney':
            
            titles = [
                        [ 
                            f'{subChoice}', 
                            ' - Heros \n- Villans \n- Princesses\n- Villans\n- Classics'
                        ],
                        
                    ]
            #   Prepare and send embed message
            self.embed.title = f'Genre : {subChoice}'
            self.embed.description = f' please select one of the sub-genres below:\n'
            
            #   Creating a for loop to handle the list
            for category, sub in titles:
                self.embed.add_field(name = f'{category}', value=f'{sub}',inline=True)
            await ctx.send(embed=self.embed)
        
            #   Clearing the fields
            self.embed.clear_fields()
        
            #   Assigning message from the user and handle it
            subGenre = await self.bot.wait_for('message', timeout=sec)
            subGenre = str(subGenre.content)
            subGenre = subGenre.capitalize()

            
            #  if a sub-category is choosen
            if subGenre == 'Heros':

                #   Calling the choice function
                answer = Disney.DisneyEasyHeros()
                virvel = Jumble.Jumble(answer)

                # Creating a list to fetch the query inside, and procsess the request to the database
                ch = []
                query = f'SELECT characterName FROM disneyCharactersEasy WHERE characterName = "{answer}"'
                self.cur.execute(query)
                data = self.cur.fetchall()

                for i in data:
                    ch.append(i[0])

                # Creating and prepare a embeded message to the user
                self.embed.title = f'The jumbled Character is seen in \"{ch[0]}\" You have **{sec}** and **{limit}** attempts to resolve which Character it is '
                self.embed.description = f'{virvel}'
                await ctx.send(embed=self.embed)

                while True:
                    
                    #   Calling the jumbled function
                    virvel = Jumble.Jumble(answer)

                    #   Retrieve the user's word choice
                    choice = await self.bot.wait_for('message', timeout=sec)
                    choice = str(choice.content)

                    #   If the choosen answer is the same as the answer
                    if choice == answer:
                        atNum +=1
                        word.append(choice)
                        await ctx.send(f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.Answer} **{answer}**')
                        break
        
                    # else if  the counter reaches max attempts 
                    elif atNum == limit:

                        #   Prepare and send the embed message
                        self.embed.title = 'The Game is over'
                        self.embed.description = f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.GameOver} **{answer}**'
                        await ctx.send(embed=self.embed)

                        # Get out of the loop
                        break

                    #   Else if the choice is not equal to the answer
                    else:
                        atNum += 1
                        word.append(choice)

                        self.embed.title = f'**{atNum}** / **{limit}** | attempted words : **{word}**'
                        self.embed.description = f'{virvel}'
                        await ctx.send(embed=self.embed)

                        #   Continue the loop
                        continue            

            elif subGenre == 'Princesses':
                
                #   Calling the choice function
                answer = Disney.DisneyEasyPrincesses()
                virvel = Jumble.Jumble(answer)

                #   Creating a list to fetch the query inside, and procsess the request to the database
                ch = []
                query = f'SELECT filmSeries FROM disneyCharactersEasy WHERE characterName = "{answer}"'
                self.cur.execute(query)
                data = self.cur.fetchall()

                for i in data:
                    ch.append(i[0])

                # Creating and prepare a embeded message to the user
                self.embed.title = f'The selected Character is from the Movie {ch[0]} You have **{sec}** and **{limit}** attempts to resolve the word. '
                self.embed.description = f'{virvel}'


                await ctx.send(embed=self.embed)

                while True:

                    #   Calling the jumbled function
                    virvel = Jumble.Jumble(answer)

                    #   Retrieve the user's word choice
                    choice = await self.bot.wait_for('message', timeout=sec)
                    choice = str(choice.content)

                    #   If the choosen answer is the same as the answer
                    if choice == answer:
                        await ctx.send(f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.Answer} **{answer}**')
                        break

                    # else if  the counter reaches max attempts 
                    elif atNum == limit:
    
                        #   Prepare and send the embed message
                        self.embed.title = 'The Game is over'
                        self.embed.description = f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.GameOver} **{answer}**'
                        await ctx.send(embed=self.embed)

                        # Get out of the loop
                        break

                    #   Else if the choice is not equal to the answer
                    else:
                        atNum += 1
                        word.append(choice)

                        self.embed.title = f'**{atNum}** / **{limit}** | attempted words : **{word}**'
                        self.embed.description = f'{virvel}'
                        await ctx.send(embed=self.embed)

                        #   Continue the loop
                        continue
            
            elif subGenre == 'Villans':
                
                #   Calling the choice function
                answer = Disney.DisneyEasyVillans()
                virvel = Jumble.Jumble(answer)

                #   Creating a list to fetch the query inside, and procsess the request to the database
                ch = []
                query = f'SELECT filmSeries FROM disneyCharactersEasy WHERE characterName = "{answer}"'
                self.cur.execute(query)
                data = self.cur.fetchall()

                for i in data:
                    ch.append(i[0])

                # Creating and prepare a embeded message to the user
                self.embed.title = f'The selected character is from the movie {ch[0]} You have **{sec}** and **{limit}** attempts to resolve the word. '
                self.embed.description = f'{virvel}'


                await ctx.send(embed=self.embed)

                while True:

                    #   Calling the jumbled function
                    virvel = Jumble.Jumble(answer)

                    #   Retrieve the user's word choice
                    choice = await self.bot.wait_for('message', timeout=sec)
                    choice = str(choice.content)

                    #   If the choosen answer is the same as the answer
                    if choice == answer:
                        await ctx.send(f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.Answer} **{answer}**')
                        break

                    # else if  the counter reaches max attempts 
                    elif atNum == limit:
    
                        #   Prepare and send the embed message
                        self.embed.title = 'The Game is over'
                        self.embed.description = f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.GameOver} **{answer}**'
                        await ctx.send(embed=self.embed)

                        # Get out of the loop
                        break

                    #   Else if the choice is not equal to the answer
                    else:
                        atNum += 1
                        word.append(choice)

                        self.embed.title = f'**{atNum}** / **{limit}** | attempted words : **{word}**'
                        self.embed.description = f'{virvel}'
                        await ctx.send(embed=self.embed)

                        #   Continue the loop
                        continue

            elif subGenre == 'Classics':
                
                #   Calling the choice function
                answer = Disney.DisneyEasyClassics()
                virvel = Jumble.Jumble(answer)

                # Creating and prepare a embeded message to the user
                self.embed.title = f'You have **{sec}** and **{limit}** attempts to resolve the word. '
                self.embed.description = f'{virvel}'


                await ctx.send(embed=self.embed)

                while True:

                    #   Calling the jumbled function
                    virvel = Jumble.Jumble(answer)

                    #   Retrieve the user's word choice
                    choice = await self.bot.wait_for('message', timeout=sec)
                    choice = str(choice.content)

                    #   If the choosen answer is the same as the answer
                    if choice == answer:
                        await ctx.send(f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.Answer} **{answer}**')
                        break

                    # else if  the counter reaches max attempts 
                    elif atNum == limit:
    
                        #   Prepare and send the embed message
                        self.embed.title = 'The Game is over'
                        self.embed.description = f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.GameOver} **{answer}**'
                        await ctx.send(embed=self.embed)

                        # Get out of the loop
                        break

                    #   Else if the choice is not equal to the answer
                    else:
                        atNum += 1
                        word.append(choice)

                        self.embed.title = f'**{atNum}** / **{limit}** | attempted words : **{word}**'
                        self.embed.description = f'{virvel}'
                        await ctx.send(embed=self.embed)

                        #   Continue the loop
                        continue

          #  Marvel Comics
        elif subChoice == 'Marvel':
            titles = [
                        [ 
                            f'{subChoice}', 
                            ' - Heros \n- Villans \n- Princesses\n- Villans\n- Classics'
                        ],
                        
                    ]
            #   Prepare and send embed message
            self.embed.title = f'Genre : {subChoice}'
            self.embed.description = f' please select one of the sub-genres below:\n'
            
            #   Creating a for loop to handle the list
            for category, sub in titles:
                self.embed.add_field(name = f'{category}', value=f'{sub}',inline=True)
            await ctx.send(embed=self.embed)
        
            #   Clearing the fields
            self.embed.clear_fields()
        
            #   Assigning message from the user and handle it
            subGenre = await self.bot.wait_for('message', timeout=sec)
            subGenre = str(subGenre.content)
            subGenre = subGenre.capitalize()

            
            #  if a sub-category is choosen
            if subGenre == 'Heros':

                #   Calling the choice function
                answer = Disney.DisneyEasyHeros()
                virvel = Jumble.Jumble(answer)

                # Creating a list to fetch the query inside, and procsess the request to the database
                ch = []
                query = f'SELECT characterName FROM disneyCharactersEasy WHERE characterName = "{answer}"'
                self.cur.execute(query)
                data = self.cur.fetchall()

                for i in data:
                    ch.append(i[0])

                # Creating and prepare a embeded message to the user
                self.embed.title = f'The jumbled Character is seen in \"{ch[0]}\" You have **{sec}** and **{limit}** attempts to resolve which Character it is '
                self.embed.description = f'{virvel}'
                await ctx.send(embed=self.embed)

                while True:
                    
                    #   Calling the jumbled function
                    virvel = Jumble.Jumble(answer)

                    #   Retrieve the user's word choice
                    choice = await self.bot.wait_for('message', timeout=sec)
                    choice = str(choice.content)

                    #   If the choosen answer is the same as the answer
                    if choice == answer:
                        atNum +=1
                        word.append(choice)
                        await ctx.send(f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.Answer} **{answer}**')
                        break
        
                    # else if  the counter reaches max attempts 
                    elif atNum == limit:

                        #   Prepare and send the embed message
                        self.embed.title = 'The Game is over'
                        self.embed.description = f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.GameOver} **{answer}**'
                        await ctx.send(embed=self.embed)

                        # Get out of the loop
                        break

                    #   Else if the choice is not equal to the answer
                    else:
                        atNum += 1
                        word.append(choice)

                        self.embed.title = f'**{atNum}** / **{limit}** | attempted words : **{word}**'
                        self.embed.description = f'{virvel}'
                        await ctx.send(embed=self.embed)

                        #   Continue the loop
                        continue            

            elif subGenre == 'Princesses':
                
                #   Calling the choice function
                answer = Disney.DisneyEasyPrincesses()
                virvel = Jumble.Jumble(answer)

                #   Creating a list to fetch the query inside, and procsess the request to the database
                ch = []
                query = f'SELECT filmSeries FROM disneyCharactersEasy WHERE characterName = "{answer}"'
                self.cur.execute(query)
                data = self.cur.fetchall()

                for i in data:
                    ch.append(i[0])

                # Creating and prepare a embeded message to the user
                self.embed.title = f'The selected Character is from the Movie {ch[0]} You have **{sec}** and **{limit}** attempts to resolve the word. '
                self.embed.description = f'{virvel}'


                await ctx.send(embed=self.embed)

                while True:

                    #   Calling the jumbled function
                    virvel = Jumble.Jumble(answer)

                    #   Retrieve the user's word choice
                    choice = await self.bot.wait_for('message', timeout=sec)
                    choice = str(choice.content)

                    #   If the choosen answer is the same as the answer
                    if choice == answer:
                        await ctx.send(f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.Answer} **{answer}**')
                        break

                    # else if  the counter reaches max attempts 
                    elif atNum == limit:
    
                        #   Prepare and send the embed message
                        self.embed.title = 'The Game is over'
                        self.embed.description = f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.GameOver} **{answer}**'
                        await ctx.send(embed=self.embed)

                        # Get out of the loop
                        break

                    #   Else if the choice is not equal to the answer
                    else:
                        atNum += 1
                        word.append(choice)

                        self.embed.title = f'**{atNum}** / **{limit}** | attempted words : **{word}**'
                        self.embed.description = f'{virvel}'
                        await ctx.send(embed=self.embed)

                        #   Continue the loop
                        continue
            
            elif subGenre == 'Villans':
                
                #   Calling the choice function
                answer = Disney.DisneyEasyVillans()
                virvel = Jumble.Jumble(answer)

                #   Creating a list to fetch the query inside, and procsess the request to the database
                ch = []
                query = f'SELECT filmSeries FROM disneyCharactersEasy WHERE characterName = "{answer}"'
                self.cur.execute(query)
                data = self.cur.fetchall()

                for i in data:
                    ch.append(i[0])

                # Creating and prepare a embeded message to the user
                self.embed.title = f'The selected character is from the movie {ch[0]} You have **{sec}** and **{limit}** attempts to resolve the word. '
                self.embed.description = f'{virvel}'


                await ctx.send(embed=self.embed)

                while True:

                    #   Calling the jumbled function
                    virvel = Jumble.Jumble(answer)

                    #   Retrieve the user's word choice
                    choice = await self.bot.wait_for('message', timeout=sec)
                    choice = str(choice.content)

                    #   If the choosen answer is the same as the answer
                    if choice == answer:
                        await ctx.send(f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.Answer} **{answer}**')
                        break

                    # else if  the counter reaches max attempts 
                    elif atNum == limit:
    
                        #   Prepare and send the embed message
                        self.embed.title = 'The Game is over'
                        self.embed.description = f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.GameOver} **{answer}**'
                        await ctx.send(embed=self.embed)

                        # Get out of the loop
                        break

                    #   Else if the choice is not equal to the answer
                    else:
                        atNum += 1
                        word.append(choice)

                        self.embed.title = f'**{atNum}** / **{limit}** | attempted words : **{word}**'
                        self.embed.description = f'{virvel}'
                        await ctx.send(embed=self.embed)

                        #   Continue the loop
                        continue

            elif subGenre == 'Classics':
                
                #   Calling the choice function
                answer = Disney.DisneyEasyClassics()
                virvel = Jumble.Jumble(answer)

                # Creating and prepare a embeded message to the user
                self.embed.title = f'You have **{sec}** and **{limit}** attempts to resolve the word. '
                self.embed.description = f'{virvel}'


                await ctx.send(embed=self.embed)

                while True:

                    #   Calling the jumbled function
                    virvel = Jumble.Jumble(answer)

                    #   Retrieve the user's word choice
                    choice = await self.bot.wait_for('message', timeout=sec)
                    choice = str(choice.content)

                    #   If the choosen answer is the same as the answer
                    if choice == answer:
                        await ctx.send(f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.Answer} **{answer}**')
                        break

                    # else if  the counter reaches max attempts 
                    elif atNum == limit:
    
                        #   Prepare and send the embed message
                        self.embed.title = 'The Game is over'
                        self.embed.description = f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.GameOver} **{answer}**'
                        await ctx.send(embed=self.embed)

                        # Get out of the loop
                        break

                    #   Else if the choice is not equal to the answer
                    else:
                        atNum += 1
                        word.append(choice)

                        self.embed.title = f'**{atNum}** / **{limit}** | attempted words : **{word}**'
                        self.embed.description = f'{virvel}'
                        await ctx.send(embed=self.embed)

                        #   Continue the loop
                        continue

        elif subChoice == 'DcComics':
            titles = [
                        [ 
                            f'{subChoice}', 
                            ' - Heros \n- Villans \n- Princesses\n- Villans\n- Classics'
                        ],
                        
                    ]
            #   Prepare and send embed message
            self.embed.title = f'Genre : {subChoice}'
            self.embed.description = f' please select one of the sub-genres below:\n'
            
            #   Creating a for loop to handle the list
            for category, sub in titles:
                self.embed.add_field(name = f'{category}', value=f'{sub}',inline=True)
            await ctx.send(embed=self.embed)
        
            #   Clearing the fields
            self.embed.clear_fields()
        
            #   Assigning message from the user and handle it
            subGenre = await self.bot.wait_for('message', timeout=sec)
            subGenre = str(subGenre.content)
            subGenre = subGenre.capitalize()

            
            #  if a sub-category is choosen
            if subGenre == 'Heros':

                #   Calling the choice function
                answer = Disney.DisneyEasyHeros()
                virvel = Jumble.Jumble(answer)

                # Creating a list to fetch the query inside, and procsess the request to the database
                ch = []
                query = f'SELECT characterName FROM disneyCharactersEasy WHERE characterName = "{answer}"'
                self.cur.execute(query)
                data = self.cur.fetchall()

                for i in data:
                    ch.append(i[0])

                # Creating and prepare a embeded message to the user
                self.embed.title = f'The jumbled Character is seen in \"{ch[0]}\" You have **{sec}** and **{limit}** attempts to resolve which Character it is '
                self.embed.description = f'{virvel}'
                await ctx.send(embed=self.embed)

                while True:
                    
                    #   Calling the jumbled function
                    virvel = Jumble.Jumble(answer)

                    #   Retrieve the user's word choice
                    choice = await self.bot.wait_for('message', timeout=sec)
                    choice = str(choice.content)

                    #   If the choosen answer is the same as the answer
                    if choice == answer:
                        atNum +=1
                        word.append(choice)
                        await ctx.send(f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.Answer} **{answer}**')
                        break
        
                    # else if  the counter reaches max attempts 
                    elif atNum == limit:

                        #   Prepare and send the embed message
                        self.embed.title = 'The Game is over'
                        self.embed.description = f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.GameOver} **{answer}**'
                        await ctx.send(embed=self.embed)

                        # Get out of the loop
                        break

                    #   Else if the choice is not equal to the answer
                    else:
                        atNum += 1
                        word.append(choice)

                        self.embed.title = f'**{atNum}** / **{limit}** | attempted words : **{word}**'
                        self.embed.description = f'{virvel}'
                        await ctx.send(embed=self.embed)

                        #   Continue the loop
                        continue            

            elif subGenre == 'Princesses':
                
                #   Calling the choice function
                answer = Disney.DisneyEasyPrincesses()
                virvel = Jumble.Jumble(answer)

                #   Creating a list to fetch the query inside, and procsess the request to the database
                ch = []
                query = f'SELECT filmSeries FROM disneyCharactersEasy WHERE characterName = "{answer}"'
                self.cur.execute(query)
                data = self.cur.fetchall()

                for i in data:
                    ch.append(i[0])

                # Creating and prepare a embeded message to the user
                self.embed.title = f'The selected Character is from the Movie {ch[0]} You have **{sec}** and **{limit}** attempts to resolve the word. '
                self.embed.description = f'{virvel}'


                await ctx.send(embed=self.embed)

                while True:

                    #   Calling the jumbled function
                    virvel = Jumble.Jumble(answer)

                    #   Retrieve the user's word choice
                    choice = await self.bot.wait_for('message', timeout=sec)
                    choice = str(choice.content)

                    #   If the choosen answer is the same as the answer
                    if choice == answer:
                        await ctx.send(f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.Answer} **{answer}**')
                        break

                    # else if  the counter reaches max attempts 
                    elif atNum == limit:
    
                        #   Prepare and send the embed message
                        self.embed.title = 'The Game is over'
                        self.embed.description = f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.GameOver} **{answer}**'
                        await ctx.send(embed=self.embed)

                        # Get out of the loop
                        break

                    #   Else if the choice is not equal to the answer
                    else:
                        atNum += 1
                        word.append(choice)

                        self.embed.title = f'**{atNum}** / **{limit}** | attempted words : **{word}**'
                        self.embed.description = f'{virvel}'
                        await ctx.send(embed=self.embed)

                        #   Continue the loop
                        continue
            
            elif subGenre == 'Villans':
                
                #   Calling the choice function
                answer = Disney.DisneyEasyVillans()
                virvel = Jumble.Jumble(answer)

                #   Creating a list to fetch the query inside, and procsess the request to the database
                ch = []
                query = f'SELECT filmSeries FROM disneyCharactersEasy WHERE characterName = "{answer}"'
                self.cur.execute(query)
                data = self.cur.fetchall()

                for i in data:
                    ch.append(i[0])

                # Creating and prepare a embeded message to the user
                self.embed.title = f'The selected character is from the movie {ch[0]} You have **{sec}** and **{limit}** attempts to resolve the word. '
                self.embed.description = f'{virvel}'


                await ctx.send(embed=self.embed)

                while True:

                    #   Calling the jumbled function
                    virvel = Jumble.Jumble(answer)

                    #   Retrieve the user's word choice
                    choice = await self.bot.wait_for('message', timeout=sec)
                    choice = str(choice.content)

                    #   If the choosen answer is the same as the answer
                    if choice == answer:
                        await ctx.send(f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.Answer} **{answer}**')
                        break

                    # else if  the counter reaches max attempts 
                    elif atNum == limit:
    
                        #   Prepare and send the embed message
                        self.embed.title = 'The Game is over'
                        self.embed.description = f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.GameOver} **{answer}**'
                        await ctx.send(embed=self.embed)

                        # Get out of the loop
                        break

                    #   Else if the choice is not equal to the answer
                    else:
                        atNum += 1
                        word.append(choice)

                        self.embed.title = f'**{atNum}** / **{limit}** | attempted words : **{word}**'
                        self.embed.description = f'{virvel}'
                        await ctx.send(embed=self.embed)

                        #   Continue the loop
                        continue

            elif subGenre == 'Classics':
                
                #   Calling the choice function
                answer = Disney.DisneyEasyClassics()
                virvel = Jumble.Jumble(answer)

                # Creating and prepare a embeded message to the user
                self.embed.title = f'You have **{sec}** and **{limit}** attempts to resolve the word. '
                self.embed.description = f'{virvel}'


                await ctx.send(embed=self.embed)

                while True:

                    #   Calling the jumbled function
                    virvel = Jumble.Jumble(answer)

                    #   Retrieve the user's word choice
                    choice = await self.bot.wait_for('message', timeout=sec)
                    choice = str(choice.content)

                    #   If the choosen answer is the same as the answer
                    if choice == answer:
                        await ctx.send(f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.Answer} **{answer}**')
                        break

                    # else if  the counter reaches max attempts 
                    elif atNum == limit:
    
                        #   Prepare and send the embed message
                        self.embed.title = 'The Game is over'
                        self.embed.description = f'**Results**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n {self.GameOver} **{answer}**'
                        await ctx.send(embed=self.embed)

                        # Get out of the loop
                        break

                    #   Else if the choice is not equal to the answer
                    else:
                        atNum += 1
                        word.append(choice)

                        self.embed.title = f'**{atNum}** / **{limit}** | attempted words : **{word}**'
                        self.embed.description = f'{virvel}'
                        await ctx.send(embed=self.embed)

                        #   Continue the loop
                        continue
