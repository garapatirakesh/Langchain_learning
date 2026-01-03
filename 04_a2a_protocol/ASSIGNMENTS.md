# Agent-to-Agent (A2A) Protocol Assignments

## Objective
Learn how autonomous agents communicate and coordinate with each other.

## Prerequisite Knowledge
- Async/Await
- JSON Schema
- WebSockets or HTTP

## Practical Assignments

### Assignment 1: The Handshake
**Goal:** Establish trust/connection between two agents.
**Task:**
1.  Define a "Hello" message format (e.g., `{"type": "HELLO", "agent_id": "..."}`).
2.  Create Script A (Agent A) that sends this message.
3.  Create Script B (Agent B) that listens, receives it, and replies with `{"type": "WELCOME"}`.

### Assignment 2: Task Delegation
**Goal:** One agent asks another to do work.
**Task:**
1.  Agent A (Manager): Has a user request "Research Python". It determines it cannot do it.
2.  Agent A constructs a message: `{"type": "TASK_REQUEST", "content": "Research Python"}` and sends it to Agent B.
3.  Agent B (Worker): Receives request, simulates work (sleep 2s), and sends back `{"type": "TASK_RESULT", "result": "Python is a language..."}`.
4.  Agent A prints the final result.

## Conceptual Quiz
1.  Why is a standardized protocol necessary for multi-agent systems?
2.  How do we handle an agent that goes offline in the middle of a task?
3.  What is the role of a "Registry" in A2A systems?
