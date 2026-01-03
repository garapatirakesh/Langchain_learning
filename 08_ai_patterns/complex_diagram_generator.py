import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_complex_diagram(prompt: str, context: dict = None):
    """
    Generates Mermaid.js code for a complex diagram based on user requirements.
    """
    print(f"Generating diagram for: {prompt}...")
    
    system_instruction = """
    You are a professional software architect and technical illustrator. 
    Your goal is to generate high-quality Mermaid.js code.
    Guidelines:
    1. Use 'flowchart LR' or 'flowchart TD' depending on what fits best.
    2. Use subgraphs to group related components (e.g., 'Data Preparation', 'Model Training').
    3. Use different node shapes: [rect], ([rounded]), [[subroutine]], {decision}, [/parallel/].
    4. Use meaningful labels and arrows.
    5. Output ONLY the mermaid code, no explanation.
    """
    
    user_input = f"User Request: {prompt}\n\n"
    if context:
        user_input += f"Added Context from follow-up questions: {json.dumps(context)}"

    response = client.chat.completions.create(
        model="gpt-4o", # Using GPT-4o for complex architecture
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_input}
        ]
    )
    
    mermaid_code = response.choices[0].message.content.replace("```mermaid", "").replace("```", "").strip()
    return mermaid_code

if __name__ == "__main__":
    # Example logic combining follow-up knowledge
    user_prompt = "image processing using machine learning"
    clarified_context = {
        "focused_tasks": ["object detection", "segmentation"],
        "stages": ["data preprocessing", "model training", "deployment"],
        "dataset_type": "medical X-ray images"
    }
    
    diagram_code = generate_complex_diagram(user_prompt, clarified_context)
    
    print("\n--- GENERATED MERMAID CODE ---")
    print(diagram_code)
    print("\n[TIP] You can paste this code into 'mermaid.live' to see the beautiful diagram!")
