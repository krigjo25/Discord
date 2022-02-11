# System reporosory
from os import getenv
from random import randrange, shuffle

# Database reporosory
import mariadb

# dotenv reporosory
from dotenv import load_dotenv
load_dotenv()

class MarvelComics():
    def ComicsEasy():
        

        # Connecting to the database

        conn = mariadb.connect(
            port = 55368,
            user = getenv('USER'),
            host = getenv('HOST'),
            db = getenv('DATABASE'),
            password = getenv('PASSWORD')
        )
        cur = conn.cursor()

        # Creating a dictonary for the queries
        subCategory = []

        # Selecting character name from the database, and procsessing it
        query = f'SELECT films FROM MarvelComics'
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

    #   Retrieve Heros
    def ComicsHero():
        

        # Connecting to the database

        conn = mariadb.connect(
            port = 55368,
            user = getenv('USER'),
            host = getenv('HOST'),
            db = getenv('DATABASE'),
            password = getenv('PASSWORD')
        )
        cur = conn.cursor()

        # Creating a dictonary for the queries
        subCategory = []

        # Selecting character name from the database, and procsessing it
        query = f'SELECT character FROM MarvelComics WHERE characterRole = "Hero"'
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

    #   Retrieve Villians
    def ComicsVillians():
        

        # Connecting to the database

        conn = mariadb.connect(
            port = 55368,
            user = getenv('USER'),
            host = getenv('HOST'),
            db = getenv('DATABASE'),
            password = getenv('PASSWORD')
        )
        cur = conn.cursor()

        # Creating a dictonary for the queries
        subCategory = []

        # Selecting character name from the database, and procsessing it
        query = f'SELECT character FROM MarvelComics WHERE characterRole = "Villians"'
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