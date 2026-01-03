import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def demo_streaming():
    print("--- LLM Streaming (SSE) Simulation ---")
    print("AI Response: ", end="", flush=True)
    
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Write a 3-sentence story about a spaceship."}],
        stream=True,
    )
    
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            print(content, end="", flush=True)
            # Simulate a slight delay for better visual effect in CLI
            time.sleep(0.05)
    print("\n\nStream finished.")

if __name__ == "__main__":
    demo_streaming()
