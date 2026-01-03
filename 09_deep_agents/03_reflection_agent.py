"""
Reflection Agent - Self-Improving Agent

This example demonstrates:
- Reflection pattern (generate → critique → improve)
- Self-evaluation and improvement
- Iterative refinement
- Quality control through reflection
"""

from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import operator


# ============================================================================
# CONCEPT 1: Reflection State
# ============================================================================
class ReflectionState(TypedDict):
    """State for reflection agent"""
    task: str  # The original task
    draft: str  # Current draft/attempt
    reflection: str  # Critique of the draft
    iterations: int  # Number of reflection cycles
    final_output: str  # Final approved output


# ============================================================================
# CONCEPT 2: Generator Node
# ============================================================================
# This node generates content based on the task
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)


def generate_node(state: ReflectionState) -> ReflectionState:
    """Generate initial draft or improved version"""
    task = state["task"]
    reflection = state.get("reflection", "")
    iterations = state.get("iterations", 0)
    
    if iterations == 0:
        # First generation
        prompt = f"""Generate a response to the following task:

Task: {task}

Provide a clear, well-structured response."""
    else:
        # Improvement based on reflection
        previous_draft = state.get("draft", "")
        prompt = f"""Improve the following draft based on the reflection:

Original Task: {task}

Previous Draft:
{previous_draft}

Reflection/Critique:
{reflection}

Generate an improved version that addresses the critique."""
    
    response = llm.invoke([HumanMessage(content=prompt)])
    
    return {
        "draft": response.content,
        "iterations": iterations + 1
    }


# ============================================================================
# CONCEPT 3: Reflection Node
# ============================================================================
# This node critiques the generated content
def reflect_node(state: ReflectionState) -> ReflectionState:
    """Reflect on and critique the current draft"""
    task = state["task"]
    draft = state["draft"]
    
    prompt = f"""You are a critical reviewer. Evaluate the following response:

Original Task: {task}

Response to Evaluate:
{draft}

Provide a constructive critique covering:
1. Accuracy and correctness
2. Completeness (does it fully address the task?)
3. Clarity and structure
4. Areas for improvement

If the response is excellent and needs no improvement, say "APPROVED".
Otherwise, provide specific suggestions for improvement."""
    
    response = llm.invoke([HumanMessage(content=prompt)])
    
    return {
        "reflection": response.content
    }


# ============================================================================
# CONCEPT 4: Conditional Routing Based on Reflection
# ============================================================================
def should_continue(state: ReflectionState) -> Literal["reflect", "generate", "end"]:
    """Decide whether to continue reflecting or finish"""
    iterations = state.get("iterations", 0)
    reflection = state.get("reflection", "")
    
    # Maximum 3 iterations to prevent infinite loops
    if iterations >= 3:
        return "end"
    
    # If approved, we're done
    if "APPROVED" in reflection.upper():
        return "end"
    
    # If we just generated, go to reflection
    if iterations > 0 and not reflection:
        return "reflect"
    
    # If we just reflected, generate improvement
    if reflection and "APPROVED" not in reflection.upper():
        return "generate"
    
    return "reflect"


# ============================================================================
# CONCEPT 5: Finalize Node
# ============================================================================
def finalize_node(state: ReflectionState) -> ReflectionState:
    """Finalize the output"""
    return {
        "final_output": state["draft"]
    }


# ============================================================================
# CONCEPT 6: Building the Reflection Graph
# ============================================================================
workflow = StateGraph(ReflectionState)

# Add nodes
workflow.add_node("generate", generate_node)
workflow.add_node("reflect", reflect_node)
workflow.add_node("finalize", finalize_node)

# Set entry point
workflow.set_entry_point("generate")

# Add conditional edges
workflow.add_conditional_edges(
    "generate",
    should_continue,
    {
        "reflect": "reflect",
        "end": "finalize"
    }
)

workflow.add_conditional_edges(
    "reflect",
    should_continue,
    {
        "generate": "generate",
        "end": "finalize"
    }
)

workflow.add_edge("finalize", END)

# Compile
app = workflow.compile()


# ============================================================================
# CONCEPT 7: Running the Reflection Agent
# ============================================================================
def run_reflection_agent(task: str):
    """Run the reflection agent on a task"""
    print("\n" + "="*60)
    print("REFLECTION AGENT")
    print("="*60)
    print(f"\nTask: {task}\n")
    print("-"*60)
    
    initial_state = {
        "task": task,
        "iterations": 0
    }
    
    iteration_num = 0
    for step in app.stream(initial_state):
        node_name = list(step.keys())[0]
        node_output = step[node_name]
        
        if node_name == "generate":
            iteration_num += 1
            print(f"\n{'='*60}")
            print(f"ITERATION {iteration_num}: GENERATION")
            print(f"{'='*60}")
            print(f"\nDraft:\n{node_output.get('draft', '')}\n")
        
        elif node_name == "reflect":
            print(f"\n{'='*60}")
            print(f"ITERATION {iteration_num}: REFLECTION")
            print(f"{'='*60}")
            print(f"\nCritique:\n{node_output.get('reflection', '')}\n")
        
        elif node_name == "finalize":
            print(f"\n{'='*60}")
            print(f"FINAL OUTPUT")
            print(f"{'='*60}")
            print(f"\n{node_output.get('final_output', '')}\n")
            print(f"\nTotal iterations: {iteration_num}")
    
    print("="*60 + "\n")


if __name__ == "__main__":
    # Example 1: Writing task
    run_reflection_agent(
        "Write a brief explanation of what machine learning is for a 10-year-old."
    )
    
    # Example 2: Technical task
    run_reflection_agent(
        "Explain the difference between a list and a tuple in Python."
    )
    
    # Example 3: Creative task
    run_reflection_agent(
        "Write a haiku about artificial intelligence."
    )
