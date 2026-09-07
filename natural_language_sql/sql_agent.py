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