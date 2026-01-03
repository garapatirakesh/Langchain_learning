# Prompting & Reasoning: Speaking the Language of AI

Now that we know how the model thinks (Probabilities & Tokens), how do we make it do useful work? This is the art of **Prompt Engineering**.

## 1. The Structure of a Prompt
In modern Chat APIs (like OpenAI's), a prompt isn't just one string. It's a list of messages with **Roles**.

1.  **System Role**: Where you define the **Persona** and **Rules**.
    *   *Example*: "You are a senior Python engineer. Answer succinctly. Never explain basic concepts."
    *   *Why*: This sets the "vibe" and constraints for the entire conversation.
2.  **User Role**: The actual task or question.
    *   *Example*: "Write a script to parse a CSV."
3.  **Assistant Role**: The AI's response (or a pre-filled response you create to guide it).

---

## 2. Core Techniques

### A. Zero-Shot Prompting
Asking the model to do something without giving examples.
*   **Prompt**: "Classify this movie review as positive or negative: 'The lighting was terrible.'"
*   **Result**: "Negative"
*   *Use when*: The task is common/easy (Translation, Summary, Simple Sentiment).

### B. Few-Shot Prompting (In-Context Learning)
The most powerful "quick fix". You give the model examples of the Input->Output pattern you want.
*   **Prompt**:
    ```text
    Convert these slang terms to formal English.
    Input: "No cap" -> Output: "Truthfully"
    Input: "Bet" -> Output: "Agreed"
    Input: "Rizz" -> Output: "Charisma"
    Input: "Yeet" -> Output:
    ```
*   **Result**: "Throw" (The model copies the pattern).
*   *Use when*: You need a very specific output format or style.

### C. Chain of Thought (CoT)
"Let's think step by step."
*   **The Problem**: LLMs are bad at math and logic if forced to answer immediately.
*   **The Fix**: Force the model to "show its work" before giving the answer.
*   **Prompt**:
    ```text
    Q: I have 5 apples. I eat 2. I buy 3 more. How many?
    A: Let's think step by step.
    1. Start with 5.
    2. Eat 2, so 5 - 2 = 3.
    3. Buy 3, so 3 + 3 = 6.
    Final Answer: 6.
    ```
*   *Why it works*: Remember the "Next Token Prediction"? By generating the reasoning steps, the model produces tokens that *help it predict the correct final number*. It basically writes its own scratchpad.

---

## 3. Hallucination: When AI Lies
**Hallucination** is when the model confidently states something that is factually wrong.

### Why?
1.  **Probabilistic**: It doesn't "know" facts. It knows which words usually follow other words. If it has never seen a specific fact, it will guess the most "plausible-sounding" words.
2.  **Yes-Man Bias**: Models are trained to be helpful. If you ask "When did George Washington invent the iPhone?", it might try to invent a date rather than correcting you, because it wants to "complete" your pattern.

### How to fix it?
1.  **"I don't know"**: Explicitly tell the System Prompt: "If you do not know the answer, say 'I don't know'. Do not make things up."
2.  **RAG (Retrieval Augmented Generation)**: Don't rely on the model's internal memory. Feed it the correct facts in the prompt (we will cover this next).

---

## Summary for New Bees

1.  **System Prompt**: Give the AI a job description.
2.  **Few-Shot**: Give examples. "Monkey see, Monkey do" is very effective for LLMs.
3.  **Chain of Thought**: Ask for "Step by step" reasoning for logic puzzles.
4.  **Skepticism**: Always verify facts. LLMs are dream machines, not search engines.

---

## 5. Code Corner: The Chat Format
When you code with Python, you don't just send a string. You send a list of dictionaries.

```python
from openai import OpenAI
client = OpenAI()

messages = [
    # 1. SYSTEM: The "God Mode" instruction
    {"role": "system", "content": "You are a poetic assistant. Speak in rhymes."},
    
    # 2. USER: The actual request
    {"role": "user", "content": "Explain quantum physics."}
]

response = client.chat.completions.create(
    model="gpt-4",
    messages=messages
)

# 3. ASSISTANT: The AI's reply
print(response.choices[0].message.content)
```
