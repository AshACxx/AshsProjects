import streamlit as st
import tempfile

from rag_aiagent import (
    load_file,
    splitter,
    database,
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



    # Load the PDF
    documents = load_file(temp_path)
    # Split into chunks
    chunks = splitter(documents)
    # Create Chroma database
    database = database(chunks)


    st.success("PDF processed successfully.")

    # Let the user ask a question
    question = st.text_input(
        "Ask a question about the PDF:"
    )


    if question:

        answer, sources = ask_question(
            question,
            database
        )


        st.subheader("Answer")

        st.write(answer)


        st.subheader("Sources")


        for source in sources:

            st.write(
                f"File: {source['source']}"
            )

            st.write(
                f"Page: {source['page']}"
            )