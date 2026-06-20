from state import AgentState
from tools import search, fetch
import json
import os
from openai import OpenAI

os.getenv("NVIDIA_API_KEY")

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY") 
)

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

{{
"title": "the title of the query",
"summary": "the summary of the query",
"findings": "the findings of the query",
"sources": "the urls/sources of the query",
"confidence_level": "Low/Medium/High"
}}
"""
    completion = client.chat.completions.create(
        model="deepseek-ai/deepseek-v4-flash",
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
        stream=False
    )
    raw_output = completion.choices[0].message.content
    parsed_report = json.loads(raw_output)
    return {"final_report": parsed_report}

