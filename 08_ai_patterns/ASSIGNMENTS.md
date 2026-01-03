# AI Patterns Assignments

## Objective
Learn common UX and Architectural patterns for AI applications.

## Prerequisite Knowledge
- Structured Output (JSON)
- UI/UX basics

## Practical Assignments

### Assignment 1: Structured Diagram Generation
**Goal:** Create a reliable generator for visual syntax.
**Task:**
1.  Choose a diagram syntax (MermaidJS or Graphviz).
2.  Create a prompt that instructs the LLM to output *only* the code block.
3.  Example Prompt: "Generate a MermaidJS flowchart for a login process."
4.  Validate that the output starts with `graph TD` (or similar).

### Assignment 2: The "Follow-up" Engine
**Goal:** Drive engagement by predicting user intent.
**Task:**
1.  Context: The user just asked "How do I bake a cake?".
2.  Task: Generate 3 short, relevant follow-up questions buttons (e.g., "Chocolate or Vanilla?", "Do you have an oven?", "Gluten-free?").
3.  Implementation: Create a specific prompt for this task. Input: Conversation History. Output: List of 3 strings.

### Assignment 3: Stream-to-UI Parser
**Goal:** Render partial UI while streaming.
**Task:**
1.  Simulate a stream of text that contains custom tags, e.g., `Here is the data: <chart>...data...</chart>`.
2.  Write a parser that buffers the stream.
3.  When it detects `<chart>`, it shouldn't print the raw tag but trigger a "Chart Rendering" placeholder.

## Conceptual Quiz
1.  Why is "Streaming" critical for AI UX perceived latency?
2.  What is "Generative UI"?
3.  How do you handle the "Thinking" state in the UI?
