"""
Human-in-the-Loop Agent

This example demonstrates:
- Pausing execution for human approval
- Interrupt mechanism in LangGraph
- Human feedback integration
- Resuming execution after approval
"""

from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import operator


# ============================================================================
# CONCEPT 1: State with Approval Tracking
# ============================================================================
class HITLState(TypedDict):
    """State for human-in-the-loop agent"""
    task: str
    proposed_action: str
    human_approved: bool
    human_feedback: str
    final_result: str


# ============================================================================
# CONCEPT 2: Proposal Node
# ============================================================================
# Agent proposes an action that needs human approval
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def propose_action_node(state: HITLState) -> HITLState:
    """Agent proposes an action for human review"""
    task = state["task"]
    
    prompt = f"""You are an AI assistant that needs human approval before taking actions.

Task: {task}

Propose a specific action to complete this task. Be clear about what you plan to do.
Format your response as:
ACTION: [what you will do]
REASON: [why this is the right approach]
RISKS: [any potential concerns]"""
    
    response = llm.invoke([HumanMessage(content=prompt)])
    
    return {
        "proposed_action": response.content,
        "human_approved": False
    }


# ============================================================================
# CONCEPT 3: Human Approval Node (Interrupt Point)
# ============================================================================
# This is where we pause for human input
def human_approval_node(state: HITLState) -> HITLState:
    """Wait for human approval - this is an interrupt point"""
    # In a real application, this would pause and wait for human input
    # For demo purposes, we'll simulate it
    
    proposed_action = state["proposed_action"]
    
    print("\n" + "="*60)
    print("HUMAN APPROVAL REQUIRED")
    print("="*60)
    print(f"\nProposed Action:\n{proposed_action}\n")
    print("-"*60)
    
    # Simulate human input (in real app, this would be actual user input)
    approval = input("Approve this action? (yes/no): ").strip().lower()
    
    if approval == "yes":
        feedback = "Approved"
        approved = True
    else:
        feedback = input("Provide feedback for improvement: ").strip()
        approved = False
    
    return {
        "human_approved": approved,
        "human_feedback": feedback
    }


# ============================================================================
# CONCEPT 4: Execution Node
# ============================================================================
def execute_action_node(state: HITLState) -> HITLState:
    """Execute the approved action"""
    task = state["task"]
    proposed_action = state["proposed_action"]
    
    prompt = f"""Execute the following approved action:

Original Task: {task}

Approved Action:
{proposed_action}

Provide the result of executing this action."""
    
    response = llm.invoke([HumanMessage(content=prompt)])
    
    return {
        "final_result": response.content
    }


# ============================================================================
# CONCEPT 5: Revision Node
# ============================================================================
def revise_action_node(state: HITLState) -> HITLState:
    """Revise the action based on human feedback"""
    task = state["task"]
    previous_action = state["proposed_action"]
    feedback = state["human_feedback"]
    
    prompt = f"""Your previous proposal was not approved. Revise it based on feedback.

Original Task: {task}

Previous Proposal:
{previous_action}

Human Feedback:
{feedback}

Provide a revised proposal that addresses the feedback.
Format your response as:
ACTION: [revised action]
REASON: [why this addresses the feedback]
CHANGES: [what you changed from the previous proposal]"""
    
    response = llm.invoke([HumanMessage(content=prompt)])
    
    return {
        "proposed_action": response.content,
        "human_approved": False
    }


# ============================================================================
# CONCEPT 6: Conditional Routing
# ============================================================================
def route_after_approval(state: HITLState) -> Literal["execute", "revise"]:
    """Route based on human approval"""
    if state["human_approved"]:
        return "execute"
    else:
        return "revise"


# ============================================================================
# CONCEPT 7: Building the HITL Graph
# ============================================================================
workflow = StateGraph(HITLState)

# Add nodes
workflow.add_node("propose", propose_action_node)
workflow.add_node("human_review", human_approval_node)
workflow.add_node("execute", execute_action_node)
workflow.add_node("revise", revise_action_node)

# Set entry point
workflow.set_entry_point("propose")

# Add edges
workflow.add_edge("propose", "human_review")

workflow.add_conditional_edges(
    "human_review",
    route_after_approval,
    {
        "execute": "execute",
        "revise": "revise"
    }
)

workflow.add_edge("revise", "human_review")
workflow.add_edge("execute", END)

# Compile with checkpointer for interrupt support
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)


# ============================================================================
# CONCEPT 8: Running with Interrupts
# ============================================================================
def run_hitl_agent(task: str):
    """Run the human-in-the-loop agent"""
    print("\n" + "="*60)
    print("HUMAN-IN-THE-LOOP AGENT")
    print("="*60)
    print(f"\nTask: {task}\n")
    
    thread_id = "hitl_demo"
    config = {"configurable": {"thread_id": thread_id}}
    
    initial_state = {
        "task": task
    }
    
    # Run the agent
    result = None
    for step in app.stream(initial_state, config):
        node_name = list(step.keys())[0]
        node_output = step[node_name]
        
        if node_name == "propose":
            print("\n" + "="*60)
            print("PROPOSAL GENERATED")
            print("="*60)
            print(f"\n{node_output.get('proposed_action', '')}\n")
        
        elif node_name == "revise":
            print("\n" + "="*60)
            print("REVISED PROPOSAL")
            print("="*60)
            print(f"\n{node_output.get('proposed_action', '')}\n")
        
        elif node_name == "execute":
            print("\n" + "="*60)
            print("EXECUTION RESULT")
            print("="*60)
            print(f"\n{node_output.get('final_result', '')}\n")
            result = node_output
    
    print("="*60 + "\n")
    return result


# ============================================================================
# CONCEPT 9: Alternative - Programmatic Approval
# ============================================================================
def run_with_programmatic_approval(task: str, auto_approve: bool = True):
    """Run with programmatic approval (no user input required)"""
    print("\n" + "="*60)
    print("PROGRAMMATIC APPROVAL DEMO")
    print("="*60)
    print(f"\nTask: {task}")
    print(f"Auto-approve: {auto_approve}\n")
    
    # Modified approval node for programmatic use
    def auto_approval_node(state: HITLState) -> HITLState:
        proposed_action = state["proposed_action"]
        print(f"\nProposed Action:\n{proposed_action}\n")
        
        if auto_approve:
            print("✓ Automatically approved\n")
            return {"human_approved": True, "human_feedback": "Approved"}
        else:
            print("✗ Automatically rejected\n")
            return {
                "human_approved": False,
                "human_feedback": "Please provide more detail about the risks"
            }
    
    # Build modified graph
    workflow_auto = StateGraph(HITLState)
    workflow_auto.add_node("propose", propose_action_node)
    workflow_auto.add_node("human_review", auto_approval_node)
    workflow_auto.add_node("execute", execute_action_node)
    workflow_auto.add_node("revise", revise_action_node)
    
    workflow_auto.set_entry_point("propose")
    workflow_auto.add_edge("propose", "human_review")
    workflow_auto.add_conditional_edges(
        "human_review",
        route_after_approval,
        {"execute": "execute", "revise": "revise"}
    )
    workflow_auto.add_edge("revise", "human_review")
    workflow_auto.add_edge("execute", END)
    
    app_auto = workflow_auto.compile()
    
    # Run
    for step in app_auto.stream({"task": task}):
        node_name = list(step.keys())[0]
        if node_name == "execute":
            print("="*60)
            print("FINAL RESULT")
            print("="*60)
            print(f"\n{step[node_name].get('final_result', '')}\n")
    
    print("="*60 + "\n")


if __name__ == "__main__":
    # Example 1: Interactive approval (requires user input)
    # Uncomment to run interactively:
    # run_hitl_agent("Delete all files in the /tmp directory")
    
    # Example 2: Programmatic approval (no user input)
    run_with_programmatic_approval(
        "Send an email to all customers about the new product launch",
        auto_approve=True
    )
    
    # Example 3: Programmatic rejection (triggers revision)
    run_with_programmatic_approval(
        "Deploy the new code to production",
        auto_approve=False
    )
