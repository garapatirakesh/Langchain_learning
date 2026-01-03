"""
Advanced Deep Agent - Combining All Concepts

This example demonstrates a complete deep agent that combines:
- Tool calling
- State management and persistence
- Reflection and self-improvement
- Planning and execution
- Human-in-the-loop (optional)
- Error handling and recovery
"""

from typing import TypedDict, Annotated, Literal, Optional
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, ToolMessage
import operator
import json


# ============================================================================
# CONCEPT 1: Comprehensive State
# ============================================================================
class DeepAgentState(TypedDict):
    """Complete state for a deep agent"""
    # User interaction
    task: str
    messages: Annotated[list, operator.add]
    
    # Planning
    plan: list[str]
    current_step: int
    
    # Execution
    step_results: Annotated[list[str], operator.add]
    tool_calls_made: int
    
    # Reflection
    reflection_notes: Annotated[list[str], operator.add]
    quality_score: int  # 1-10
    
    # Control flow
    needs_replanning: bool
    needs_human_approval: bool
    iteration_count: int
    
    # Output
    final_answer: str
    confidence: str  # low, medium, high


# ============================================================================
# CONCEPT 2: Advanced Tools
# ============================================================================
def search_knowledge_base(query: str) -> str:
    """Search a knowledge base for information.
    
    Args:
        query: The search query
    """
    # Simulated knowledge base
    kb = {
        "python": "Python is a high-level programming language known for simplicity.",
        "langgraph": "LangGraph is a framework for building stateful, multi-agent applications.",
        "ai": "Artificial Intelligence is the simulation of human intelligence by machines.",
    }
    
    for key, value in kb.items():
        if key in query.lower():
            return f"Found: {value}"
    
    return "No specific information found in knowledge base."


def calculate_advanced(expression: str) -> str:
    """Perform advanced calculations.
    
    Args:
        expression: Mathematical expression to evaluate
    """
    try:
        result = eval(expression)
        return f"Calculation result: {result}"
    except Exception as e:
        return f"Error in calculation: {str(e)}"


def validate_output(content: str) -> str:
    """Validate output quality.
    
    Args:
        content: Content to validate
    """
    # Simple validation rules
    issues = []
    
    if len(content) < 50:
        issues.append("Content is too short")
    if len(content) > 2000:
        issues.append("Content is too long")
    if not any(char.isdigit() or char.isalpha() for char in content):
        issues.append("Content lacks substance")
    
    if issues:
        return f"Validation issues: {', '.join(issues)}"
    else:
        return "Validation passed: Content quality is good"


tools = [search_knowledge_base, calculate_advanced, validate_output]
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
llm_with_tools = llm.bind_tools(tools)


# ============================================================================
# CONCEPT 3: Planning Node with Deep Analysis
# ============================================================================
def deep_planner(state: DeepAgentState) -> DeepAgentState:
    """Create a detailed plan with analysis"""
    task = state["task"]
    iteration = state.get("iteration_count", 0)
    
    system_msg = """You are an expert planner. Analyze tasks deeply and create detailed plans.
Consider:
1. What information is needed
2. What tools might be useful
3. Potential challenges
4. Quality criteria for success"""
    
    prompt = f"""Analyze and plan for this task:

Task: {task}
Iteration: {iteration + 1}

Create a detailed plan as a JSON array of steps.
Each step should be clear and actionable.

Example: ["Step 1: Research topic X", "Step 2: Analyze findings", "Step 3: Synthesize results"]

Provide ONLY the JSON array:"""
    
    messages = [
        SystemMessage(content=system_msg),
        HumanMessage(content=prompt)
    ]
    
    response = llm.invoke(messages)
    
    # Parse plan
    try:
        content = response.content.strip()
        start_idx = content.find('[')
        end_idx = content.rfind(']') + 1
        json_str = content[start_idx:end_idx]
        plan = json.loads(json_str)
    except:
        plan = ["Analyze the task", "Execute solution", "Validate results"]
    
    print(f"\n{'='*60}")
    print(f"PLAN CREATED (Iteration {iteration + 1})")
    print(f"{'='*60}")
    for i, step in enumerate(plan):
        print(f"{i+1}. {step}")
    print()
    
    return {
        "plan": plan,
        "current_step": 0,
        "iteration_count": iteration + 1
    }


# ============================================================================
# CONCEPT 4: Smart Executor with Tool Use
# ============================================================================
def smart_executor(state: DeepAgentState) -> DeepAgentState:
    """Execute current step, potentially using tools"""
    plan = state["plan"]
    current_step = state["current_step"]
    task = state["task"]
    previous_results = state.get("step_results", [])
    tool_calls = state.get("tool_calls_made", 0)
    
    if current_step >= len(plan):
        return {}
    
    step_description = plan[current_step]
    
    # Build context
    context = f"Original task: {task}\n"
    context += f"Current step ({current_step + 1}/{len(plan)}): {step_description}\n"
    
    if previous_results:
        context += "\nPrevious results:\n"
        for i, result in enumerate(previous_results[-3:]):  # Last 3 results
            context += f"- {result[:100]}...\n"
    
    system_msg = """You are an executor agent. Complete the given step effectively.
Use tools when appropriate. Be thorough and precise."""
    
    messages = [
        SystemMessage(content=system_msg),
        HumanMessage(content=context)
    ]
    
    response = llm_with_tools.invoke(messages)
    
    # Check if tools were called
    result_content = response.content
    new_tool_calls = tool_calls
    
    if hasattr(response, "tool_calls") and response.tool_calls:
        new_tool_calls += len(response.tool_calls)
        print(f"\n🔧 Tools called: {[tc['name'] for tc in response.tool_calls]}")
    
    print(f"\n{'='*60}")
    print(f"STEP {current_step + 1} EXECUTED")
    print(f"{'='*60}")
    print(f"Result: {result_content[:200]}...")
    print()
    
    return {
        "step_results": [result_content],
        "current_step": current_step + 1,
        "tool_calls_made": new_tool_calls,
        "messages": [response]
    }


# ============================================================================
# CONCEPT 5: Reflector with Quality Assessment
# ============================================================================
def reflector(state: DeepAgentState) -> DeepAgentState:
    """Reflect on progress and assess quality"""
    task = state["task"]
    plan = state["plan"]
    results = state.get("step_results", [])
    
    system_msg = """You are a reflection specialist. Analyze the work done so far.
Assess quality, identify issues, and determine if replanning is needed."""
    
    prompt = f"""Reflect on this work:

Task: {task}
Plan: {json.dumps(plan)}
Results so far: {len(results)} steps completed

Latest results:
{chr(10).join(results[-2:]) if results else 'None yet'}

Provide:
1. Quality score (1-10)
2. Key observations
3. Whether replanning is needed (YES/NO)
4. Suggestions for improvement

Format:
SCORE: [1-10]
OBSERVATIONS: [your observations]
REPLAN: [YES/NO]
SUGGESTIONS: [suggestions]"""
    
    messages = [
        SystemMessage(content=system_msg),
        HumanMessage(content=prompt)
    ]
    
    response = llm.invoke(messages)
    reflection = response.content
    
    # Parse reflection
    score = 7  # default
    needs_replan = False
    
    if "SCORE:" in reflection:
        try:
            score_line = [l for l in reflection.split('\n') if 'SCORE:' in l][0]
            score = int(''.join(filter(str.isdigit, score_line)))
        except:
            pass
    
    if "REPLAN:" in reflection:
        needs_replan = "YES" in reflection.upper()
    
    print(f"\n{'='*60}")
    print(f"REFLECTION")
    print(f"{'='*60}")
    print(f"Quality Score: {score}/10")
    print(f"Needs Replanning: {needs_replan}")
    print(f"\n{reflection}\n")
    
    return {
        "reflection_notes": [reflection],
        "quality_score": score,
        "needs_replanning": needs_replan
    }


# ============================================================================
# CONCEPT 6: Synthesizer with Confidence Assessment
# ============================================================================
def synthesizer(state: DeepAgentState) -> DeepAgentState:
    """Synthesize final answer with confidence assessment"""
    task = state["task"]
    results = state.get("step_results", [])
    quality_score = state.get("quality_score", 5)
    
    system_msg = """You are a synthesis expert. Combine all work into a final answer.
Assess your confidence in the answer."""
    
    prompt = f"""Synthesize a final answer:

Task: {task}

All results:
{chr(10).join(results)}

Provide:
1. A comprehensive final answer
2. Your confidence level (low/medium/high)

Format:
ANSWER: [final answer]
CONFIDENCE: [low/medium/high]
REASONING: [why this confidence level]"""
    
    messages = [
        SystemMessage(content=system_msg),
        HumanMessage(content=prompt)
    ]
    
    response = llm.invoke(messages)
    content = response.content
    
    # Parse confidence
    confidence = "medium"
    if "CONFIDENCE:" in content:
        if "high" in content.lower():
            confidence = "high"
        elif "low" in content.lower():
            confidence = "low"
    
    # Extract answer
    if "ANSWER:" in content:
        answer_part = content.split("ANSWER:")[1].split("CONFIDENCE:")[0].strip()
    else:
        answer_part = content
    
    print(f"\n{'='*60}")
    print(f"FINAL SYNTHESIS")
    print(f"{'='*60}")
    print(f"Confidence: {confidence}")
    print(f"\n{answer_part}\n")
    
    return {
        "final_answer": answer_part,
        "confidence": confidence
    }


# ============================================================================
# CONCEPT 7: Routing Logic
# ============================================================================
def route_after_planning(state: DeepAgentState) -> Literal["execute", "end"]:
    """Route after planning"""
    plan = state.get("plan", [])
    return "execute" if plan else "end"


def route_after_execution(state: DeepAgentState) -> Literal["execute", "reflect"]:
    """Route after executing a step"""
    current = state.get("current_step", 0)
    plan = state.get("plan", [])
    
    if current < len(plan):
        return "execute"
    else:
        return "reflect"


def route_after_reflection(state: DeepAgentState) -> Literal["replan", "synthesize"]:
    """Route based on reflection"""
    needs_replan = state.get("needs_replanning", False)
    iteration = state.get("iteration_count", 0)
    quality = state.get("quality_score", 5)
    
    # Replan if needed and haven't iterated too many times
    if needs_replan and iteration < 2 and quality < 7:
        return "replan"
    else:
        return "synthesize"


# ============================================================================
# CONCEPT 8: Building the Deep Agent Graph
# ============================================================================
workflow = StateGraph(DeepAgentState)

# Add all nodes
workflow.add_node("plan", deep_planner)
workflow.add_node("execute", smart_executor)
workflow.add_node("reflect", reflector)
workflow.add_node("synthesize", synthesizer)

# Entry point
workflow.set_entry_point("plan")

# Routing
workflow.add_conditional_edges(
    "plan",
    route_after_planning,
    {"execute": "execute", "end": END}
)

workflow.add_conditional_edges(
    "execute",
    route_after_execution,
    {"execute": "execute", "reflect": "reflect"}
)

workflow.add_conditional_edges(
    "reflect",
    route_after_reflection,
    {"replan": "plan", "synthesize": "synthesize"}
)

workflow.add_edge("synthesize", END)

# Compile with checkpointing
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)


# ============================================================================
# CONCEPT 9: Running the Deep Agent
# ============================================================================
def run_deep_agent(task: str):
    """Run the complete deep agent"""
    print("\n" + "="*60)
    print("DEEP AGENT - ADVANCED EXECUTION")
    print("="*60)
    print(f"\nTask: {task}\n")
    print("="*60)
    
    config = {"configurable": {"thread_id": "deep_agent_session"}}
    
    initial_state = {
        "task": task,
        "messages": [],
        "step_results": [],
        "reflection_notes": [],
        "iteration_count": 0,
        "tool_calls_made": 0,
        "current_step": 0
    }
    
    result = None
    for step in app.stream(initial_state, config):
        node_name = list(step.keys())[0]
        if node_name == "synthesize":
            result = step[node_name]
    
    # Final summary
    print("\n" + "="*60)
    print("EXECUTION SUMMARY")
    print("="*60)
    print(f"Final Answer: {result.get('final_answer', '')[:200]}...")
    print(f"Confidence: {result.get('confidence', 'unknown')}")
    print(f"Quality Score: {result.get('quality_score', 0)}/10")
    print(f"Iterations: {result.get('iteration_count', 0)}")
    print(f"Tool Calls: {result.get('tool_calls_made', 0)}")
    print(f"Steps Completed: {len(result.get('step_results', []))}")
    print("="*60 + "\n")


if __name__ == "__main__":
    # Example 1: Complex analytical task
    run_deep_agent(
        "Explain how LangGraph deep agents work and provide a comparison with traditional chatbots"
    )
    
    # Example 2: Research task
    run_deep_agent(
        "What are the key considerations when building production-ready AI agents?"
    )
