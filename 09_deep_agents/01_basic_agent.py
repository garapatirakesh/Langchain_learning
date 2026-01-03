"""
Basic LangGraph Agent with Tool Calling

This example demonstrates:
- Creating a simple agent with tools
- State management with TypedDict
- Tool binding and execution
- Basic agent loop
"""

from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import operator


# ============================================================================
# CONCEPT 1: State Definition
# ============================================================================
# State holds all information that flows through the agent graph
class AgentState(TypedDict):
    """The state of our agent - this is what gets passed between nodes"""
    messages: Annotated[list, operator.add]  # List of messages in conversation
    

# ============================================================================
# CONCEPT 2: Tool Definition
# ============================================================================
# Tools are functions the agent can call to perform actions
def get_weather(location: str) -> str:
    """Get the current weather for a location.
    
    Args:
        location: The city and state, e.g. 'San Francisco, CA'
    """
    # In a real app, this would call a weather API
    return f"The weather in {location} is sunny and 72°F"


def calculate(expression: str) -> str:
    """Calculate a mathematical expression.
    
    Args:
        expression: A mathematical expression like '2 + 2' or '10 * 5'
    """
    try:
        result = eval(expression)
        return f"The result is: {result}"
    except Exception as e:
        return f"Error calculating: {str(e)}"


# ============================================================================
# CONCEPT 3: LLM with Tool Binding
# ============================================================================
# We bind tools to the LLM so it knows what functions it can call
tools = [get_weather, calculate]
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
llm_with_tools = llm.bind_tools(tools)


# ============================================================================
# CONCEPT 4: Agent Node
# ============================================================================
# The agent node decides what to do next (respond or call a tool)
def agent_node(state: AgentState) -> AgentState:
    """The agent decides whether to call a tool or respond to the user"""
    messages = state["messages"]
    
    # Call the LLM with the conversation history
    response = llm_with_tools.invoke(messages)
    
    # Return the updated state with the new message
    return {"messages": [response]}


# ============================================================================
# CONCEPT 5: Conditional Routing
# ============================================================================
# Decide whether to continue to tools or end the conversation
def should_continue(state: AgentState) -> str:
    """Determine if we should call tools or end"""
    messages = state["messages"]
    last_message = messages[-1]
    
    # If the LLM makes a tool call, route to the tools node
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    
    # Otherwise, end the conversation
    return END


# ============================================================================
# CONCEPT 6: Building the Graph
# ============================================================================
# Create the graph structure
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("agent", agent_node)
workflow.add_node("tools", ToolNode(tools))

# Set entry point
workflow.set_entry_point("agent")

# Add conditional edges
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",  # If tools needed, go to tools node
        END: END  # Otherwise, end
    }
)

# After tools are called, always go back to the agent
workflow.add_edge("tools", "agent")

# Compile the graph
app = workflow.compile()


# ============================================================================
# CONCEPT 7: Running the Agent
# ============================================================================
def run_agent(user_input: str):
    """Run the agent with a user input"""
    print(f"\n{'='*60}")
    print(f"USER: {user_input}")
    print(f"{'='*60}\n")
    
    # Create initial state
    initial_state = {
        "messages": [HumanMessage(content=user_input)]
    }
    
    # Run the graph
    for step in app.stream(initial_state):
        print(f"Step: {list(step.keys())[0]}")
        
        # Print agent responses
        if "agent" in step:
            last_msg = step["agent"]["messages"][-1]
            if hasattr(last_msg, "content") and last_msg.content:
                print(f"AGENT: {last_msg.content}")
            if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:
                for tool_call in last_msg.tool_calls:
                    print(f"  → Calling tool: {tool_call['name']}")
                    print(f"    Args: {tool_call['args']}")
        
        # Print tool results
        if "tools" in step:
            for msg in step["tools"]["messages"]:
                if isinstance(msg, ToolMessage):
                    print(f"TOOL RESULT: {msg.content}")
        
        print()


if __name__ == "__main__":
    # Example 1: Simple question (no tools needed)
    run_agent("Hello! What can you help me with?")
    
    # Example 2: Weather query (uses get_weather tool)
    run_agent("What's the weather like in New York, NY?")
    
    # Example 3: Math calculation (uses calculate tool)
    run_agent("What is 15 * 23 + 100?")
    
    # Example 4: Multiple tool calls
    run_agent("What's the weather in Paris, France and what is 50 divided by 2?")
