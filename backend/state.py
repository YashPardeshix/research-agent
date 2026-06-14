from typing import TypedDict

class AgentState(TypedDict):
    query: str
    visited_urls: list[str]
    findings: list[str]
    retry_count: int
