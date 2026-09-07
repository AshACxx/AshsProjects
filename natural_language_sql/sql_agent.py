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
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql

def check_sql(sql):

    sql_upper = sql.upper().strip()

    dangerous_words = [
        "DELETE",
        "DROP",
        "UPDATE",
        "INSERT",
        "ALTER",
        "CREATE",
        "REPLACE"
    ]

    for word in dangerous_words:

        if word in sql_upper:
            return False

    # Only allow queries that read data
    if not (
        sql_upper.startswith("SELECT")
        or sql_upper.startswith("WITH")
    ):
        return False

    return True


# ---------------------------------------------------------
# RUN SQL QUERY
# ---------------------------------------------------------

def run_query(connection, sql):

    cursor = connection.cursor()

    cursor.execute(sql)

    rows = cursor.fetchall()

    # Get column names
    column_names = []

    if cursor.description:

        for column in cursor.description:
            column_names.append(column[0])

    return column_names, rows

# ---------------------------------------------------------
# EXPLAIN RESULTS
# ---------------------------------------------------------

def explain_results(question, sql, columns, rows):

    # Prevent massive amounts of database data
    # from being sent to the model
    sample_rows = rows[:20]

    prompt = f"""
You are an AI data analyst.

Explain the database result in simple English.

USER QUESTION:
{question}

SQL QUERY:
{sql}

COLUMNS:
{columns}

RESULTS:
{sample_rows}

Give a clear and concise answer to the user's question.
"""

    response = llm.invoke(prompt)

    return response.content


# ---------------------------------------------------------
# MAIN QUESTION FUNCTION
# ---------------------------------------------------------

def ask_database(question, database_path):

    # Connect to database
    connection = connect_database(database_path)

    try:

        # Get database tables + columns
        schema = get_schema(connection)

        # Turn English question into SQL
        sql = generate_sql(
            question,
            schema
        )

        # Make sure AI didn't generate dangerous SQL
        safe = check_sql(sql)

        if not safe:

            return (
                "The generated SQL was blocked for safety.",
                sql,
                [],
                []
            )

        # Run SQL
        columns, rows = run_query(
            connection,
            sql
        )

        # Explain results
        answer = explain_results(
            question,
            sql,
            columns,
            rows
        )

        return (
            answer,
            sql,
            columns,
            rows
        )

    except Exception as error:

        return (
            f"An error occurred: {error}",
            "",
            [],
            []
        )

    finally:

        connection.close()