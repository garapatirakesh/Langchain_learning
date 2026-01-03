import json
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List, Optional
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- DATA MODELS ---

class Question(BaseModel):
    id: str
    type: str = Field(description="Type of input: 'text', 'checkbox', or 'radio'")
    label: str
    options: Optional[List[str]] = Field(default=None, description="Only for checkbox/radio")

class Questionnaire(BaseModel):
    title: str
    questions: List[Question]

# --- LOGIC ---

def generate_followup_questions(user_request: str):
    """
    Analyzes a user request and generates clarifying questions 
    to create a better diagram.
    """
    print(f"User Request: {user_request}\n")
    print("AI is determining what clarifying questions to ask...")
    
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a diagramming assistant. Before generating a diagram, you must ask 2-3 clarifying questions to understand the scope, stages, and data types. Use 'text', 'checkbox', or 'radio' for question types."},
            {"role": "user", "content": user_request}
        ],
        response_format=Questionnaire,
    )
    
    return completion.choices[0].message.parsed

if __name__ == "__main__":
    request = "generate a image processing using machine learning"
    questions = generate_followup_questions(request)
    
    print(f"\n--- {questions.title} ---")
    for q in questions.questions:
        print(f"\n[{q.type.upper()}] {q.label}")
        if q.options:
            print(f"Options: {', '.join(q.options)}")
    
    print("\n[INFO] This logic allows your app to interview the user dynamically, just like Eraser.io!")
