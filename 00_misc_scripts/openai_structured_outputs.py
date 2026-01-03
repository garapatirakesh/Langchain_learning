import os
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. NEW: Structured Outputs with Strict Mode (using Pydantic)
class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]
    importance: int # 1 to 10

def demo_strict_outputs():
    print("--- 1. OpenAI Strict Structured Outputs ---")
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Extract the event information."},
            {"role": "user", "content": "I have a meeting with Rakesh and Anjali on Friday for the budget review. It's high priority, like 9/10."}
        ],
        response_format=CalendarEvent,
    )
    
    event = completion.choices[0].message.parsed
    print(f"Event Object: {event}")
    print(f"Date: {event.date}, Participants: {event.participants}\n")

# 2. Native JSON Mode (Requires "json" in prompt)
def demo_json_mode():
    print("--- 2. OpenAI JSON Mode ---")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": "List 3 colors and their hex codes."}
        ],
        response_format={"type": "json_object"}
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    demo_strict_outputs()
    demo_json_mode()
