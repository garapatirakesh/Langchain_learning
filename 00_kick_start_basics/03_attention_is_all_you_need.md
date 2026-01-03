# Section 3: "Attention Is All You Need"

## 1. The Paper That Changed Everything
In 2017, Google researchers were tired of the slowness of LSTMs. They published **"Attention Is All You Need"**, proposing the **Transformer**.

**Key Hypothesis**: "We don't need recurrence (reading one by one). We just need Attention."

---

## 2. The Core Concept: Self-Attention
Self-Attention is a mechanism that allows the model to look at **every word in the sentence at the same time** and decide which words are related.

### The "Bank" Analogy
Consider the word "Bank". It is homonymous (has multiple meanings).

**Sentence A**: *"I sat by the river bank."*
**Sentence B**: *"I deposited money in the bank."*

To a computer, the word "bank" is just a token ID (e.g., #5921). How does it know the meaning?

**How Self-Attention solves it:**
1.  The model looks at "Bank" in Sentence A.
2.  It calculates a "relevance score" (Attention Score) against every other word: "I", "sat", "by", "the", "river".
3.  It finds a **Strong Connection** with "**River**".
4.  It updates the vector for "Bank" to mean "Geological Landform".

In Sentence B:
1.  It finds a **Strong Connection** with "**Deposited**" and "**Money**".
2.  It updates the vector for "Bank" to mean "Financial Institution".

It does this for **every word** pairing simultaneously.

---

## 3. Why Transformers Won
1.  **Context**: Because every word looks at every other word, the "distance" between words doesn't matter. Word #1 refers to Word #1000 just as easily as Word #2. No "Vanishing Gradient".
2.  **Parallelization**: Since we don't need to wait for Word #1 to process Word #2, we can feed the **entire Internet** into the model at once (batches) and train on thousands of GPUs.

This capability to scale is what allowed GPT models to grow from millions to **billions** of parameters.

---

## 4. Code Corner: Simple Self-Attention
Attention is just math for "How relevant is Word A to Word B?".

```python
import numpy as np

def softmax(x):
    e_x = np.exp(x)
    return e_x / e_x.sum()

# We represent words as vectors (Embeddings)
# Let's say we have 3 words: [Bank, River, Money]
# Ideally: Bank should match high with River (if it's a river bank) or Money (if it's a financial bank)

# Let's define the current context: "River Bank"
# We want to know what "Bank" pays attention to.

# Simplified Vectors (normally these are learned)
vector_river = np.array([0.9, 0.1])
vector_bank  = np.array([0.8, 0.2]) # Similar to River
vector_money = np.array([0.1, 0.9]) # Different

# 1. The Dot Product measures similarity
score_river_bank = np.dot(vector_river, vector_bank) # 0.72 + 0.02 = 0.74
score_money_bank = np.dot(vector_money, vector_bank) # 0.08 + 0.18 = 0.26

scores = np.array([score_river_bank, score_money_bank])
print(f"Raw Scores: {scores}") 

# 2. Softmax turns scores into probabilities (Attention Weights)
attention_weights = softmax(scores)
print(f"Attention Weights: {attention_weights}")
# Result: [0.61, 0.38] -> "Bank" pays 61% attention to "River" and 38% to "Money"
```
