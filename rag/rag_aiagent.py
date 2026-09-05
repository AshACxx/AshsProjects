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

llm = ChatOllama(
    model = "llama3.2",
    temperature = 0 
)   

embedding_function = HuggingFaceEmbeddings