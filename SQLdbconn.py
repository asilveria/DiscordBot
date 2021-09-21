
from sqlite3.dbapi2 import sqlite_version
import discord
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :args: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def functionCallTest():
    print("Test Test Test")

def tableCreate():
    
    database = "quotesqlite.db"
    sql_create_quotes_table = """ CREATE TABLE IF NOT EXISTS quotes (
                                        id integer PRIMARY KEY,
                                        author text NOT NULL,
                                        submit_date text,
                                        quote_text text
                                    ); """
    # create a database connection

    conn = create_connection(database)

    if conn is not None:
    # create quotes table
        create_table(conn, sql_create_quotes_table)

    else:
        print("Error! cannot create the database connection.")

tableCreate()