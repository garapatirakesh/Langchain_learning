# LangGraph Agents Assignments

## Objective
Learn to build stateful, cyclic, and complex agent workflows using LangGraph.

## Prerequisite Knowledge
- LangChain Core
- Understanding of Graphs (Nodes and Edges)
- Notebooks: `lg_1_basic.ipynb` to `lg_8_deepagent.ipynb`

## Practical Assignments

### Assignment 1: The Linear Pipeline
**Goal:** Build a simple sequential graph.
**Task:**
1.  Define a `State` TypedDict with a key `text`.
2.  Create three nodes: `clean_text` (removes whitespace), `uppercase_text` (converts to caps), and `reverse_text` (reverses string).
3.  Add them to a `StateGraph`.
4.  Connect them linearly: START -> clean -> uppercase -> reverse -> END.
5.  Compile and run.

### Assignment 2: The Logic Router
**Goal:** Implement conditional branching (Conditional Edges).
**Task:**
1.  Create a State with `query` and `classification`.
2.  Node 1: `classify_intent`. Uses an LLM to categorize input as "Greeting", "Math", or "General".
3.  Create 3 handler nodes: `handle_greeting`, `handle_math`, `handle_general`.
4.  Add a **conditional edge** after `classify_intent` that checks the `classification` state and routes to the correct handler.
5.  All handlers go to END.

### Assignment 3: The Generator-Critic Loop
**Goal:** Implement a cycle for quality improvement.
**Task:**
1.  State: `topic`, `draft`, `critique`, `revision_count`.
2.  Node `generate`: Writes a short paragraph on `topic`.
3.  Node `critique`: Reviews the `draft`. If good, returns "ACCEPT". If bad, returns "REVISE" + critique comments.
4.  Conditional Edge:
    - If "ACCEPT": Go to END.
    - If "REVISE" AND `revision_count` < 3: Go back to `generate` (pass critique back so it can improve).
    - If "REVISE" AND `revision_count` >= 3: Go to END (give up).

### Assignment 4: Simple Tool-Using Agent
**Goal:** Recreate a ReAct-style agent manually.
**Task:**
1.  Define a tool (e.g., `multiply(a, b)`).
2.  Node `agent`: Calls LLM with tool binding.
3.  Node `tool_executor`: Executes the tool call if the LLM requested one.
4.  Edge Logic:
    - If LLM output has tool_calls -> go to `tool_executor`.
    - If LLM output is text -> go to END.
    - After `tool_executor`, go back to `agent` with the result.

## Conceptual Quiz
1.  What is the difference between `StateGraph` and `MessageGraph`?
2.  Why do we need to annotate state keys with `operator.add` (reducers) sometimes?
3.  How does `compile()` change the graph structure into a runnable?
4.  What is "Checkpointer" used for in LangGraph?
