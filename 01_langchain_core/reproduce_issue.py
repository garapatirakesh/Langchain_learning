
import os
import getpass

print("Inspecting imports...")
try:
    import langchain.agents
    print(f"langchain.agents has create_agent: {'create_agent' in dir(langchain.agents)}")
    from langchain.agents import create_agent
    # Check signature roughly or just try to use interrupt_before
except ImportError as e:
    print(f"ImportError: {e}")


try:
    from langchain.agents.middleware import HumanInTheLoopMiddleware
    print("HumanInTheLoopMiddleware found.")
except ImportError:
    print("HumanInTheLoopMiddleware NOT found in langchain.agents.middleware")

# Define tools and model first
# Using ChatOpenAI 
model = ChatOpenAI(model="gpt-4o")

# Try to run with interrupt_before instead of middleware to see if it works/is supported
print("\n--- Attempting fix with interrupt_before ---")
try:
    # Attempt to create agent with interrupt_before kwarg
    agent = create_agent(
        model=model,
        tools=[read_email_tool, send_email_tool],
        checkpointer=checkpointer,
        interrupt_before=["send_email_tool"] 
    )
    print("Created agent with interrupt_before.")
    
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "Read my latest email and send a reply to John Doe saying I'll be late to the meeting."}]},
        config=config
    )
    print("Response (fix attempt):", response)
except Exception as e:
    print(f"Fix attempt failed (likely create_agent doesn't accept interrupt_before or other issue): {e}")

# ORIGINAL FAILING CALL (commented out or kept for checking imports)
# print("Invoking agent...")

try:
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "Read my latest email and send a reply to John Doe saying I'll be late to the meeting."}]},
        config=config
    )
    print("Response:", response)
except Exception as e:
    print(f"Caught expected error: {e}")
