import os
from dotenv import load_dotenv

# The deepagents library provides a high-level factory for agents
from deepagents.graph import create_deep_agent
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

load_dotenv()

# --- 1. Define Tools ---
@tool
def calculate_calculator(expression: str) -> str:
    """Useful for mathematical calculations. Input should be a math expression like '2 + 2'."""
    try:
        return str(eval(expression))
    except Exception as e:
        return str(e)

@tool
def search_the_web(query: str) -> str:
    """Useful for finding current information. Input should be a search query."""
    # Mocking a search response for demonstration
    return f"Search result for '{query}': Deep Agents are a LangChain library for persistent, stateful agents."

# --- 2. Configure the Model ---
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# --- 3. Create the Deep Agent ---
# The create_deep_agent function constructs the LangGraph for us,
# including built-in planning and execution loops.
agent = create_deep_agent(
    llm=llm,
    tools=[calculate_calculator, search_the_web],
    # You can customize the prompt if needed, but the library comes with smart defaults
    # prompt="You are an expert researcher. Use tools to find and process information."
)

# --- 4. Execute the Agent ---
def main():
    print("🚀 Running Simple Deep Agent...")
    
    # We invoke it with a task. The agent will autonomously decide:
    # 1. To search for information
    # 2. To calculate if needed
    # 3. To summarize results
    task = "Find out what Deep Agents are and then calculate 1234 * 5678."
    
    # Deep Agents return a stream of events or final output
    # For simplicity, we invoke it synchronously here
    result = agent.invoke({"task": task})
    
    print("\n--- AGENT RESPONSE ---")
    print(result.get("response", "No response found."))

if __name__ == "__main__":
    main()
