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
    RecursiveCharacterTextSplitter(
        chunks = 1000,
        chunk_overlap = 200
        
    )