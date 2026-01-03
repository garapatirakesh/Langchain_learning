# LangChain Core Assignments

## Objective
Master the fundamentals of LangChain, including the Expression Language (LCEL), Prompt Templates, Memory management, and Streaming.

## Prerequisite Knowledge
- Basic Python
- Understanding of LLMs
- Notebooks in this folder (`0_lc_basics.ipynb` through `08-streaming.ipynb`)

## Practical Assignments

### Assignment 1: The Translator Chain
**Goal:** Create a simple translation pipeline using LCEL.
**Task:**
1.  Define a `PromptTemplate` that accepts `source_lang`, `target_lang`, and `text`.
2.  Initialize a ChatModel (e.g., `ChatOpenAI` or similar).
3.  Create a chain using the pipe `|` operator: `prompt | model`.
4.  Run the chain to translate "Hello, how are you?" from English to French.
**Challenge:** Add an `OutputParser` (like `StrOutputParser`) to the end of the chain so you get a clean string instead of an `AIMessage`.

### Assignment 2: Chat with History (Memory)
**Goal:** Implement a conversation loop that remembers context.
**Task:**
1.  Use `RunnableWithMessageHistory` or manually manage a list of messages.
2.  Create a chain that takes input and existing history.
3.  Write a simple `while` loop getting user input.
4.  After each turn, print the response and update the history.
**Challenge:** Limit the history to the last 5 messages (Window Memory).

### Assignment 3: Streaming Responses
**Goal:** Handle real-time output from the LLM.
**Task:**
1.  take your chain from Assignment 1 or 2.
2.  Instead of `.invoke()`, use `.stream()`.
3.  Iterate over the chunks and print them immediately (`print(chunk, end="", flush=True)`).
**Challenge:** Modify the stream loop to count the number of tokens/chunks received.

### Assignment 4: Custom Runnable
**Goal:** Understand LCEL deeper by creating a custom function component.
**Task:**
1.  Define a simple python function `length_check(text: str) -> dict`. It should return `{"original": text, "length": len(text)}`.
2.  Make this function a `Runnable` (using `@chain` decorator or `RunnableLambda`).
3.  Insert this into a chain: `prompt | model | parser | length_check`.
4.  Observe how the output changes.

## Conceptual Quiz
1.  What is the primary advantage of using LCEL (pipe syntax) over the legacy `LLMChain` classes?
2.  How does `RunnablePassthrough` help when passing multiple arguments to a prompt?
3.  What happens if you invoke a chain without an OutputParser?
4.  How does LangSmith help with debugging chains?
