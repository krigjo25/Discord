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

    """
        Connecting to preferably database in MariaDB

        >   Creation Date   : 12.01-23
        >   Last update     :

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        Copyright (C) 2023  Kristoffer Gjøsund
    """

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

    def SelectTable (self, table, *column, ):

        #   Initializing a list
        sqlData = []
        query = ""

        #   Select a table from the database

        if bool(column) == False: query = f"SELECT * from {table};"

        elif bool(column) == True:

            for i in column : query += f"{i} "
            query = f"SELECT {query}FROM {table};"

        #  Execute the query.
        try :

            self.cur.execute(query)

        except Exception as e: print(e)
        else:
            #   Fetching the sql selection
            sql = self.cur.fetchall()
            #   Iterating through the sql list
            for i in sql:

                for j in i:
                    if j != None: sqlData.append(j)

        #   Clearing some space
        del sql
        del query
        del column

        #   Returning the values in sqlData
        return sqlData

    def SelectRow(self, table, value, *column):

        #   Initializing a list
        sqlData = []
        query = ""

        #   Select row
        if bool(column) == False: query = f"SELECT * FROM {table} WHERE categories = \"{value}\";"

        #  Execute the query.
        self.cur.execute(query)
        #   Fetching the sql selection
        sql = self.cur.fetchall()

        #   Initializing a list 
        for i in sql:
            for j in i:
                if j != None: sqlData.append(j)

        #   Clearing some space
        del sql
        del query
        del column

        #   Returning the values in sqlData
        return sqlData

    def SelectColumn(self, table, where, value, *column):

        #   Declare arrays
        sqlData = []

        #   Declare variables
        arg = ""

        #   Iterating through the argument

        for i in column : arg += f"{i} "

        query = f"SELECT {arg}FROM {table} WHERE {where} = \"{value}\";"

        #  Execute the query.
        try :

            self.cur.execute(query)

        except Exception as e: print(e)
        else:

            #   Fetching the sql selection
            sql = self.cur.fetchall()

            #   Iterating through the sql list
            for i in sql:

                for j in i:
                    if j != None: sqlData.append(j)

        print(sqlData)
        #   Clearing some space
        del sql, query
        del column, value
        del where
        del arg

        print(sqlData)
        #   Returning the values in sqlData
        return sqlData

    def RowCount(self, query):

        #   Executes the query and retrieve the rows

        self.cur.execute(query)

        #   Fetch the cursor
        self.cur.fetchall()

        #   Counts the rows in the cursor
        return self.cur.rowcount

    def newRecord(self, database, table, *dbcolumn):#   Not working properly

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
