
#   Python resposories
from os import getenv
from dotenv import load_dotenv


# pylib Responsories
from pylib.systemModule.databasePython import MariaDB

load_dotenv()

class RandomJumbles():
   
    def __init__(self, word):
  
        return

    def weeklyJumbles():

        #   Initializing database connection
        db = MariaDB()
        database = getenv('database2')

        query = f'SELECT title FROM disneyClassicsEasy'
        word = db.selectFromTable(database, query)

        return word
        pass