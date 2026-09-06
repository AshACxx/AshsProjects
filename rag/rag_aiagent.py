# =========================================================
# IMPORT MODULES
# =========================================================

# Connects LangChain to Llama running locally through Ollama
from langchain_ollama import ChatOllama

# Converts text into embeddings so we can search by meaning
from langchain_huggingface import HuggingFaceEmbeddings

# Stores and searches document chunks
from langchain_chroma import Chroma

# Allows us to create a retrieval tool for the AI
from langchain_core.tools import tool

# Splits large documents into smaller chunks
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Loads PDF files
from langchain_community.document_loaders import PyPDFLoader

# Creates an AI agent that can use tools
from langgraph.prebuilt import create_react_agent

# Gives the AI conversation memory
from langgraph.checkpoint.memory import MemorySaver


# Ai model that will generate results
llm = ChatOllama(
    model = "llama3.2",
    temperature = 0 
)   

# Specifying what embedding model is used 
# Embedding model converts text into numerical representations.
# This allows us to compare the user's question with parts of the PDF
# and find the most relevant information.
embedding_function = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)


# ---------------------------------------------------------
# LOAD PDF
# ---------------------------------------------------------


def load_file(file_path):
    loader = PyPDFLoader(file_path)
    """
    Loads a PDF and converts each page into a LangChain document.
    """
    documents = loader.load()
    return documents 

def splitter(documents):
    """
    Splits the PDF text into smaller chunks.

    Smaller chunks make it easier to search for
    specific information inside large documents.
    """
    #1000 = characters incl spaces and punctuation
    #overlap makes it so context isnt lost in other chunks 
    txt_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200
        
    )
    
    """
    split.documents is how it actually splits the document, it applies the rules
    of txt_splitter to documents
    """
    chunks = txt_splitter.split_documents(documents)
    return chunks

def database(chunks):
    """
    Stores the document chunks inside Chroma.

    Chroma allows us to search the PDF
    based on meaning instead of exact words.
    """
    database = Chroma.from_documents(
        documents = chunks,
        embedding = embedding_function
    )
    
    return database

def ask_question(question, database):
    results = database.similarity_search(
        question,
        k=4
    )
    
    context = "\n\n".join(
        document.page_content #get the actual text stored inside that document chunk.
        for document in results
    )
    
    prompt = f"""
You are an AI study assistant.

Answer the question using only the information
provided from the uploaded documents.

If the answer cannot be found in the documents,
say that you cannot find enough information.

DOCUMENT INFORMATION:

{context}

QUESTION:

{question}
"""
    # Sending prompt to llm
    response = llm.invoke(prompt)
    
    # Store where the info comes from
    sources = []
    
    # For loop used to get the meta data of the document and returns where the information comes from 
    for document in results:
        source = document.metadata.get(
            'source',
            'Unknown'
        )
        
        # Getting page metadata
        page = document.metadata.get(
            'page',
            0
        )
        
        # Create a readable source
        source_text = f"Page {page + 1}"
        
        # Prevent the same page being shown repeatedly
        if source_text not in sources:
            sources.append(source_text)
    
    return response.content, sources  #content is the ais response in a hidden response 

    