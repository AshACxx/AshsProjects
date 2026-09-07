import sqlite3

from langchain_ollama import ChatOllama


# ---------------------------------------------------------
# AI MODEL
# ---------------------------------------------------------

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# ---------------------------------------------------------
# CONNECT TO DATABASE
# ---------------------------------------------------------

def connect_database(database_path):

    connection = sqlite3.connect(database_path)

    return connection

# ---------------------------------------------------------
# GET DATABASE STRUCTURE
# ---------------------------------------------------------

def get_schema(connection):

    cursor = connection.cursor()

    # Get all table names
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table';"
    )

    tables = cursor.fetchall()

    schema = ""

    # Go through every table
    for table in tables:

        table_name = table[0]

        # Get information about the columns
        cursor.execute(
            f"PRAGMA table_info('{table_name}')"
        )

        columns = cursor.fetchall()

        schema += f"\nTable: {table_name}\n"

        for column in columns:

            column_name = column[1]
            column_type = column[2]

            schema += f"- {column_name} ({column_type})\n"

    return schema