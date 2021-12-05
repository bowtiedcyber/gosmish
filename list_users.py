#!/usr/bin/python3

import sqlite3

try:
    sqliteConnection = sqlite3.connect('gosmish.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_query = 'SELECT * FROM victims'
    for row in cursor.execute(sqlite_query):
        print(row)
    cursor.close() 
except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")
