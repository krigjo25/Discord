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

    '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Connecting to preferably database in MariaDB

            #   SELECT, Counting rows, 
            #   Dropping / Creating databases, Counting rows in a table
            #   Delete records, insert records
    '''

    def __init__(self, database):

        try:

            #   Initializing the database connection
            self.database = database

            self.conn = mariadb.connect(
                                        host = getenv('H0ST'), 
                                        user = getenv('MASTER'), 
                                        port = int(getenv('PORT')), 
                                        password = getenv('PASSWORD'),
                                        database = self.database)

            #   Creating a cursor to execute the statements
            self.cur = self.conn.cursor()

        except mariadb.Error as e:
            print(f"\nError connecting to the database: \n {e}")
            exit(1)

        return

    def closeConnection (self):
        return self.conn.close()

    def Database(self):

        arg = input("Drop / Create database name :")        
        query = f"{arg};"
        self.cur.execute(query)

        return

    def SelectTable (self, table, query = None, column = None):

        #   Select a table from the database
        if query == None and column == None:
            query = f"SELECT * FROM {table};"


        #  Execute the query.
        self.cur.execute(query)

        #   Fetching the sql selection
        sql = self.cur.fetchall()

        #   Initializing a list 
        sqlData = [i for i in sql]
    
        #   Clean up
        del sql

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
        return self.cur.rowcount

    def newRecord(self, database, table, column, column1, clm1, clm2):

        #   Database selection
        self.conn.database = database

        #   Creating a query to be executed
        query = f'INSERT INTO {table} ({column}, {column1}) VALUES (%s, %s)' & (clm1, clm2)

        #   Executes the query 
        self.cur.execute(query)
        self.conn.commit()

        #   Clean up
        del query
        del column
        del column1
        del database
        

        return

    def DelRecord(self, database, table, column, query):

        #   Database selection
        self.conn.database = database

        
        #   Creating a query to be executed
        query = f'DELETE FROM {table} WHERE {column} = {query}'

        #   Executes the query 
        self.cur.execute(query)
        self.conn.commit()

        #   Clean up
        del query
        del table
        del column
        del database

        return
