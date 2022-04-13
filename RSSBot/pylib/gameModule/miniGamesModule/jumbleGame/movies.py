from random import randrange, shuffle, sample, random

from os import getenv
import mariadb

# dotenv reporosory

from dotenv import load_dotenv
load_dotenv()

class Movies():
    

    def familyMovies():
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
        query = f'SELECT movieName FROM movies WHERE genre = "Family" '
        cur.execute(query)
        data = cur.fetchall()

        for i in data:
            subCategory.append(i[0])

        # Randomizing 
        x = randrange(0,6)
        shuffle(subCategory)
        print(subCategory[0])
        # Assigning a variable to the given key
        pick = subCategory[0]
        print(pick)

        #   Closing the accsess to the database
        conn.close()
        return pick

    def ComedyMovies():
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
        query = f'SELECT movieName FROM movies WHERE genre = "Comedy"'
        cur.execute(query)
        data = cur.fetchall()

        for i in data:
            subCategory.append(i[0])

        # Randomizing 
        x = randrange(0,6)
        shuffle(subCategory)
        print(subCategory[0])
        # Assigning a variable to the given key
        pick = subCategory[0]
        print(pick)

        #   Closing the accsess to the database
        conn.close()
        return pick
    
    def ActionMovies():
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
        query = f'SELECT movieName FROM movies WHERE genre = "Action" '
        cur.execute(query)
        data = cur.fetchall()

        for i in data:
            subCategory.append(i[0])

        # Randomizing 
        x = randrange(0,6)
        shuffle(subCategory)
        print(subCategory[0])
        # Assigning a variable to the given key
        pick = subCategory[0]
        print(pick)

        #   Closing the accsess to the database
        conn.close()
        return pick