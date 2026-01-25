
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import ToolMessage
import os
from dotenv import load_dotenv

load_dotenv()

# --- 1. Define Tools ---
@tool
def read_email_tool(email_id: str) -> str:
    """Mock function to read an email by its ID."""
    print(f"\n[Tool] Reading email {email_id}...")
    return f"Email content for ID: {email_id}"

@tool
def send_email_tool(recipient: str, subject: str, body: str) -> str:
    """Mock function to send an email."""
    print(f"\n[Tool] Sending email to {recipient}...")
    return f"Email sent to {recipient} with subject '{subject}'"

# --- 2. Setup Agent with Interrupts ---
checkpointer = InMemorySaver()
config = {"configurable": {"thread_id": "1"}}

# Ensure API Key
if not os.environ.get("OPENAI_API_KEY"):
    print("Warning: OPENAI_API_KEY not set")

try:
    # First, creating agent WITHOUT interrupt to check graph structure
    agent = create_agent(
        model="gpt-4o",
        tools=[read_email_tool, send_email_tool],
        checkpointer=checkpointer, 
    )
    
    # Check node names
    print(f"Graph Nodes: {agent.get_graph().nodes.keys()}")
    
    # We expect 'tools' or similar. 
    # For selective interruption (only send_email), standard interrupt_before is node-based.
    # To interrupt ONLY on specific tools in the standard prebuilt agent, 
    # you'd technically need to inspect state inside a node or use a custom checkpointer/store logic, 
    # OR simpler: interrupt on 'tools' and then in the UI/Driver, check which tool is about to run.
    
    # Re-compiling with correct interrupt based on typical name 'tools' or 'action'
    # NOTE: create_agent might not expose compile args directly depending on version, 
    # checking if we can pass it during creation or compile.
    # The error showed "return graph.compile(..., interrupt=...)" invoked by create_agent.
    # So passing via create_agent kwargs works.
    
    agent_with_interrupt = create_agent(
        model="gpt-4o",
        tools=[read_email_tool, send_email_tool],
        checkpointer=checkpointer,
        interrupt_before=["tools"], # Standard node name for tools
    )

    print("\n--- Step 1: Initial Invocation ---")
    print("User Request: 'Read my latest email and send a reply...'")
    
    # We use stream to see the steps
    for chunk in agent_with_interrupt.stream(
        {"messages": [{"role": "user", "content": "Read my latest email (id: 123) and send a reply to John with subject 'Hi' saying I'll be there."}]},
        config=config
    ):
        print(f"Chunk: {chunk}")

    print("\n--- Agent Paused (Interrupted) ---")
    print("The agent should have stopped before 'tools' node.")
    
    # Check state to verify next step is the tool call
    state = agent_with_interrupt.get_state(config)
    print(f"Next Action: {state.next}") 
    
    # Inspect which tool is about to be called
    last_message = state.values['messages'][-1]
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        print(f"Pending Tool Calls: {[tc['name'] for tc in last_message.tool_calls]}")
    
    # --- 3. Human Approval Logic ---
    approval = input("\nDo you want to approve execution? (yes/no): ")
    
    if approval.lower() == "yes":
        print("\n--- Step 2: Resuming Execution (Approved) ---")
        # Native LangGraph resume for interrupt_before usually just runs the pending node.
        for chunk in agent_with_interrupt.stream(None, config=config):
             print(f"Resume Chunk: {chunk}")
             
    else:
        print("\n--- Action Rejected ---")
        print("Execution stopped.")

except Exception as e:
    import traceback
    traceback.print_exc()
