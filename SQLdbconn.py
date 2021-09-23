
from sqlite3.dbapi2 import sqlite_version
import discord
import random
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

def insertHelper(conn, author, sub_date, quote_text):
     quote = (author,sub_date,quote_text)
     insertQuote(conn, quote)

def insertQuote(conn, quote):
    
    sql = ''' INSERT INTO quotes (author, submit_date, quote_text)
                VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, quote)
    conn.commit()

    return cur.lastrowid

def removeQuote(conn,id):

    sql = '''DELETE FROM quotes WHERE id=?'''
    cur = conn.cursor()
    cur.execute(sql,(id,))
    conn.commit()

def returnQuoteBody(conn):
    
    #'''GO SELECT TOP 1 * FROM quotes ORDER BY NEWID() GO'''
    quoteDeets = []
    cursor = conn.execute('''SELECT * FROM quotes''')
    record = cursor.fetchall()
    for row in record:
        quoteDeets.append(row[0])
        quoteDeets.append(row[1])
        quoteDeets.append(row[2])
        quoteDeets.append(row[3])
    
    cursor.close()
    return quoteDeets
   
def fireUp():

    database = "quotesqlite.db"
    sql_create_quotes_table = """ CREATE TABLE IF NOT EXISTS quotes (
                                        id integer PRIMARY KEY,
                                        author text NOT NULL,
                                        submit_date text,
                                        quote_text text
                                    ); """
    # create a database connection

    conn = create_connection(database)
    return conn
