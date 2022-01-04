# System reporosory
from os import getenv
from random import randrange, shuffle, sample, random

# Database reporosory
import mariadb

# dotenv reporosory
from dotenv import load_dotenv
load_dotenv()

class DCComics():
    #   Retrieve Classic movies
    def ComicsEasy():
        

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
        query = f'SELECT films FROM dcComics'
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
                    user = os.getenv('USER'),
                    password = os.getenv('PASSWORD'),
                    host = os.getenv('HOST'),
                    db = os.getenv('DATABASE')
        )
        cur = conn.cursor()

        # Creating a dictonary for the queries
        subCategory = []

        # Selecting character name from the database, and procsessing it
        query = f'SELECT character FROM dcComics WHERE characterRole = "Hero"'
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
                    user = os.getenv('USER'),
                    password = os.getenv('PASSWORD'),
                    host = os.getenv('HOST'),
                    db = os.getenv('DATABASE')
        )
        cur = conn.cursor()

        # Creating a dictonary for the queries
        subCategory = []

        # Selecting character name from the database, and procsessing it
        query = f'SELECT character FROM dcComics WHERE characterRole = "Villians"'
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