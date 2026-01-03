# Understanding A2A (Agent-to-Agent) Protocols

## What is A2A?
**A2A (Agent-to-Agent)** is an open communication standard (pioneered by Google and now part of the Linux Foundation) that allows AI agents to talk to each other. 

In a world where we have many specialized agents (Coding agents, Legal agents, Math agents), we need a "language" for them to collaborate. That language is A2A.

## Key Components of A2A

### 1. The Agent Card (Discovery)
How does one agent know what another agent can do? 
Each A2A-compliant agent exposes an **Agent Card**. 
- **Name**: The identifier.
- **Capabilities**: A list of tasks it can perform (e.g., `execute_sql`, `summarize_text`).
- **Input/Output Schemas**: Standard JSON schemas for interaction.

### 2. Tasks and Lifecycle
In A2A, agents don't just "chat." They exchange **Tasks**.
A task has a clear lifecycle:
1.  **Request**: The Consumer agent asks the Provider agent to do something.
2.  **Acknowledge**: The Provider says "Got it, I'm working on it."
3.  **Status Updates**: Optional updates for long-running tasks.
4.  **Completion**: The Provider delivers the final result.

### 3. Artifacts
The output of an A2A task is called an **Artifact**. 
Artifacts are structured data. If a Coding Agent writes code, the artifact contains the code, the file name, and perhaps instructions on how to run it.

## Code Example: A Simple Multi-Agent Hand-off

Imagine a **Travel Orchestrator** agent (Consumer) and a **Flight Specialist** agent (Provider).

**Message 1: Consumer -> Provider (Task Creation)**
```json
{
  "jsonrpc": "2.0",
  "method": "create_task",
  "params": {
    "task_id": "FL-123",
    "prompt": "Find the cheapest flight from NYC to London on Dec 20",
    "constraints": { "budget": 500 }
  }
}
```

**Message 2: Provider -> Consumer (Artifact Delivery)**
```json
{
  "jsonrpc": "2.0",
  "result": {
    "status": "completed",
    "artifacts": [
      {
        "id": "A1",
        "type": "flight_option",
        "data": {
          "airline": "SkyWays",
          "price": 420,
          "cabin": "Economy"
        }
      }
    ]
  }
}
```

## How A2A differs from MCP

| Feature | MCP (Model Context Protocol) | A2A (Agent-to-Agent) |
| :--- | :--- | :--- |
| **Players** | Model and Tools/Data | Agent and Agent |
| **Logic Location** | The model decides which tool to call. | The agent decides which other agent to delegate to. |
| **Complexity** | Simple Tool Calls (Input -> Result). | Complex Tasks (Asynchronous, Multi-step). |
| **Privacy** | The central model sees everything. | Providers can keep their internal tools/data private (Opacity). |

## Summary for Students
Learn A2A if you want to build **Multi-Agent Systems (MAS)**. While MCP is great for making a single agent smarter by giving it a calculator, A2A is for building an entire *department* of AI agents that work together to solve enterprise problems.
