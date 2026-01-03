# DeepAgents Library: Key Concepts

The `deepagents` library is an "Agent Framework" built on top of LangGraph. It differs from standard LangGraph by providing a **higher-level abstraction** and a **modular middleware system**.

## 🧠 Autonomous Planning Loop
Unlike a standard `ReAct` agent which often goes back and forth between one tool and one thought, Deep Agents are designed with a **Loop-within-a-Loop** architecture:
1.  **Macro-Plan**: The agent creates an internal plan (Step 1, Step 2, Step 3).
2.  **Micro-Execution**: The agent executes each step, potentially using multiple tools or subagents per step.
3.  **Reflection & Update**: After each step, the agent updates its internal plan based on what it discovered.

## 🧱 The Middleware Pattern
In standard LangGraph, you manually add nodes for things like "File Writing" or "Human Approval". In the `deepagents` library, these are encapsulated as **Middleware**.
- Middleware automatically injects the necessary **Tools** into the agent's toolbox.
- Middleware handles the **Node logic** for those tools.
- This allows you to create a "File Expert" by simply adding `FileSystemMiddleware()` to any agent.

## 🏗️ Hierarchy and Delegation (Subagents)
Deep Agents support **Hierarchical delegation** out of the box. 
- A **Manager** can be a Deep Agent.
- Its **sub-workers** can also be Deep Agents.
- The `SubAgentMiddleware` handles the handoff of task descriptions and the return of results, keeping the manager's context window clean from the specialist's noise.

## 💾 Context Sandboxing
One of the unique features of the `deepagents` library is managing large/long-running context via a **virtual file system**. 
- Instead of keeping a 50-page PDF in the prompt, the agent saves it to its "workspace".
- It reads only what it needs, when it needs it.
- This effectively gives the LLM "Unlimited Memory" by offloading data to disk.

## 🛡️ Stability and Error Recovery
`create_deep_agent` includes built-in retry logic and structured output validation. If a tool fails or the LLM returns invalid data, the internal graph handles the loop-back and correction without you having to write the code for it.

---

*Summary based on LangChain DeepAgents Documentation.*
