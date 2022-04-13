
#   Python Repositories
from os import getenv
from random import sample, randint

#   dotenv Repositories
from dotenv import load_dotenv

#   Discord Repositories
from discord.embeds import Embed
from discord.colour import Color
from discord.ext.commands import Cog, command

#   Categories
#from  category.waltdisney import WaltDisney
#from category.randomjumble import RandomJumble

#   pylib resposories
from pylib.systemModule.databasePython import MariaDB
from pylib.dictionaries.gameDictionaries import GameError, GameDictionary, JumbleCategory

load_dotenv()

class JumbleGame(Cog):

    def __init__(self, bot):
        self.bot = bot
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

        ge = GameError()
        rj = RetrieveJumble()
        gd = GameDictionary()
        categories = JumbleCategory()

        #   Configure the jumble Settings

        word = []
        sec = 60.0
        counter = 4

        #   Prepare and send the embeded message
        self.embed.title = 'Jumble Game'
        self.embed.description = f'Welcome to the jumble Game\n You grant {counter} attempts and {sec} sec, please select one of the categories below:\n'

        for category, sub in categories.Titles():
            self.embed.add_field(name = f'{category}', value=f'{sub}',inline=True)

        await ctx.send(embed=self.embed)

        #   Clearing the fields
        self.embed.clear_fields()
        
        #   Handling the retrieved message
        category = await self.bot.wait_for('message', timeout=sec)
        category = str(category.content).capitalize()

        #   random Category
        if category == 'Random':
            pass
            
        #  Walt Disney
        elif category == 'Walt disney':

            #   Prepare and send embed message
            self.embed.title = f'Selected Category : {category}'
            self.embed.description = f' please select one of the sub-category below:\n {categories.SubTitle(category)}'
            await ctx.send(embed=self.embed)
        
            #   Clearing the fields
            self.embed.clear_fields()
        
            #   Assigning message from the user and handle it
            sub = await self.bot.wait_for('message', timeout=sec)
            sub = str(sub.content).lower().replace(" ", "")

            answer = rj.RetrieveDisneyJumble(sub, category)
            answer = str(answer[0])

            virvel = self.GenerateJumble(answer)
            self.embed.title = f'The jumbled Character is seen in \'img\'\n You have **{sec}** sec and **{counter}** attempts to resolve which Character it is '
            self.embed.description = f'{virvel}'
            await ctx.send(embed = self.embed)

        while True:


            #   Retrieve the user's word Option
            option = await self.bot.wait_for('message', timeout=sec)
            option = str(option.content)

            counter -= 1

            virvel = self.GenerateJumble(answer)

            #   checking wheter the answer is equal or not
            if option == answer or counter == 0:

                if option == answer:

                    word.append(option)

                    #   Prepare & send the embed message
                    self.embed.title = f'Game Summary'
                    self.embed.description = f'words tried : **{word}**\nWith attempts : **{counter}** left\n{gd.CorrectAnswer()}'

                elif counter == 0:

                     #   Prepare & send the embed message
                    self.embed.title = 'Game Summary'
                    self.embed.description = f'Words tried : **{word}** \n{gd.GameOver()}\nThe correct answer : **{answer}**'

                await ctx.send(embed=self.embed)

                break

            elif option != answer:

                word.append(option)

                #   Prepare & send the embed message)
                self.embed.title = f'**{counter}** attempts left\nattempted words : **{word}**'
                self.embed.description = f'{virvel}'

            await ctx.send(embed=self.embed)

        return

class RetrieveJumble():
   
    def __init__(self):
        pass
   
    def RetrieveDisneyJumble(self, sub, category):

        """
            Retrieve a Disney movie from the database,
            choose one of the selected values
        """
        category = str(category).lower().replace(" ", "")

        #   Initializing database connection
        db = MariaDB()
        database = getenv('database2')
        query = f'SELECT {sub} FROM {category}'
        print(query)

        word = db.selectFromTable(database, query)

        #   Counting the rows in the database
        x = db.RowCount(database, query)
        x = randint(1, x)

        #   Closing the connection
        db.closeConnection()

        return  word[x]