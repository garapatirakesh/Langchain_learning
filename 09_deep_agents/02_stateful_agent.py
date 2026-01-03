"""
Stateful Agent with Memory and Checkpointing

This example demonstrates:
- Persistent state across multiple interactions
- Memory/checkpointing for conversation history
- Rich state with multiple fields
- State updates and accumulation
"""

from typing import TypedDict, Annotated, Sequence
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
import operator


# ============================================================================
# CONCEPT 1: Rich State Definition
# ============================================================================
# A more complex state that tracks multiple pieces of information
class ConversationState(TypedDict):
    """Enhanced state with multiple fields"""
    messages: Annotated[Sequence[BaseMessage], operator.add]  # Conversation history
    user_name: str  # User's name (if provided)
    conversation_count: int  # Number of exchanges
    topics_discussed: Annotated[list[str], operator.add]  # Topics covered


# ============================================================================
# CONCEPT 2: Stateful Agent Node
# ============================================================================
# This agent maintains context across multiple turns
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)


def conversational_agent(state: ConversationState) -> ConversationState:
    """Agent that maintains conversation context"""
    messages = state["messages"]
    user_name = state.get("user_name", "")
    count = state.get("conversation_count", 0)
    
    # Build a system message with context
    system_context = "You are a helpful assistant."
    if user_name:
        system_context += f" You are talking to {user_name}."
    system_context += f" This is exchange #{count + 1} in the conversation."
    
    # Prepend system message
    full_messages = [HumanMessage(content=system_context)] + list(messages)
    
    # Get response
    response = llm.invoke(full_messages)
    
    # Extract topics from the conversation (simple keyword extraction)
    last_user_msg = messages[-1].content if messages else ""
    topics = extract_topics(last_user_msg)
    
    return {
        "messages": [response],
        "conversation_count": count + 1,
        "topics_discussed": topics
    }


def extract_topics(text: str) -> list[str]:
    """Simple topic extraction (in real app, use NLP)"""
    keywords = ["weather", "math", "science", "history", "sports", "food", "travel"]
    found_topics = [kw for kw in keywords if kw.lower() in text.lower()]
    return found_topics if found_topics else ["general"]


# ============================================================================
# CONCEPT 3: Name Extraction Node
# ============================================================================
# A specialized node to extract and remember the user's name
def extract_name_node(state: ConversationState) -> ConversationState:
    """Extract user name if mentioned"""
    messages = state["messages"]
    current_name = state.get("user_name", "")
    
    # If we already have a name, skip
    if current_name:
        return {}
    
    # Check the last user message for name introduction
    if messages:
        last_msg = messages[-1].content.lower()
        
        # Simple name extraction (in real app, use NER)
        if "my name is" in last_msg:
            parts = last_msg.split("my name is")
            if len(parts) > 1:
                name = parts[1].strip().split()[0].capitalize()
                return {"user_name": name}
        
        if "i'm" in last_msg or "i am" in last_msg:
            for phrase in ["i'm ", "i am "]:
                if phrase in last_msg:
                    parts = last_msg.split(phrase)
                    if len(parts) > 1:
                        name = parts[1].strip().split()[0].capitalize()
                        return {"user_name": name}
    
    return {}


# ============================================================================
# CONCEPT 4: Building the Stateful Graph
# ============================================================================
workflow = StateGraph(ConversationState)

# Add nodes
workflow.add_node("extract_name", extract_name_node)
workflow.add_node("agent", conversational_agent)

# Set entry point
workflow.set_entry_point("extract_name")

# Add edges
workflow.add_edge("extract_name", "agent")
workflow.add_edge("agent", END)

# ============================================================================
# CONCEPT 5: Checkpointing for Persistence
# ============================================================================
# MemorySaver allows the agent to remember across multiple invocations
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)


# ============================================================================
# CONCEPT 6: Running with Thread ID
# ============================================================================
def run_conversation():
    """Run a multi-turn conversation with persistent state"""
    
    # Thread ID identifies a unique conversation session
    thread_id = "conversation_123"
    config = {"configurable": {"thread_id": thread_id}}
    
    print("\n" + "="*60)
    print("STATEFUL CONVERSATION DEMO")
    print("="*60 + "\n")
    
    # Turn 1
    print("Turn 1:")
    print("-" * 40)
    result = app.invoke(
        {
            "messages": [HumanMessage(content="Hi! My name is Alice.")],
            "conversation_count": 0,
            "topics_discussed": []
        },
        config=config
    )
    print(f"USER: Hi! My name is Alice.")
    print(f"AGENT: {result['messages'][-1].content}")
    print(f"State - Name: {result.get('user_name', 'Unknown')}")
    print(f"State - Count: {result['conversation_count']}")
    print()
    
    # Turn 2 - The agent remembers Alice's name!
    print("Turn 2:")
    print("-" * 40)
    result = app.invoke(
        {"messages": [HumanMessage(content="What's the weather like today?")]},
        config=config
    )
    print(f"USER: What's the weather like today?")
    print(f"AGENT: {result['messages'][-1].content}")
    print(f"State - Name: {result.get('user_name', 'Unknown')}")
    print(f"State - Count: {result['conversation_count']}")
    print(f"State - Topics: {result.get('topics_discussed', [])}")
    print()
    
    # Turn 3 - Context is maintained
    print("Turn 3:")
    print("-" * 40)
    result = app.invoke(
        {"messages": [HumanMessage(content="Can you help me with some math?")]},
        config=config
    )
    print(f"USER: Can you help me with some math?")
    print(f"AGENT: {result['messages'][-1].content}")
    print(f"State - Name: {result.get('user_name', 'Unknown')}")
    print(f"State - Count: {result['conversation_count']}")
    print(f"State - Topics: {result.get('topics_discussed', [])}")
    print()
    
    # Turn 4 - Agent remembers everything
    print("Turn 4:")
    print("-" * 40)
    result = app.invoke(
        {"messages": [HumanMessage(content="What have we talked about so far?")]},
        config=config
    )
    print(f"USER: What have we talked about so far?")
    print(f"AGENT: {result['messages'][-1].content}")
    print(f"State - Name: {result.get('user_name', 'Unknown')}")
    print(f"State - Count: {result['conversation_count']}")
    print(f"State - Topics: {result.get('topics_discussed', [])}")
    print()
    
    print("="*60)
    print("CONVERSATION COMPLETE")
    print(f"Total exchanges: {result['conversation_count']}")
    print(f"User: {result.get('user_name', 'Unknown')}")
    print(f"Topics: {', '.join(set(result.get('topics_discussed', [])))}")
    print("="*60)


# ============================================================================
# CONCEPT 7: Inspecting Checkpoints
# ============================================================================
def inspect_checkpoints():
    """Show how to inspect saved checkpoints"""
    thread_id = "conversation_123"
    config = {"configurable": {"thread_id": thread_id}}
    
    print("\n" + "="*60)
    print("CHECKPOINT INSPECTION")
    print("="*60 + "\n")
    
    # Get the current state
    state = app.get_state(config)
    
    print(f"Current State:")
    print(f"  - Messages: {len(state.values.get('messages', []))} messages")
    print(f"  - User Name: {state.values.get('user_name', 'Unknown')}")
    print(f"  - Conversation Count: {state.values.get('conversation_count', 0)}")
    print(f"  - Topics: {state.values.get('topics_discussed', [])}")
    print()


if __name__ == "__main__":
    # Run the conversation
    run_conversation()
    
    # Inspect the saved state
    inspect_checkpoints()
