
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware
from langchain_openai import ChatOpenAI
import os
import re
from dotenv import load_dotenv

# Load env 
load_dotenv()
if not os.environ.get("OPENAI_API_KEY"):
    print("Warning: OPENAI_API_KEY not set")

print("Creating agent with compiled regex to reproduce TypeError...")
try:
    # Method 2: Compiled regex pattern (AS PROVIDED BY USER - FAILING)
    agent2 = create_agent(
        model="gpt-4o",
        tools=[],
        middleware=[
            PIIMiddleware(
                "phone_number",
                # This should cause TypeError because it's not callable in the way middleware expects
                detector=re.compile(r"\+?\d{1,3}[\s.-]?\d{3,4}[\s.-]?\d{4}"), 
                strategy="mask",
            ),
        ],
    )
    
    print("Invoking agent...")
    agent2.invoke({"messages": [{"role": "user", "content": "Call me at +1-800-555-1234 or 800.555.5678."}]})
    print("Invoke successful (unexpected if attempting to reproduce error)")

except Exception as e:
    print(f"\nCaught expected error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
