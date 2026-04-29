from langchain.chat_models import init_chat_model
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
import os 

#initialize search tool
#set env key

os.environ['TAVILY_API_KEY'] = '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'

search_tool = TavilySearchResults(max_results = 2)

query = "What is the weather in Dublin"

search_result= search_tool.invoke(query)
print(search_result)


model = init_chat_model('gpt-4o-mini', model_provider='openai')
tools = [search_tool]
memory = MemorySaver()