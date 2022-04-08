#    Python Library
from os import getenv
from random import sample

# dotenv Library
from dotenv import load_dotenv

#   Discord Repositories
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command

#   Categories
from categories.waltDisney import WaltDisney
from categories.JumbleDictionaries import JumbleCategory

#   pylib resposories
from pylib.dictionaries.gameDictionaries import GameDictionary
from pyButt.pylib.systemModule.databasePython import MariaDB

load_dotenv()

class JumbleGame(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.Answer = GameDictionary.CorrectAnswer()
        self.modeError = GameDictionary.DifficultyError()
        self.embed = Embed(color=Color.dark_purple(), description='') 

    def GenerateJumble(self, word):

        """         GenerateJumble
                Jumbles the words randomly 
        """

        #   Shuffle the characters of the word
        randomize = sample(word, len(word))
    
        #   Join the elements of the iterator with particular character.
        jumble = ''.join(randomize)

        return jumble

    @command(name='jumble')
    
    async def JumbleGame(self, ctx):

        """                             JumbleGame

            Send a welcome message to the user, ask him to select first a category, then a sub category
            When a user has selected a subCategory, the program sends out a random word from a dictonary and jumble it before send.
            When the user recieves the word, he has 120 seconds on easiest mode to decode it. easy- kimpossible : 60 , 

        """

        #   Initializing the classes
        #   initializing the connection
        db = MariaDB()
        wd = WaltDisney()
        d = GameDictionary()
        categories = JumbleCategory()
        
        #   Configure the jumble Settings
        word = []
        atNum = 0
        limit = 4
        sec = 60.0

        #   Prepare and send the embeded message
        self.embed.title = 'Jumble Game'
        self.embed.description = f'Welcome to the jumble Game\n You grant {limit} attempts and default time limit : {sec} please select one of the sub-categories below:\n'
        for genre, sub in categories.Titles():
            self.embed.add_field(name = f'{genre}', value=f'{sub}',inline=True)

        await ctx.send(embed=self.embed)

        #   Clearing the fields
        self.embed.clear_fields()
        
        #   Handling the retrieved message
        sub = await self.bot.wait_for('message', timeout=sec)
        sub = str(sub.content)
        sub = sub.lower()

        #   Genre : randomCategory
        
        if sub == 'randomCategory':
            pass
            

        elif sub == 'waltdisney':

            genre = categories.SubTitle(sub)


            #   Prepare and send embed message
            self.embed.title = f'Genre : {sub}'
            self.embed.description = f' please select one of the sub-genres below:\n {sub}'

            await ctx.send(embed=self.embed)
        
            #   Clearing the fields
            self.embed.clear_fields()
        
            #   Assigning message from the user and handle it
            sub = await self.bot.wait_for('message', timeout=sec)
            sub = str(sub.content)
            sub = sub.lower()

            if sub == 'characters':

                # Creating and prepare a embeded message to the user

                answer = wd.Characters(sub)

                self.embed.title = f'The jumbled Character is seen in \\ You have **{sec}** and **{limit}** attempts to resolve which Character it is '
                self.embed.description = f'{virvel}'
                await ctx.send(embed=self.embed)
            
        while True:
                    
            #   Calling the jumbled function
            virvel = self.GenerateJumble(answer)

            #   Retrieve the user's word choice
            choice = await self.bot.wait_for('message', timeout=sec)
            choice = str(choice.content)

            #   Initializing variables
            word = []
            atNum = 0
            limit = 4

            #   checking wheter the answer is equal or not
            if choice == answer:

                atNum +=1
                word.append(choice)

                self.embed.title = f'{d.CorrectAnswer()}'
                self.embed.description = f'**Game Summuary**\n words : **{word}** \n Attempts : **{atNum}** of **{limit}** \n'

                await ctx.send(embed=self.embed)

                break
            
            elif choice != answer:
                atNum += 1
                word.append(choice)

                self.embed.title = f'**{atNum}** / **{limit}** | attempted words : **{word}**'
                self.embed.description = f'{virvel}'
                await ctx.send(embed=self.embed)

            elif atNum == limit:

                #   Prepare and send the embed message
                self.embed.title = 'The Game is over'
                self.embed.description = f'**Game Summuary**\nWords tried : **{word}** \nGame Attempts : **4** of **4** \n{d.GameOver()}\nThe correct answer : **{answer}**'
                await ctx.send(embed=self.embed)
        return