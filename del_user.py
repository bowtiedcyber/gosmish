#!/usr/bin/python3
import sys
import sqlite3
try:
    contact_id = sys.argv[1]
except:
    print('enter contact ID as arg 1')
    exit()
try:
    sqliteConnection = sqlite3.connect('gosmish.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    sqlite_query = 'DELETE FROM victims WHERE contact_id IS %s'%(contact_id)
    cursor.execute(sqlite_query)
    sqliteConnection.commit()
    print('done.')
    cursor.close() 
except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")
