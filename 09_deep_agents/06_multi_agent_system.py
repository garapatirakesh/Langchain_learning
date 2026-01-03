"""
Multi-Agent System - Collaborative Agents

This example demonstrates:
- Multiple specialized agents working together
- Agent handoffs and collaboration
- Supervisor pattern for coordination
- Specialized roles and responsibilities
"""

from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import operator


# ============================================================================
# CONCEPT 1: Shared State for Multi-Agent System
# ============================================================================
class MultiAgentState(TypedDict):
    """Shared state across all agents"""
    task: str
    current_agent: str
    researcher_output: str
    writer_output: str
    reviewer_output: str
    final_output: str
    iteration: int


# ============================================================================
# CONCEPT 2: Specialized Agent Definitions
# ============================================================================
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)


# Researcher Agent - Gathers information
def researcher_agent(state: MultiAgentState) -> MultiAgentState:
    """Research agent gathers information and facts"""
    task = state["task"]
    
    system_msg = """You are a research specialist. Your job is to:
1. Identify key topics and questions
2. Gather relevant information
3. Organize findings clearly
4. Provide factual, well-researched content"""
    
    prompt = f"""Research the following topic and provide comprehensive information:

Topic: {task}

Provide:
- Key facts and information
- Important concepts
- Relevant examples
- Sources or references (can be general)"""
    
    messages = [
        SystemMessage(content=system_msg),
        HumanMessage(content=prompt)
    ]
    
    response = llm.invoke(messages)
    
    print("\n" + "="*60)
    print("RESEARCHER AGENT")
    print("="*60)
    print(f"\n{response.content}\n")
    
    return {
        "researcher_output": response.content,
        "current_agent": "researcher"
    }


# Writer Agent - Creates content
def writer_agent(state: MultiAgentState) -> MultiAgentState:
    """Writer agent creates polished content"""
    task = state["task"]
    research = state.get("researcher_output", "")
    
    system_msg = """You are a professional writer. Your job is to:
1. Transform research into engaging content
2. Structure information clearly
3. Use appropriate tone and style
4. Make content accessible and interesting"""
    
    prompt = f"""Create well-written content based on this research:

Topic: {task}

Research Findings:
{research}

Write a clear, engaging piece that covers the topic comprehensively."""
    
    messages = [
        SystemMessage(content=system_msg),
        HumanMessage(content=prompt)
    ]
    
    response = llm.invoke(messages)
    
    print("\n" + "="*60)
    print("WRITER AGENT")
    print("="*60)
    print(f"\n{response.content}\n")
    
    return {
        "writer_output": response.content,
        "current_agent": "writer"
    }


# Reviewer Agent - Quality control
def reviewer_agent(state: MultiAgentState) -> MultiAgentState:
    """Reviewer agent checks quality and provides feedback"""
    task = state["task"]
    content = state.get("writer_output", "")
    iteration = state.get("iteration", 0)
    
    system_msg = """You are a quality reviewer. Your job is to:
1. Check accuracy and completeness
2. Verify clarity and structure
3. Identify areas for improvement
4. Approve or request revisions"""
    
    prompt = f"""Review the following content:

Original Topic: {task}

Content to Review:
{content}

Provide:
1. Overall assessment (Good/Needs Improvement)
2. Strengths
3. Areas for improvement
4. Recommendation (APPROVE or REVISE)"""
    
    messages = [
        SystemMessage(content=system_msg),
        HumanMessage(content=prompt)
    ]
    
    response = llm.invoke(messages)
    
    print("\n" + "="*60)
    print("REVIEWER AGENT")
    print("="*60)
    print(f"\n{response.content}\n")
    
    return {
        "reviewer_output": response.content,
        "current_agent": "reviewer",
        "iteration": iteration + 1
    }


# Supervisor Agent - Coordinates the workflow
def supervisor_agent(state: MultiAgentState) -> MultiAgentState:
    """Supervisor coordinates the multi-agent workflow"""
    current = state.get("current_agent", "")
    
    print("\n" + "="*60)
    print("SUPERVISOR: Coordinating workflow...")
    print(f"Last agent: {current}")
    print("="*60 + "\n")
    
    return {}


# ============================================================================
# CONCEPT 3: Routing Logic
# ============================================================================
def route_from_supervisor(state: MultiAgentState) -> Literal["researcher", "writer", "reviewer", "end"]:
    """Supervisor decides which agent to call next"""
    current = state.get("current_agent", "")
    
    if not current:
        # Start with researcher
        return "researcher"
    elif current == "researcher":
        # After research, go to writer
        return "writer"
    elif current == "writer":
        # After writing, go to reviewer
        return "reviewer"
    else:
        # After review, end
        return "end"


def route_from_reviewer(state: MultiAgentState) -> Literal["writer", "finalize"]:
    """Route based on reviewer's decision"""
    review = state.get("reviewer_output", "")
    iteration = state.get("iteration", 0)
    
    # Max 2 iterations
    if iteration >= 2:
        return "finalize"
    
    # Check if approved
    if "APPROVE" in review.upper():
        return "finalize"
    else:
        return "writer"


# Finalizer Node
def finalizer_node(state: MultiAgentState) -> MultiAgentState:
    """Finalize the output"""
    content = state.get("writer_output", "")
    
    print("\n" + "="*60)
    print("FINALIZING OUTPUT")
    print("="*60 + "\n")
    
    return {
        "final_output": content
    }


# ============================================================================
# CONCEPT 4: Building the Multi-Agent Graph
# ============================================================================
workflow = StateGraph(MultiAgentState)

# Add all agents as nodes
workflow.add_node("supervisor", supervisor_agent)
workflow.add_node("researcher", researcher_agent)
workflow.add_node("writer", writer_agent)
workflow.add_node("reviewer", reviewer_agent)
workflow.add_node("finalize", finalizer_node)

# Set entry point
workflow.set_entry_point("supervisor")

# Supervisor routes to different agents
workflow.add_conditional_edges(
    "supervisor",
    route_from_supervisor,
    {
        "researcher": "researcher",
        "writer": "writer",
        "reviewer": "reviewer",
        "end": "finalize"
    }
)

# Each agent returns to supervisor
workflow.add_edge("researcher", "supervisor")
workflow.add_edge("writer", "supervisor")

# Reviewer can send back to writer or finalize
workflow.add_conditional_edges(
    "reviewer",
    route_from_reviewer,
    {
        "writer": "writer",
        "finalize": "finalize"
    }
)

workflow.add_edge("finalize", END)

# Compile
app = workflow.compile()


# ============================================================================
# CONCEPT 5: Running the Multi-Agent System
# ============================================================================
def run_multi_agent_system(task: str):
    """Run the multi-agent system"""
    print("\n" + "="*60)
    print("MULTI-AGENT SYSTEM")
    print("="*60)
    print(f"\nTask: {task}\n")
    print("="*60)
    
    initial_state = {
        "task": task,
        "iteration": 0
    }
    
    result = None
    for step in app.stream(initial_state):
        node_name = list(step.keys())[0]
        node_output = step[node_name]
        
        if node_name == "finalize":
            result = node_output
    
    print("\n" + "="*60)
    print("FINAL OUTPUT")
    print("="*60)
    print(f"\n{result.get('final_output', '')}\n")
    print("="*60)
    print(f"Total iterations: {result.get('iteration', 0)}")
    print("="*60 + "\n")


# ============================================================================
# CONCEPT 6: Alternative Pattern - Parallel Agents
# ============================================================================
def parallel_agents_example():
    """Example of agents working in parallel"""
    
    class ParallelState(TypedDict):
        task: str
        agent1_result: str
        agent2_result: str
        combined_result: str
    
    def agent1(state: ParallelState) -> ParallelState:
        """First parallel agent"""
        task = state["task"]
        prompt = f"Analyze the technical aspects of: {task}"
        response = llm.invoke([HumanMessage(content=prompt)])
        print(f"\nAgent 1 (Technical): {response.content}\n")
        return {"agent1_result": response.content}
    
    def agent2(state: ParallelState) -> ParallelState:
        """Second parallel agent"""
        task = state["task"]
        prompt = f"Analyze the business aspects of: {task}"
        response = llm.invoke([HumanMessage(content=prompt)])
        print(f"\nAgent 2 (Business): {response.content}\n")
        return {"agent2_result": response.content}
    
    def combiner(state: ParallelState) -> ParallelState:
        """Combine results from parallel agents"""
        result1 = state["agent1_result"]
        result2 = state["agent2_result"]
        
        prompt = f"""Combine these two analyses:

Technical Analysis:
{result1}

Business Analysis:
{result2}

Provide a unified perspective."""
        
        response = llm.invoke([HumanMessage(content=prompt)])
        return {"combined_result": response.content}
    
    # Build parallel graph
    parallel_workflow = StateGraph(ParallelState)
    parallel_workflow.add_node("agent1", agent1)
    parallel_workflow.add_node("agent2", agent2)
    parallel_workflow.add_node("combiner", combiner)
    
    parallel_workflow.set_entry_point("agent1")
    parallel_workflow.add_edge("agent1", "agent2")
    parallel_workflow.add_edge("agent2", "combiner")
    parallel_workflow.add_edge("combiner", END)
    
    parallel_app = parallel_workflow.compile()
    
    print("\n" + "="*60)
    print("PARALLEL AGENTS EXAMPLE")
    print("="*60 + "\n")
    
    result = parallel_app.invoke({
        "task": "Implementing AI in customer service"
    })
    
    print("\n" + "="*60)
    print("COMBINED RESULT")
    print("="*60)
    print(f"\n{result['combined_result']}\n")
    print("="*60 + "\n")


if __name__ == "__main__":
    # Example 1: Sequential multi-agent system
    run_multi_agent_system(
        "Explain the benefits of using LangGraph for building AI agents"
    )
    
    # Example 2: Parallel agents
    parallel_agents_example()
