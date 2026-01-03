from dotenv import load_dotenv

from deepagents.graph import create_deep_agent
from deepagents.middleware.subagents import SubAgentMiddleware
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

load_dotenv()

# --- 1. Define LLM ---
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# --- 2. Create a Specialist Agent (The Subagent) ---
# This agent is good at one thing: Weather.
@tool
def check_weather(city: str) -> str:
    """Gets the current weather for a city."""
    return f"The weather in {city} is 22°C and sunny."

specialist_agent_graph = create_deep_agent(
    llm=llm,
    tools=[check_weather],
)

# --- 3. Create the Manager Agent ---
# The Manager doesn't have weather tools directly.
# Instead, it has SubAgentMiddleware which allows it to delegate.

subagent_middleware = SubAgentMiddleware(
    # We define a "team" of subagents the manager can talk to
    subagents={
        "weather_expert": specialist_agent_graph
    }
)

manager_agent = create_deep_agent(
    llm=llm,
    tools=[], # Manager has no tools of its own
    middleware=[subagent_middleware]
)

# --- 4. Execute ---
def main():
    print("🚀 Running Manager-Subagent Delegation Demo...")
    
    # Task: Something the manager can't do without the subagent
    task = "Find out the weather in San Francisco and give me a travel recommendation."
    
    result = manager_agent.invoke({"task": task})
    
    print("\n--- MANAGER'S FINAL RESPONSE ---")
    print(result.get("response"))

if __name__ == "__main__":
    main()
