import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def demo_chain_of_thought():
    print("--- 1. Chain of Thought (CoT) ---")
    prompt = "A jug holds 5 liters of water. I pour out 2 liters, then add 4. How much is left? Think step by step."
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    print(response.choices[0].message.content)

def demo_few_shot():
    print("\n--- 2. Few-Shot Prompting ---")
    prompt = """Convert the following into a technical bug report:
User: It crashes when I click save.
Report: [CRITICAL] App enters crash state on SaveButton.onClick.

User: The login screen is blue instead of green.
Report: [UI] Unexpected background-color: blue on /login; expected: green.

User: I can't see the logout button on mobile.
Report:"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    print(response.choices[0].message.content)

def demo_system_constraints():
    print("\n--- 3. System Constraints ---")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a grumpy sailor. Answer in exactly 10 words, no more, no less."},
            {"role": "user", "content": "How's the weather?"}
        ]
    )
    print(response.choices[0].message.content)
    print(f"Word count: {len(response.choices[0].message.content.split())}")

if __name__ == "__main__":
    demo_chain_of_thought()
    demo_few_shot()
    demo_system_constraints()
