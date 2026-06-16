from state import AgentState
from langgraph.graph import StateGraph, END
from tools import search, fetch

def search_node(state: AgentState) -> AgentState:
    urls = search(state["query"])
    return {"urls_to_read": urls}

def fetch_node(state:AgentState) -> AgentState:
    for url in state["urls_to_read"]:
        content = fetch(url)
    return {"findings": content}

 