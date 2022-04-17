#   Python responsories
from sys import exit
from os import getenv
from datetime import datetime, date

#   Database responsories
import mariadb

#   dotenv Responsories
from dotenv import load_dotenv
load_dotenv()

#   Selecting, Inserting or updates a table
class MariaDB():

    '''         mariaDB

        Connects to the preferably used database from
        mariaDB. with Commands, such as SELECT, INSERT,
        UPDATE, CREATE DATABASE, CREATE TABLE
                
        the function also calls a procedure and a function.
    '''

    def __init__(self):

        try:

            #   Initializing the database connection
            self.conn = mariadb.connect(
                                        host = getenv('H0ST'), 
                                        user = getenv('MASTER'), 
                                        port = int(getenv('PORT')), 
                                        password = getenv('PASSWORD'),
                                        database = getenv('database'))

            #   Creating a cursor to execute the statements
            self.cur = self.conn.cursor()

        except mariadb.Error as e:
            print(f"\nError connecting to the database: \n {e}")
            exit(1)

        return

    def closeConnection (self):

        #   Closing the connection to the database
        self.conn.close()


        return

    def selectFromTable (self, database, query):


        #   Database selection
        self.conn.database = database

        #  Execute the query.
        self.cur.execute(query)


        #   Fetching the sql selection
        sql = self.cur.fetchall()

        #   Initializing a list to return
        sqlData = []
    
        #   append to the list
        for i in sql:
            sqlData.append(i)

        #   Returning the values in sqlData
        return sqlData

    def RowCount(self, database, query):

        #   Database selection
        self.conn.database = database

        #   Executes the query and retrieve the rows
        self.cur.execute(query)

        #   Fetch the cursor
        self.cur.fetchall()

        #   Counts the rows in the cursor
        counter = self.cur.rowcount

        return counter

    def newRecord(self, database, clm1, clm2):

        #   Database selection
        self.conn.database = database

        #   Retrieve values from the .env file
        table = getenv('table1')
        column1 = getenv('column1')
        column2 = getenv('column2')

        #   Creating a query to be executed
        query = f'INSERT INTO {table}({column1}, {column2}) VALUES (%s, %s)' & (clm1, clm2)

        #   Executes the query 
        self.cur.execute(query)
        self.conn.commit()

        return

    def DelRecord(self, database, query):

        #   Database selection
        self.conn.database = database

        #   Retrieve values from the .env file
        table = getenv('table1')
        column1 = getenv('column1')
        
        #   Creating a query to be executed
        query = f'DELETE FROM {table} WHERE {column1} = {query}'

        #   Executes the query 
        self.cur.execute(query)
        self.conn.commit()

        return