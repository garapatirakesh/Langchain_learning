"""
Planning Agent - Think Before Acting

This example demonstrates:
- Plan-and-execute pattern
- Breaking down complex tasks into steps
- Sequential execution of planned steps
- Progress tracking
"""

from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import operator
import json


# ============================================================================
# CONCEPT 1: Planning State
# ============================================================================
class PlanningState(TypedDict):
    """State for planning agent"""
    task: str  # Original task
    plan: list[str]  # List of steps to execute
    current_step: int  # Which step we're on
    step_results: Annotated[list[str], operator.add]  # Results of each step
    final_answer: str  # Final combined result


# ============================================================================
# CONCEPT 2: Planner Node
# ============================================================================
# This node creates a plan by breaking down the task
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def planner_node(state: PlanningState) -> PlanningState:
    """Create a step-by-step plan for the task"""
    task = state["task"]
    
    prompt = f"""You are a planning expert. Break down the following task into clear, sequential steps.

Task: {task}

Provide a numbered list of steps needed to complete this task. Each step should be:
- Specific and actionable
- In logical order
- Clear about what needs to be done

Return ONLY a JSON array of steps, like this:
["Step 1 description", "Step 2 description", "Step 3 description"]

JSON array:"""
    
    response = llm.invoke([HumanMessage(content=prompt)])
    
    # Parse the plan
    try:
        # Extract JSON from response
        content = response.content.strip()
        # Find JSON array in the response
        start_idx = content.find('[')
        end_idx = content.rfind(']') + 1
        json_str = content[start_idx:end_idx]
        plan = json.loads(json_str)
    except:
        # Fallback: split by newlines
        plan = [line.strip() for line in response.content.split('\n') 
                if line.strip() and not line.strip().startswith('#')]
    
    return {
        "plan": plan,
        "current_step": 0
    }


# ============================================================================
# CONCEPT 3: Executor Node
# ============================================================================
# This node executes one step of the plan
def executor_node(state: PlanningState) -> PlanningState:
    """Execute the current step of the plan"""
    plan = state["plan"]
    current_step = state["current_step"]
    task = state["task"]
    previous_results = state.get("step_results", [])
    
    if current_step >= len(plan):
        return {}
    
    step_description = plan[current_step]
    
    # Build context from previous steps
    context = ""
    if previous_results:
        context = "\n\nPrevious steps completed:\n"
        for i, result in enumerate(previous_results):
            context += f"{i+1}. {plan[i]}\n   Result: {result}\n"
    
    prompt = f"""You are executing a plan to complete a task.

Original Task: {task}

Current Step ({current_step + 1}/{len(plan)}): {step_description}
{context}

Execute this step and provide the result. Be specific and detailed."""
    
    response = llm.invoke([HumanMessage(content=prompt)])
    
    return {
        "step_results": [response.content],
        "current_step": current_step + 1
    }


# ============================================================================
# CONCEPT 4: Synthesizer Node
# ============================================================================
# This node combines all step results into a final answer
def synthesizer_node(state: PlanningState) -> PlanningState:
    """Synthesize all step results into a final answer"""
    task = state["task"]
    plan = state["plan"]
    step_results = state["step_results"]
    
    # Build a summary of all steps
    steps_summary = ""
    for i, (step, result) in enumerate(zip(plan, step_results)):
        steps_summary += f"\nStep {i+1}: {step}\nResult: {result}\n"
    
    prompt = f"""You are synthesizing the results of a multi-step plan.

Original Task: {task}

Steps Executed and Results:
{steps_summary}

Provide a comprehensive final answer that combines all the step results 
to fully address the original task."""
    
    response = llm.invoke([HumanMessage(content=prompt)])
    
    return {
        "final_answer": response.content
    }


# ============================================================================
# CONCEPT 5: Conditional Routing
# ============================================================================
def should_continue(state: PlanningState) -> Literal["execute", "synthesize"]:
    """Decide whether to execute next step or synthesize results"""
    current_step = state["current_step"]
    plan = state["plan"]
    
    if current_step < len(plan):
        return "execute"
    else:
        return "synthesize"


# ============================================================================
# CONCEPT 6: Building the Planning Graph
# ============================================================================
workflow = StateGraph(PlanningState)

# Add nodes
workflow.add_node("planner", planner_node)
workflow.add_node("executor", executor_node)
workflow.add_node("synthesizer", synthesizer_node)

# Set entry point
workflow.set_entry_point("planner")

# Add edges
workflow.add_conditional_edges(
    "planner",
    should_continue,
    {
        "execute": "executor",
        "synthesize": "synthesizer"
    }
)

workflow.add_conditional_edges(
    "executor",
    should_continue,
    {
        "execute": "executor",
        "synthesize": "synthesizer"
    }
)

workflow.add_edge("synthesizer", END)

# Compile
app = workflow.compile()


# ============================================================================
# CONCEPT 7: Running the Planning Agent
# ============================================================================
def run_planning_agent(task: str):
    """Run the planning agent on a task"""
    print("\n" + "="*60)
    print("PLANNING AGENT")
    print("="*60)
    print(f"\nTask: {task}\n")
    
    initial_state = {
        "task": task,
        "step_results": []
    }
    
    for step in app.stream(initial_state):
        node_name = list(step.keys())[0]
        node_output = step[node_name]
        
        if node_name == "planner":
            print("\n" + "="*60)
            print("PLAN CREATED")
            print("="*60)
            plan = node_output.get("plan", [])
            for i, step_desc in enumerate(plan):
                print(f"{i+1}. {step_desc}")
            print()
        
        elif node_name == "executor":
            current = node_output.get("current_step", 0)
            results = node_output.get("step_results", [])
            if results:
                print(f"\n{'='*60}")
                print(f"STEP {current} EXECUTED")
                print(f"{'='*60}")
                print(f"Result: {results[-1]}\n")
        
        elif node_name == "synthesizer":
            print("\n" + "="*60)
            print("FINAL ANSWER")
            print("="*60)
            print(f"\n{node_output.get('final_answer', '')}\n")
    
    print("="*60 + "\n")


if __name__ == "__main__":
    # Example 1: Research task
    run_planning_agent(
        "Explain how to make a simple web application with Python"
    )
    
    # Example 2: Analysis task
    run_planning_agent(
        "Compare the pros and cons of using SQL vs NoSQL databases"
    )
    
    # Example 3: Problem-solving task
    run_planning_agent(
        "How would you design a system to handle 1 million concurrent users?"
    )
