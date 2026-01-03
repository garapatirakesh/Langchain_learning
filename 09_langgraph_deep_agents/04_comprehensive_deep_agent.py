import os
import tempfile
from dotenv import load_dotenv

from deepagents.graph import create_deep_agent
from deepagents.middleware.fs import FileSystemMiddleware
from deepagents.middleware.subagents import SubAgentMiddleware
# Note: In a production setting, you'd use a real checkpointer for cross-session memory
from langgraph.checkpoint.memory import MemorySaver

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

load_dotenv()

# --- 1. Tools ---
@tool
def final_validator(content: str) -> str:
    """Useful to perform a final check on the quality of a report."""
    return f"Validated! The report is professional and complete. Length: {len(content)} characters."

# --- 2. Subagent Setup ---
# Specialist agent for coding
@tool
def get_python_snippet(task: str) -> str:
    """Generates a python snippet for a task."""
    return f"```python\ndef {task.replace(' ', '_')}():\n    print('Hello World')\n```"

coder_subagent = create_deep_agent(
    llm=ChatOpenAI(model="gpt-4o-mini", temperature=0),
    tools=[get_python_snippet]
)

# --- 3. Manager Setup with Multiple Capabilities ---
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

with tempfile.TemporaryDirectory() as workspace:
    print(f"📁 Workspace: {workspace}")
    
    # Capability 1: File Storage
    fs = FileSystemMiddleware(root_dir=workspace)
    
    # Capability 2: Delegation
    sub_mgr = SubAgentMiddleware(subagents={"coding_expert": coder_subagent})
    
    # Multi-turn memory
    checkpointer = MemorySaver()

    # Create the Comprehensive Deep Agent
    agent = create_deep_agent(
        llm=llm,
        tools=[final_validator],
        middleware=[fs, sub_mgr],
        checkpoint=checkpointer
    )

    # --- 4. Running the comprehensive task ---
    def run_complex_task():
        print("\n🚀 Task: Multidisciplinary project with file management.")
        
        config = {"configurable": {"thread_id": "project_123"}}
        
        # Phase 1: Research and Delegation
        task1 = "Delegate the task of creating a 'hello world' function to the coding expert. Save the code into 'script.py'."
        agent.invoke({"task": task1}, config=config)
        
        # Phase 2: Refinement (Testing persistent memory)
        print("\n🔄 Phase 2: Testing memory persistence...")
        task2 = "Read 'script.py', add a comment to it, and then run the final validator tool on the whole content."
        result = agent.invoke({"task": task2}, config=config)
        
        print("\n--- FINAL AGENT SUMMARY ---")
        print(result.get("response"))

if __name__ == "__main__":
    run_complex_task()
