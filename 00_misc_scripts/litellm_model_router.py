import os
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

def model_router(prompt):
    """
    Simulates a logic-based model router.
    - Short/Simple prompts go to a cheap model (GPT-3.5 or Llama).
    - Complex/Long prompts go to an expensive model (GPT-4).
    """
    print(f"\nRouting Prompt: '{prompt[:40]}...'")
    
    # Logic: If prompt > 50 chars, use expensive model
    if len(prompt) > 50:
        model = "openai/gpt-4o"
        print(">> Decision: COMPLEX -> Using GPT-4o")
    else:
        model = "openai/gpt-4o-mini" # Or "groq/llama-3.1-70b-versatile"
        print(">> Decision: SIMPLE -> Using GPT-4o-mini")
        
    response = completion(model=model, messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content

if __name__ == "__main__":
    # Test 1: Simple
    res1 = model_router("Hello!")
    print(f"Result: {res1}")
    
    # Test 2: Complex
    res2 = model_router("Explain the theory of general relativity in the style of a pirate and provide 3 mathematical equations.")
    print(f"Result: {res2[:100]}...")
