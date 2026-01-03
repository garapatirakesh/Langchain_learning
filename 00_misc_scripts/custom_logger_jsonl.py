import json
import time
import os

def log_to_jsonl(prompt, response, model="gpt-4o-mini"):
    """
    Saves every interaction to a .jsonl file. 
    This is essential for building custom datasets for fine-tuning.
    """
    log_entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "model": model,
        "payload": {
            "messages": [
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": response}
            ]
        }
    }
    
    filename = "llm_interactions.jsonl"
    with open(filename, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    
    print(f"Logged interaction to {filename}")

if __name__ == "__main__":
    # Simulate an interaction
    p = "Tell me a joke."
    r = "Why did the AI cross the road? To get to the other dataset."
    
    log_to_jsonl(p, r)
    
    # Read back to show user
    print("\nCurrent Log Content:")
    with open("llm_interactions.jsonl", "r") as f:
        print(f.read())
