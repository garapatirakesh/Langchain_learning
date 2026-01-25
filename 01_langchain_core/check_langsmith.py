
import os

print("Checking LangSmith Configuration...")
env_vars = [
    "LANGCHAIN_TRACING_V2",
    "LANGCHAIN_API_KEY",
    "LANGCHAIN_ENDPOINT",
    "LANGCHAIN_PROJECT"
]

for var in env_vars:
    value = os.environ.get(var)
    if value:
        # Mask key for security
        if "KEY" in var:
            print(f"{var}: {'*' * 8}{value[-4:] if len(value) > 4 else '****'}")
        else:
            print(f"{var}: {value}")
    else:
        print(f"{var}: NOT SET")
