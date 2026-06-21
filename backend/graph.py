from langgraph.graph import StateGraph, START, END
from state import AgentState
from nodes import search_node, fetch_node, synthesis_node

workflow = StateGraph(AgentState)
workflow.add_node("search", search_node)
workflow.add_node("fetch", fetch_node)
workflow.add_node("synthesis", synthesis_node)
workflow.add_edge(START, "search")
workflow.add_edge("search", "fetch")
workflow.add_edge("fetch", "synthesis")
workflow.add_edge("synthesis", END)

app = workflow.compile()