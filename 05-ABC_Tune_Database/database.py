import sqlite3
import pandas as pd

def my_sql_database():
    ''' 
    old code 
    conn = sqlite3.connect("tunes2.db")

    cursor = conn.cursor()

    cursor.execute("DELETE TABLE IF EXISTS tunes2")
    conn.commit()
    conn.close()
    '''
    #improvement recc by ai 
    conn = sqlite3.connect("tunes2.db")

    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS tunes2")
    conn.commit()
    conn.close()




def inserting(book_number,tunes):
    conn = sqlite3.connect("tunes2.db")
    cursor = conn.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS tunes2 (id INTEGER PRIMARY KEY AUTOINCREMENT, book_number INTEGER, title TEXT, key TEXT, type TEXT, body TEXT)')

    for tune in tunes: #1 is used to insert the data into a table
        #cursor lets u run sql commands
        cursor.execute('INSERT INTO tunes2(book_number,title,key,type,body) VALUES (?,?,?,?,?)',(book_number,tune.get("title", ""),tune.get("key", ""),tune.get("type", ""),tune.get("body", "")))
    conn.commit()
    conn.close()

def ctdb():
    conn = sqlite3.connect('tunes2.db')
    return conn

def load_tunes_from_database():
    #variable conn holds the function ctdb
    conn = ctdb()
    #selecting all columns from tunes
    query = "SELECT * FROM tunes2"
    #creating a data from 
    df = pd.read_sql(query, conn)
    conn.close()

    return df
