import os
import sqlite3


def initDb():
    connection = sqlite3.connect('./data/database.sqlite')
    with open('./data/schema.sql', 'r') as schema:
        connection.executescript(schema.read())
    connection.commit()
    connection.close()