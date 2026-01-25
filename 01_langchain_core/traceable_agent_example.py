
import os
from dotenv import load_dotenv
from getpass import getpass

# Load key from .env file (assuming it's in the parent directory as found earlier)
# You can also manually set them:
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = "your-api-key"
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print(f"API Key: {OPENAI_API_KEY}")

# must enter API key
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY") or \
    getpass("Enter LangSmith API Key: ")

LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
print(f"LANGCHAIN_API_KEY Key: {LANGCHAIN_API_KEY}")

# CRITICAL STEP: Enable Tracing
os.environ["LANGCHAIN_TRACING_V2"] = "true"
# Optional: Set a project name
os.environ["LANGCHAIN_PROJECT"] = "ToolCallLimitMiddleware Demo"

from langchain.agents import create_agent
from langchain.agents.middleware import ToolCallLimitMiddleware
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI # Using langchain_openai for the model string to work smoothly or verify

@tool(parse_docstring=True)
def search_items(query: str) -> str:
    """Search for items in the store.

    Args:
        query: Search query to find items.

    Returns:
        List of matching items with IDs and prices.
    """
    return """Found 3 items:
    - ID: hdpn-001, Sony WH-1000XM5, $299.99, rating 4.5/5
    - ID: hdpn-002, Bose QuietComfort 45, $279.00, rating 4.7/5
    - ID: hdpn-003, Apple AirPods Max, $549.00, rating 4.8/5"""


@tool(parse_docstring=True)
def purchase_item(item_id: str) -> str:
    """Purchase an item by its ID.

    Args:
        item_id: The unique identifier of the item to purchase.

    Returns:
        Purchase confirmation.
    """
    # Simulate purchase
    return f"✓ Successfully purchased item {item_id}"


PROMPT = """
You are a shopping assistant. Help users search for and purchase items.
Use the search_items tool to find items and the purchase_item tool to purchase items.
Make sure to use the ratings of the items to make the best purchase decision.
"""

# Ensure OpenAI API Key is set (loaded from .env)
if not os.environ.get("OPENAI_API_KEY"):
    print("Warning: OPENAI_API_KEY not found in environment.")

try:
    # Explicitly creating model to avoid potential registry lookup issues if just string is passed 
    # and environment is complex, though string usually works.
    model = ChatOpenAI(model="gpt-4o")

    agent = create_agent(
        model=model, # Passing object instead of string for clarity
        tools=[search_items, purchase_item],
        system_prompt=PROMPT,
        middleware=[
            ToolCallLimitMiddleware(
                tool_name="purchase_item",
                run_limit=1,  # Max 1 purchase per conversation turn
                thread_limit=2,  # Max 2 purchases total across all conversation turns
            )
        ],
    )
    
    print("Invoking agent with tracing enabled...")
    response = agent.invoke({"messages": [{"role": "user", "content": "Find and buy me the best headphones under $300."}]})
    print("Response:", response)
    print("\nCheck your LangSmith project 'ToolCallLimitMiddleware Demo' for the trace!")

except Exception as e:
    print(f"Error occurred: {e}")
