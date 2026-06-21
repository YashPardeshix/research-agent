from graph import app
import json

initial_state ={"query": "Latest advancements in fusion energy"}
final_state = app.invoke(initial_state)
finished_report=json.dumps(final_state["final_report"], indent=2)
print(finished_report)

