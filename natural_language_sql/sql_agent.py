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

# ---------------------------------------------------------
# TURN QUESTION INTO SQL
# ---------------------------------------------------------

def generate_sql(question, schema):

    prompt = f"""
You are an SQL assistant.

Convert the user's question into a SQLite SELECT query.

Only generate SQL that reads data.

Do not use:
DELETE
DROP
UPDATE
INSERT
ALTER
CREATE

DATABASE STRUCTURE:

{schema}

USER QUESTION:

{question}

Return ONLY the SQL query.
Do not explain the query.
Do not use markdown.
"""

    response = llm.invoke(prompt)

    sql = response.content.strip()

    # Sometimes AI may still add markdown
    sql = sql.repace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql