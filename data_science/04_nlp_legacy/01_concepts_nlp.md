# NLP: Legacy to Modern

## 1. Tokenization
Cutting text into pieces.
- **Word Level**: ["The", "cat"]
- **Subword Level (BPE/WordPiece)**: Used by modern LLMs. ["Play", "ing"].

## 2. Bag of Words (BoW) & TF-IDF
- **BoW**: Counting word frequency. "Good" = 2.
- **TF-IDF**: "Term Frequency - Inverse Document Frequency".
    - Punishment for common words like "The", "Is".
    - Reward for rare, specific words like "Genome", "Quantum".
    - Matrix is **Sparse** (Mostly zeros).

## 3. Word Embeddings (Word2Vec / GloVe)
- Dense Vectors. `[0.1, -0.9, ...]`.
- captures semantic meaning (King - Man + Woman = Queen).
- Static: "Bank" always has the same vector, regardless of context.

## 4. Sequence Models (RNN / LSTM)
- Process text in order.
- Capable of Context (to an extent).
- **Seq2Seq**: Encoder -> Decoder architecture used for Translation before Transformers took over.

*(Note: Transformers and Attention are covered in the `00_kick_start_basics` folder!)*
