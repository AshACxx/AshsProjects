import streamlit as st
import pandas as pd
from pathlib import Path

from sql_agent import ask_database


# ---------------------------------------------------------
# PAGE
# ---------------------------------------------------------

st.title("AI Database Analyst")

st.write(
    "Ask questions about the database using normal English."
)


# ---------------------------------------------------------
# DATABASE LOCATION
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

database_path = BASE_DIR / "data" / "northwind.db"


# ---------------------------------------------------------
# QUESTION
# ---------------------------------------------------------

question = st.text_input(
    "Ask a question about the database:"
)


if question:

    with st.spinner("Analysing database..."):

        answer, sql, columns, rows = ask_database(
            question,
            str(database_path)
        )


    # ---------------------------------------------------------
    # ANSWER
    # ---------------------------------------------------------

    st.subheader("Answer")

    st.write(answer)


    # ---------------------------------------------------------
    # RESULTS
    # ---------------------------------------------------------

    if rows:

        st.subheader("Results")

        dataframe = pd.DataFrame(
            rows,
            columns=columns
        )

        st.dataframe(dataframe)


    # ---------------------------------------------------------
    # SHOW SQL
    # ---------------------------------------------------------

    if sql:

        st.subheader("Generated SQL")

        st.code(
            sql,
            language="sql"
        )