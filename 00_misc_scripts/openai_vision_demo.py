import os
import base64
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def demo_vision():
    print("--- OpenAI Vision (GPT-4o) Demo ---")
    # Using a public URL for the demo instead of a local file
    image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Giotto_-_Scrovegni_-_-36-_-__Adoration_of_the_Magi.jpg/640px-Giotto_-_Scrovegni_-_-36-_-__Adoration_of_the_Magi.jpg"

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What is happening in this painting?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    # Note: Ensure your OpenAI API key supports GPT-4o
    try:
        demo_vision()
    except Exception as e:
        print(f"Error: {e}")
