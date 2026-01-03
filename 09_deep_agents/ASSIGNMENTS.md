# Deep Agents (From Scratch) Assignments

## Objective
Understand the internal mechanics of agents by building them without frameworks like LangChain or LangGraph. Pure Python and API calls.

## Prerequisite Knowledge
- Python Control Flow (loops, functions)
- Basics of LLM API (OpenAI/Anthropic)
- `concepts_explained.py`

## Practical Assignments

### Assignment 1: The Basic Loop
**Goal:** Create a chatbot loop.
**Task:**
1.  Create a `while True` loop.
2.  Take user input.
3.  Append to a `messages` list.
4.  Call the LLM API.
5.  Print response and append to messages.
6.  Allow a "quit" command to exit.

### Assignment 2: Manual Tool Calling
**Goal:** Implement "ReAct" logic manually.
**Task:**
1.  Define a function `get_weather(city)`.
2.  Define a "system prompt" that tells the LLM: "If you need weather, output JSON: {'tool': 'get_weather', 'city': '...'}".
3.  In your loop: Check if the LLM output is that JSON.
4.  If yes: Run the python function `get_weather`.
5.  Add the result to the `messages` list with a "User/System" role (e.g., "Tool Output: Sunny").
6.  Call LLM again to get the final answer.

### Assignment 3: Reflection Step
**Goal:** Add a self-correction mechanism.
**Task:**
1.  Before showing the final answer to the user, intercept it.
2.  Send it to a "Critic" LLM call: "Review this answer for accuracy. Output OK or IMPROVE: [suggestions]."
3.  If "IMPROVE", add the critique to the context and ask the original LLM to fix it.
4.  Loop max 2 times.

### Assignment 4: Planning System
**Goal:** Separate planning from execution.
**Task:**
1.  User asks a complex question (e.g., "Plan a trip to Paris").
2.  Step 1: Application calls LLM to generate a **Plan** (List of steps).
3.  Step 2: Loop through the steps one by one. For each step, call the Act/Execute LLM.
4.  Accumulate results.

## Conceptual Quiz
1.  What is the "Context Window" limit?
2.  Why is "System Prompt" different from "User Prompt"?
3.  What happens if the "Tool Output" is too large for the context?
