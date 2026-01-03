# Module 09: LangGraph Deep Agents

This module explores the `deepagents` library, a high-level framework built on top of LangGraph for creating sophisticated, autonomous agents.

## 🌟 What are Deep Agents?

"Deep Agents" refers to agents designed for **complex, multi-step tasks** that go beyond simple chat or search. According to the official documentation, Deep Agents excel at tasks that require:

1.  **Autonomous Planning**: The agent can break down a large goal into smaller, actionable steps.
2.  **Context Sandboxing (File Systems)**: Managing large amounts of context by using a sandboxed file system, allowing the agent to read, write, and reference files as parts of its reasoning.
3.  **Delegation (Subagents)**: Ability to spawn and manage specialized subagents to isolate context and handle sub-tasks more efficiently.

## 🏗️ Core Architectural Concepts

### 1. The `create_deep_agent` Factory
The library provides a specialized factory function that handles the complex state management, graph construction, and loop logic for you.

### 2. Middleware Architecture
The true power of this library lies in its **Middleware** system. You can "plug in" capabilities to your agent easily:
*   **`FileSystemMiddleware`**: Gives the agent a virtual "hard drive" to store notes, results, and intermediate data.
*   **`SubAgentMiddleware`**: Allows an agent to call another agent (delegation).
*   **`HITLMiddleware`**: Adds Human-in-the-Loop approval checkpoints.

### 3. State Management
Deep agents use a specialized state that tracks the plan, the current task, and the history of actions across multiple turns.

---

## 📂 Module Contents

1.  **01_simple_deep_agent.py**: Introduction to `create_deep_agent` with basic tool use.
2.  **02_filesystem_agent.py**: How to give your agent a sandboxed file system to manage large context.
3.  **03_subagent_delegation.py**: Building "Manager" agents that delegate tasks to "Specialist" agents.
4.  **04_comprehensive_deep_agent.py**: A full-featured agent using planning, filesystems, and subagents.

---

## 🎯 When to Use Deep Agents?

*   **Large Documents**: When the context is too big for a single prompt, use the FileSystem to store and retrieve chunks.
*   **Specialized Knowledge**: When a task needs multiple experts, use Subagents.
*   **Long-Running Tasks**: When a goal requires 10+ steps (like writing a book or complex research).
*   **High Precision**: When you need human approval at critical steps (HITL).

---

## 🚀 Getting Started

1.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Set your API Key** in the `.env` file.
3.  Run the examples in order.

*Reference: [LangGraph Deep Agents Overview](https://docs.langchain.com/oss/python/deepagents/overview)*
