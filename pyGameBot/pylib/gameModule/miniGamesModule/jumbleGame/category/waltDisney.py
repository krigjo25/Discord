
#   Python Repositories
from os import getenv
from random import randint, randrange, shuffle

# dotenv Repositories
from dotenv import load_dotenv

#   pylib Repositories
from pylib.systemModule.databasePython import MariaDB

load_dotenv()

# Creating a function to choose a random word
class WaltDisney():
   
    def __init__(self, word):
        return
   
    def Classics(self):
        """
            Retrieve a Disney movie from the database,
            choose one of the selected values
        """

        #   Initializing database connection
        db = MariaDB()
        database = getenv('database1')
        table = getenv('table')
        column = getenv('column')
        query = f'SELECT {table} FROM {table}'
        word = db.selectFromTable(database, query)

        #   Counting the rows in the database
        x = db.RowCount(database, query)
        x -=1
        x = randint(0,x)

        #   Closing the connection
        db.closeConnection()

        return  word[x]

    def Characters(self):

        """
            Retrieve a character name from the database,
            choose one of the selected values
        """

        # Selecting character name from the database, and procsessing it
        
        #   Initializing database connection
        db = MariaDB()
        database = getenv('database1')
        table = getenv('table')
        column = getenv('column')
        query = f'SELECT * characterName FROM disneyCharactersEasy;'
        word = db.selectFromTable(database, query)

        #   Counting the rows in the database
        x = db.RowCount(database, query)
        x -=1
        x = randint(0,x)

        #   Closing the connection
        db.closeConnection()

        return  word[x]
