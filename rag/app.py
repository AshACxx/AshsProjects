import streamlit as st
import tempfile

from rag_aiagent import (
    load_pdf,
    split_documents,
    create_database,
    ask_question
)


st.title("AI Study Assistant")

st.write(
    "Upload a PDF and ask questions about it."
)

# Let the user upload a PDF
uploaded_file = st.file_uploader(
    "Upload a PDF",
    type="pdf"
)


if uploaded_file is not None:

    # Streamlit gives us the uploaded file in memory.
    # PyPDFLoader needs an actual file path,
    # so we temporarily save the PDF.

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(
            uploaded_file.getvalue()
        )

        temp_path = temp_file.name