# System reporosory
from os import getenv
from random import randrange, shuffle

# Database reporosory
import mariadb

# dotenv reporosory
from dotenv import load_dotenv

#   pylib Resposory
from pylib.systemModule.databasePython import MariaDB

load_dotenv()

# Creating a function to choose a random word
class Disney():
   
    def __init__(self, word):
        return

    # Family movies   
    def DisneyEasyClassics():
        
        #   Initializing database connection
        db = MariaDB()
        database = getenv('database1')
        table = getenv('table')
        column = getenv('column')

        query = f'SELECT {table} FROM {table}'
        word = db.selectFromTable(database, query)

        #   Closing the connection
        db.closeConnection()

        return  word

    #   Retrieve Disney Princesses
    def DisneyEasyPrincesses():

        # Selecting character name from the database, and procsessing it
        
        #   Initializing database connection
        db = MariaDB()
        database = getenv('database1')
        table = getenv('table')
        column = getenv('column')

        query = f'SELECT characterName FROM disneyCharactersEasy WHERE role = "Princess"'

        word = db.selectFromTable(database, query)

        #   Closing the connection
        db.closeConnection()

        return  word

    #   Retrieve Disney Heros
    def DisneyEasyHeros():
        
        #   Initializing database connection
        db = MariaDB()
        database = getenv('database1')
        table = getenv('table')
        column = getenv('column')

        query = f'SELECT characterName FROM disneyCharactersEasy WHERE role = "Heros"'

        word = db.selectFromTable(database, query)

        #   Closing the connection
        db.closeConnection()

        return  word


    #   Retrieve Disney Villians
    def DisneyEasyVillians():
        
        #   Initializing database connection
        db = MariaDB()
        database = getenv('database1')
        table = getenv('table')
        column = getenv('column')

        query = f'SELECT characterName FROM disneyCharactersEasy WHERE role = "Villians"'

        word = db.selectFromTable(database, query)

        #   Closing the connection
        db.closeConnection()

        return  word
