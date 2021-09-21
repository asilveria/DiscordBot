#Bot main.py
from sqlite3.dbapi2 import sqlite_version
from typing import final
import discord
import sqlite3
from sqlite3 import Error

def create_connection():
    #creates a db conn that exists in memory

    conn = None

    try:
        conn = sqlite3.connect(':memory:')
        print("sqlite version test: ",sqlite_version)
    except Error as e:
        print(e)
    finally:
        if conn: 
            conn.close

if __name__ == '__main__':
    create_connection()
