# 🔍 Single-Agent Research System (DeepSeek-R1 + LangGraph)

A production-grade, state-governed single-agent research assistant built in Python using **LangGraph** and the **NVIDIA NIM API (DeepSeek-R1/v4)**. The agent takes any search query, dynamically crawls the web, handles scraping failures gracefully, sanitizes raw web contexts, and synthesizes a structured executive research report.

---

## 🛠️ Core Engineering Patterns Demonstrated

* **State-Driven Synthesis:** Rather than running unstructured AI prompts, the data flow is strictly state-governed. A sequential pipeline runs: `search` (URLs extraction) ➡️ `fetch` (raw HTML scraper) ➡️ `synthesis` (deep-reasoning summary). The LLM acts as the final aggregator, compiling the structured state.
* **State Segregation:** We isolate raw, high-volume operational data (HTML scraps) from the final generated executive report (`final_report: dict`) inside our LangGraph state, ensuring data purity and preventing state pollution.
* **Graceful Failure Handling:** Intercepts scraping and network failures at the node level by filtering out network warnings and corrupted pages before they contaminate the LLM’s context window.
* **Execution Context Isolation:** Guarantees multi-user safety by using local list accumulators inside function nodes, completely eliminating memory leaks and cross-user data exposure.

---

## 📐 System Architecture

```text
    [START]
       │
       ▼
 ┌───────────┐
 │  search   │  ◄── Uses Tavily API to gather target sources
 └─────┬─────┘
       │
       ▼
 ┌───────────┐
 │   fetch   │  ◄── Scrapes raw HTML & sanitizes out failure states
 └─────┬─────┘
       │
       ▼
 ┌───────────┐
 │ synthesis │  ◄── Feeds clean contexts to DeepSeek via NVIDIA NIM
 └─────┬─────┘
       │
       ▼
     [END] (Outputs Structured executive JSON)

📂 Project Structure

yashpardeshix-research-agent/
└── backend/
    ├── state.py         # Type definitions for the encapsulated AgentState
    ├── tools.py         # Search & fetch integrations (Tavily, Requests)
    ├── nodes.py         # Business logic for graph nodes (Isolated, Secure)
    ├── graph.py         # LangGraph workflow orchestration & compilation
    └── main.py          # Execution entrypoint (Prettified JSON output)

⚙️ Installation & Setup

1. Clone the Repository

git clone https://github.com/yashpardeshix/yashpardeshix-research-agent.git
cd yashpardeshix-research-agent/backend

2. Set Up Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Configure Environment Variables

Create a .env file in the backend/ directory:

TAVILY_API_KEY="your_tavily_api_key"
NVIDIA_API_KEY="your_nvidia_nim_api_key"

4. Run the Agent

python main.py

📊 Sample Output Schema

When running the agent, the final compiled output is a beautifully formatted,
strict JSON payload:

{
  "title": "Latest Breakthroughs in Nuclear Fusion Energy",
  "summary": "Recent experiments have achieved net energy gain milestones...",
  "findings": [
    "Achieved Q-factor greater than 1.5 in magnetic confinement tests.",
    "Advanced superconducting magnets reduced heat dissipation requirements by 30%."
  ],
  "sources": [
    "https://example-fusion-source.org/news",
    "https://nature-fusion-breakthroughs.com"
  ],
  "confidence_level": "High"
}





