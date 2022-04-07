# System reporosory
from os import getenv
from random import randrange, shuffle

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
            port = int(getenv('PORT')),
            user = getenv('USER'),
            host = getenv('HOST'),
            db = getenv('DATABASE'),
            password = getenv('PASSWORD')
        )

        cur = conn.cursor()

        # Creating a dictonary for the queries
        subCategory = []

        # Selecting character name from the database, and procsessing it
        query = f'SELECT title FROM disneyClassicsEasy'
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
            port = int(getenv('PORT')),
            user = getenv('USER'),
            host = getenv('HOST'),
            db = getenv('DATABASE'),
            password = getenv('PASSWORD')
        )

        cur = conn.cursor()

        # Creating a dictonary for the queries
        subCategory = []

        # Selecting character name from the database, and procsessing it
        query = f'SELECT characterName FROM disneyCharactersEasy WHERE role = "Princess"'
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
            port = int(getenv('PORT')),
            user = getenv('USER'),
            host = getenv('HOST'),
            db = getenv('DATABASE'),
            password = getenv('PASSWORD')
        )

        cur = conn.cursor()

        # Creating a dictonary for the queries
        subCategory = []
 
        # Selecting character name from the database, and procsessing it
        query = f'SELECT characterName FROM disneyCharactersEasy WHERE role = "Hero"'
        cur.execute(query)
        data = cur.fetchall()

        for i in data:
            subCategory.append(i[0])

        # Randomizing 
        x = randrange(0,7)
        shuffle(subCategory)

        # Assigning a variable to the given key
        pick = subCategory[x]

        #   Closing the accsess to the database
        conn.close()

        return  pick

    #   Retrieve Disney Villians
    def DisneyEasyVillians():
        
        # Connecting to the database

        conn = mariadb.connect(
            port = int(getenv('PORT')),
            user = getenv('USER'),
            host = getenv('HOST'),
            db = getenv('DATABASE'),
            password = getenv('PASSWORD')
        )

        cur = conn.cursor()

        # Creating a dictonary for the queries
        subCategory = []

        # Selecting character name from the database, and procsessing it
        query = f'SELECT characterName FROM disneyCharactersEasy WHERE role = "Villian"'
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