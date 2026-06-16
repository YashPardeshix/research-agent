from state import AgentState
from langgraph.graph import StateGraph, END
from tools import search, fetch

def search_node(state: AgentState) -> AgentState:
    urls = search(state["query"])
    return {"urls_to_read": urls}

def fetch_node(state:AgentState) -> AgentState:
    local_findings = []
    for url in state["urls_to_read"]:
        content = fetch(url)
        if "Error" not in content:     
            local_findings.append(content)
    return {"findings": local_findings}


 