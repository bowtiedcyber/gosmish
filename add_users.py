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
        sqlite_insert_query = """INSERT INTO victims
                              (contact_id, first_name, last_name, phone, role) 
                               VALUES 
                              (%s,'%s','%s','%s','%s')"""%(contact_id, first_name, last_name, phone, role)
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close() 
except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")
