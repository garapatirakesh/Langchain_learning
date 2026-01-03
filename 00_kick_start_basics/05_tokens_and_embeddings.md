# Tokens, Embeddings, and Vectors: How AI "Understands" Meaning

In the previous guide, we learned that models are "Next Token Predictors". But what is a Token? And how does the computer understand that "Apple" is a fruit and also a technology company?

## 1. Tokens: The Atoms of Language
Humans read characters and words. LLMs read **Tokens**.

### What is a Token?
A token is a chunk of text. It can be:
- A whole word: `apple`
- A part of a word: `ing` in "playing"
- A character: `a`
- A punctuation mark: `?`

**Rule of Thumb**: 1,000 tokens is roughly 750 words (in English).

### Why does this matter?
1.  **Cost**: API providers (OpenAI, Anthropic) charge by the literal token count (Input + Output).
2.  **Weaknesses**: Because models see tokens, not letters, they are bad at character-level tasks.
    - *Example*: If you ask `How many 'r's are in 'Strawberry'?`, an older model might fail. Why? Because to the model, the token `Strawberry` is a single ID number (e.g., `8503`). It doesn't "see" the letters inside unless it breaks it down.

### Context Window
The "Context Window" is how many tokens the model can keep in its working memory at once.
- GPT-4o has a massive context window (128k tokens ~ 300 pages of a book).
- If your conversation goes over this limit, the model "forgets" the earliest messages.

---

## Code Corner A: Visualizing Tokens
You can use the library `tiktoken` (used by OpenAI) to see this yourself.

```python
import tiktoken

# Load the encoding for GPT-4
enc = tiktoken.encoding_for_model("gpt-4")

text = "The quick brown fox"
tokens = enc.encode(text)

print(f"Encoded IDs: {tokens}")
print(f"Decoded chunks: {[enc.decode([t]) for t in tokens]}")
# Output might look like: ['The', ' quick', ' brown', ' fox']
# Notice the spaces are part of the tokens!
```


---

## 2. Embeddings: Turning Words into Numbers
Computers can't do math on the word "Dog". They need numbers. But we can't just assign `Dog = 1` and `Cat = 2`, because `2 - 1 = 1` doesn't mean `Cat - Dog = ?`.

We need a system where numbers capture **Meaning**.

### The Vector (The Coordinate)
Imagine a 2D graph.
- X-axis: "Royalty"
- Y-axis: "Gender"

1.  **King**: High Royalty, Male -> `[0.9, 0.1]`
2.  **Queen**: High Royalty, Female -> `[0.9, 0.9]`
3.  **Man**: Low Royalty, Male -> `[0.1, 0.1]`
4.  **Woman**: Low Royalty, Female -> `[0.1, 0.9]`

Real LLMs don't have just 2 dimensions (axes). They have **thousands** (e.g., 1,536 dimensions for OpenAI).
Every piece of text becomes a list of numbers: `[0.002, -0.45, 0.88, ...]`.

### The Magic of "Vector Math"
Because words are positions in space, we can do math with meaning:
**Vector (King) - Vector (Man) + Vector (Woman) ≈ Vector (Queen)**

This is **Embedding**. It embeds a thought into a multi-dimensional math space.

---

## 3. Semantic Search (Vector Search)
This is the foundational concept for **RAG (Retrieval Augmented Generation)**.

### The Problem: Keyword Search
If you search for "furry pet", a Keyword Search (Ctrl+F) looks for the exact word "furry". It **won't** find a document that says "I love my cat", because the word "furry" isn't there.

### The Solution: Semantic Search
1.  Turn your query "furry pet" into a Vector (Embedding).
2.  Turn all your documents ("I love my cat", "Cars are fast") into Vectors.
3.  **Cosine Similarity**: Measure the distance between the query vector and document vectors.
    - "Furry pet" and "I love my cat" will be very close in the vector space (High probability of related meaning).
    - "Furry pet" and "Cars are fast" will be far apart.

**Result**: The AI finds the *meaning*, not just the keyword.

---

## 4. Temperature: The "Creativity" Knob
When an LLM predicts the next token, it assigns a probability to every possible word in its vocabulary.

**Context**: "The sky is..."
- `blue` (90%)
- `Cloudy` (5%)
- `Green` (0.001%)

### What does Temperature do?
- **Temp = 0**: The model ALWAYS picks the highest probability word (`blue`). It is deterministic, focused, and boring. Great for Code or Facts.
- **Temp = 1 (or higher)**: The model flattens the curve. It might pick `Cloudy` or even `Green`. It encourages variety and "Hallucination" (Creativity).

---

## Summary for New Bees

1.  **Tokens**: The chunks models read. Not words.
2.  **Embeddings**: Converting meaning into a list of numbers (Vectors).
3.  **Vector Store/DB**: A database that stores these numbers to help AI search by *meaning*.
4.  **Temperature**: A setting. Low = Fact/Code. High = Poem/Story.

---

## Code Corner B: Cosine Similarity
How do we mathematically find which documents are effectively the same?

```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Let's say we have 3 sentences turned into 2D vectors
# 1. "I love dogs" (Pet)
# 2. "I like cats" (Pet)
# 3. "I drive a car" (Vehicle)

vec_dog = np.array([[0.9, 0.1]]) # High "Living thing", Low "Mechanical"
vec_cat = np.array([[0.8, 0.2]])
vec_car = np.array([[0.1, 0.9]]) # Low "Living thing", High "Mechanical"

# Similarity between Dog and Cat
sim_dog_cat = cosine_similarity(vec_dog, vec_cat)
print(f"Dog vs Cat: {sim_dog_cat[0][0]:.4f}") # High Number

# Similarity between Dog and Car
sim_dog_car = cosine_similarity(vec_dog, vec_car)
print(f"Dog vs Car: {sim_dog_car[0][0]:.4f}") # Low Number
```

