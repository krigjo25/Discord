# System reporosory
from os import getenv
from random import randrange, shuffle, sample, random

# Database reporosory
import mariadb

# dotenv reporosory
from dotenv import load_dotenv
load_dotenv()

# Creating a function to choose a random word
class Disney():
   
    def __init__(self, word):
     '''   self.conn = mariadb.connect(
                    user = os.getenv('USER'),
                    password = os.getenv('PASSWORD'),
                    host = os.getenv('HOST'),
                    db = os.getenv('DATABASE')
        )
        self.cur = self.conn.cursor()
        return'''

    # Family movies   
    def DisneyEasyClassics():
        

        # Connecting to the database

        conn = mariadb.connect(
                    user = os.getenv('USER'),
                    password = os.getenv('PASSWORD'),
                    host = os.getenv('HOST'),
                    db = os.getenv('DATABASE')
        )
        cur = conn.cursor()

        # Creating a dictonary for the queries
        subCategory = []

        # Selecting character name from the database, and procsessing it
        query = f'SELECT filmSeries FROM disneyMoviesSeriesEasy'
        cur.execute(query)
        data = cur.fetchall()

        for i in data:
            subCategory.append(i[0])

        # Randomizing 
        x = randrange(0,11)
        shuffle(subCategory)

        # Assigning a variable to the given key
        pick = subCategory[x]

        #   Closing the accsess to the database
        conn.close()

        return  pick

    #   Retrieve Disney Princesses
    def DisneyEasyPrincesses():
        
        # Connecting to the database

        conn = mariadb.connect(
                    user = os.getenv('USER'),
                    password = os.getenv('PASSWORD'),
                    host = os.getenv('HOST'),
                    db = os.getenv('DATABASE')
        )
        cur = conn.cursor()

        # Creating a dictonary for the queries
        subCategory = []

        # Selecting character name from the database, and procsessing it
        query = f'SELECT characterName FROM disneyCharactersEasy WHERE characterRole = "Princess"'
        cur.execute(query)
        data = cur.fetchall()

        for i in data:
            subCategory.append(i[0])

        # Randomizing 
        x = randrange(0,11)
        shuffle(subCategory)

        # Assigning a variable to the given key
        pick = subCategory[x]

        #   Closing the accsess to the database
        conn.close()

        return  pick

    #   Retrieve Disney Heros
    def DisneyEasyHeros():
        
        # Connecting to the database

        conn = mariadb.connect(
                    user = os.getenv('USER'),
                    password = os.getenv('PASSWORD'),
                    host = os.getenv('HOST'),
                    db = os.getenv('DATABASE')
        )
        cur = conn.cursor()

        # Creating a dictonary for the queries
        subCategory = []
 
        # Selecting character name from the database, and procsessing it
        query = f'SELECT characterName FROM disneyCharactersEasy WHERE characterRole = "Hero"'
        cur.execute(query)
        data = cur.fetchall()

        for i in data:
            subCategory.append(i[0])

        # Randomizing 
        x = randrange(0,8)
        shuffle(subCategory)
        print(subCategory, 'Heros')
        # Assigning a variable to the given key
        pick = subCategory[x]

        #   Closing the accsess to the database
        conn.close()

        return  pick

    #   Retrieve Disney Villians
    def DisneyEasyVillians():
        
        # Connecting to the database

        conn = mariadb.connect(
                    user = os.getenv('USER'),
                    password = os.getenv('PASSWORD'),
                    host = os.getenv('HOST'),
                    db = os.getenv('DATABASE')
        )
        cur = conn.cursor()

        # Creating a dictonary for the queries
        subCategory = []

        # Selecting character name from the database, and procsessing it
        query = f'SELECT characterName FROM disneyCharactersEasy WHERE characterRole = "Villian"'
        cur.execute(query)
        data = cur.fetchall()

        for i in data:
            subCategory.append(i[0])

        # Randomizing 
        x = randrange(0,6)
        shuffle(subCategory)

        # Assigning a variable to the given key
        pick = subCategory[x]

        #   Closing the accsess to the database
        conn.close()

        return  pick