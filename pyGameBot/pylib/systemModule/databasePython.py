#   Python responsories
import sys
import os

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
            #   Delete, Select records, 
    '''

    def __init__(self, database):

        self.database = database

        try:

            #   Initializing the database connection
            self.conn = mariadb.connect(
                                        host = os.getenv('H0ST'), 
                                        user = os.getenv('MASTER'), 
                                        port = int(os.getenv('PORT')), 
                                        password = os.getenv('PASSWORD'),
                                        database = self.database)

            #   Creating a cursor to execute the statements
            self.cur = self.conn.cursor()

        except mariadb.Error as e:
            print(f"\nError connecting to the database:\n{e}")
            sys.exit(1)

        else: print("Connection success")
        return

    def closeConnection (self):
        return self.conn.close()

    def Database(self, arg, db):
 
        query = f"{str(arg).upper()} DATABASE {db};"

        return self.cur.execute(query)

    def SelectTable (self, table, column = None):

        #   Select a table from the database
        if  column == None: query = f"SELECT * FROM {table};"

        else:

            for i in column: query += f"{i},"
            query = f"SELECT {query} FROM {table};"

        #  Execute the query.
        self.cur.execute(query)

        #   Fetching the sql selection
        sql = self.cur.fetchall()

        #   Initializing a list 
        sqlData = [i for i in sql]
    
        #   Clearing some space
        del sql
        del query
        del column

        #   Returning the values in sqlData
        return sqlData

    def RowCount(self, query):

        #   Executes the query and retrieve the rows
        self.cur.execute(query)

        #   Fetch the cursor
        self.cur.fetchall()

        #   Counts the rows in the cursor
        return self.cur.rowcount

    #   Not working properly
    def newRecord(self, database, table, *dbcolumn):

        #   Initializing variables
        column = ""
        values = ""
        #   Database selection
        self.conn.database = database

        #   How to know if its a column or value?
        for i in dbcolumn: column +=f"{i},"

        #   Creating a query to be executed
        query = f'INSERT INTO {table} ({column}) VALUES ({values})'

        #   Executes the query 
        self.cur.execute(query)
        self.conn.commit()

        #   Clear some space
        del i

        del query
        del column
        del database
        del dbcolumn
        del dbvalues
        

        return

    def DelRecord(self, *query):

        
        #   Creating a query to be executed
        query = f'DELETE FROM {query[0]} WHERE {query[1]} = {query[3]};'

        #   Executes the query 
        self.cur.execute(query)
        self.conn.commit()

        #   Clean up
        del query

        return

if __name__ == "__main__":
    db = MariaDB(os.getenv("db2"))
    db.closeConnection()