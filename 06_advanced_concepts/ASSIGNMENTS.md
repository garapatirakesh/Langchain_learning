# Advanced Concepts Assignments

## Objective
Explore advanced topics like RAG, Persistence, and "Time Travel" (State History).

## Prerequisite Knowledge
- Embeddings
- Vector Databases (Concept)
- State Management

## Practical Assignments

### Assignment 1: DIY Vector Search (RAG)
**Goal:** Understand how RAG works mathematically.
**Task:**
1.  Take 5 sentences about different topics.
2.  Use an embedding model (e.g., OpenAI `text-embedding-3-small` or a local SentenceTransformer) to get vectors for each.
3.  Take a user query vector.
4.  Calculate Cosine Similarity between the query vector and the 5 sentence vectors.
5.  Return the sentence with the highest score.

### Assignment 2: State Time Travel
**Goal:** Implement a system that can undo/redo state changes.
**Task:**
1.  Create a class `StateManager`.
2.  It holds `current_state` (dict) and `history` (list of dicts).
3.  Method `update(key, value)`: Save current state to `history`, then update `current_state`.
4.  Method `undo()`: Pop the last state from `history` and make it `current`.
5.  Test it by simulating a conversation where you "undo" the last turn.

### Assignment 3: Subgraphs Config
**Goal:** Managing configuration in nested graphs.
**Task:**
1.  refer to `langgraph_subgraphs_config.ipynb`.
2.  Create a Parent Graph.
3.  Create a Child Graph (Subgraph).
4.  Pass a `config` (e.g., `{"configurable": {"user_id": "123"}}`) from Parent to Child.
5.  Verify the Child can access `user_id`.

## Conceptual Quiz
1.  Why is "Chunking" important in RAG?
2.  What is the trade-off of storing every single state version (History)?
3.  How does Cosine Similarity differ from Euclidean Distance?
