import streamlit as st
import tempfile

from rag import (
    load_pdf,
    split_documents,
    create_database,
    ask_question
)


st.title("AI Study Assistant")

st.write(
    "Upload a PDF and ask questions about it."
)