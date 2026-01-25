
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Load env for API key setup (though error is local logic mostly, agent init needs it)
load_dotenv()
if not os.environ.get("OPENAI_API_KEY"):
    print("Warning: OPENAI_API_KEY not set")

# Method 3: Custom detector function (AS PROVIDED BY USER - FAILING)
def detect_ssn(content: str) -> list[dict[str, str | int]]:
    """Detect SSN with validation.

    Returns a list of dictionaries with 'text', 'start', and 'end' keys.
    """
    import re
    matches = []
    pattern = r"\d{3}-\d{2}-\d{4}"
    for match in re.finditer(pattern, content):
        ssn = match.group(0)
        # Validate: first 3 digits shouldn't be 000, 666, or 900-999
        first_three = int(ssn[:3])
        if first_three not in [0, 666] and not (900 <= first_three <= 999):
            matches.append({
                "value": ssn,  # <--- Corrected key
                "start": match.start(),
                "end": match.end(),
                "type": "ssn" # Added type key as it appeared in other errors/logic
            })
    return matches

print("Creating agent to reproduce KeyError...")
try:
    agent3 = create_agent(
        model="gpt-4o",
        tools=[],
        middleware=[
            PIIMiddleware(
                "ssn",
                detector=detect_ssn,
                strategy="hash",
            ),
        ],
    )

    print("Invoking agent...")
    agent3.invoke({"messages": [{"role": "user", "content": "My SSN is 123-45-6789 and 000-12-3456."}]})
except Exception as e:
    print(f"\nCaught expected error: {type(e).__name__}: {e}")
    # print traceback to be sure it matches
    import traceback
    traceback.print_exc()
