#!/usr/bin/python3

import sqlite3

try:
    sqliteConnection = sqlite3.connect('gosmish.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    victims = open('victims.csv')
    for i in victims:
        i = i.rstrip()
        i = i.split(',')
        contact_id = i[0]
        first_name = i[1]
        last_name = i[2]
        phone = i[3]
        role = i[4]
        sqlite_insert_query = """CREATE TABLE victims (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	phone TEXT NOT NULL UNIQUE,
        role TEXT NOT NULL
);"""
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Table Created ", cursor.rowcount)
        cursor.close() 
except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")
