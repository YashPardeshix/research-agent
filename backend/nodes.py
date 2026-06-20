from state import AgentState
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


def synthesis_node(state:AgentState) -> AgentState:
    combined_context = "\n\n".join(state["findings"])
    prompt = f"""
You are an expert researcher. Read the following raw research findings and write a structured executive report.

Raw Research Findings:
{combined_context}

{
"title": the title of the query,
"summary": the summary of the query,
"findings": the findings of the query,
"sources": the urls/sources of the query,
"confidence_level": Low/Medium/High
}
"""