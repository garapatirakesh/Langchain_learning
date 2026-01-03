import os
import tempfile
from dotenv import load_dotenv

from deepagents.graph import create_deep_agent
from deepagents.middleware.fs import FileSystemMiddleware
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

load_dotenv()

# --- 1. Define Tools that interact with the environment ---
# Built-in FileSystemMiddleware will automatically provide tools to the agent
# like 'read_file', 'write_file', 'list_files', etc. 
# but we can also define specific domain tools.

@tool
def get_stock_data(symbol: str) -> str:
    """Mock stock data fetcher."""
    return f"Stock {symbol} is currently at $150.00. Previous close was $148.50."

# --- 2. Configure Model and Middleware ---
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# We create a sandboxed directory for the agent to work in
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"📁 Initializing agent with sandboxed file system at: {temp_dir}")
    
    # Initialize the FileSystemMiddleware
    # This gives the agent a set of tools to manage data independently of the chat context
    fs_middleware = FileSystemMiddleware(root_dir=temp_dir)

    # create_deep_agent accepts a list of middleware
    agent = create_deep_agent(
        llm=llm,
        tools=[get_stock_data],
        middleware=[fs_middleware]
    )

    # --- 3. Execute ---
    def run_fs_demo():
        print("\n🚀 Task: Analyze stock and SAVE a report to a file.")
        
        # We tell the agent to write its findings to a file
        task = "Fetch stock data for AAPL, calculate the daily gain/loss, and save a full report in a file named 'aapl_report.txt'."
        
        result = agent.invoke({"task": task})
        
        print("\n--- AGENT SUMMARY ---")
        print(result.get("response"))

        # Verify the file was actually created in the sandbox
        report_path = os.path.join(temp_dir, "aapl_report.txt")
        if os.path.exists(report_path):
            with open(report_path, "r") as f:
                print(f"\n📄 CONTENT OF 'aapl_report.txt' (from sandbox):")
                print("-" * 30)
                print(f.read())
                print("-" * 30)
        else:
            print("\n❌ File was not created in the expected location.")

if __name__ == "__main__":
    run_fs_demo()
