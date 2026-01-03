# 🤖 LangGraph Deep Agents - Complete Learning Repository

Welcome to the comprehensive guide on **LangGraph Deep Agents**! This repository contains everything you need to understand and build sophisticated AI agents using LangGraph and OpenAI.

## 📚 What You'll Learn

This repository covers **7 core concepts** of deep agents, progressing from basic to advanced:

1. **Basic Agent with Tools** - Foundation of agent systems
2. **Stateful Agent** - Memory and persistence
3. **Reflection Agent** - Self-improvement through critique
4. **Planning Agent** - Strategic task decomposition
5. **Human-in-the-Loop** - Safety and approval workflows
6. **Multi-Agent Systems** - Collaborative agent architectures
7. **Advanced Deep Agent** - Combining all patterns

## 🗂️ Repository Structure

```
09_deep_agents/
│
├── 📖 Documentation
│   ├── README.md                    ← You are here
│   ├── SETUP.md                     ← Installation & setup guide
│   ├── concepts_explained.py        ← Detailed concept explanations
│   └── visual_summary.py            ← Quick visual reference
│
├── 🎯 Getting Started
│   └── quick_start.py               ← Interactive demo launcher
│
├── 💡 Examples (Study in this order)
│   ├── 01_basic_agent.py            ← Start here!
│   ├── 02_stateful_agent.py
│   ├── 03_reflection_agent.py
│   ├── 04_planning_agent.py
│   ├── 05_human_in_loop.py
│   ├── 06_multi_agent_system.py
│   └── 07_advanced_deep_agent.py    ← Complete implementation
│
└── 📦 Dependencies
    └── requirements.txt
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Your OpenAI API Key

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="sk-your-api-key-here"
```

**Linux/Mac:**
```bash
export OPENAI_API_KEY="sk-your-api-key-here"
```

### 3. Run the Interactive Demo
```bash
python quick_start.py
```

### 4. Explore Concepts
```bash
python concepts_explained.py
```

### 5. Study Examples
```bash
python 01_basic_agent.py
python 02_stateful_agent.py
# ... and so on
```

## 📖 Concept Overview

### 1️⃣ Basic Agent with Tools
**File:** `01_basic_agent.py`

Learn the fundamentals:
- State management with TypedDict
- Tool definition and binding
- Graph structure (nodes and edges)
- Conditional routing

**Flow:**
```
User Input → Agent Decides → Calls Tool → Processes Result → Responds
```

---

### 2️⃣ Stateful Agent with Memory
**File:** `02_stateful_agent.py`

Master persistence:
- Checkpointing with MemorySaver
- Thread-based sessions
- Rich state tracking
- Multi-turn conversations

**Key Feature:** Agent remembers context across multiple interactions!

---

### 3️⃣ Reflection Agent
**File:** `03_reflection_agent.py`

Self-improvement pattern:
- Generate initial output
- Critique the output
- Improve based on critique
- Repeat until quality threshold met

**Pattern:**
```
Generate → Reflect → Improve → (Loop) → Finalize
```

---

### 4️⃣ Planning Agent
**File:** `04_planning_agent.py`

Strategic execution:
- Break down complex tasks into steps
- Execute steps sequentially
- Track progress
- Synthesize results

**Pattern:**
```
Task → Plan → Execute Step 1 → Step 2 → ... → Synthesize
```

---

### 5️⃣ Human-in-the-Loop Agent
**File:** `05_human_in_loop.py`

Safety and control:
- Pause execution for approval
- Integrate human feedback
- Revision based on rejection
- Critical action safeguards

**Pattern:**
```
Propose → Human Reviews → Approve/Reject → Execute/Revise
```

---

### 6️⃣ Multi-Agent System
**File:** `06_multi_agent_system.py`

Collaborative intelligence:
- Specialized agent roles
- Supervisor coordination
- Agent handoffs
- Parallel and sequential workflows

**Agents:**
- Researcher (gathers information)
- Writer (creates content)
- Reviewer (quality control)
- Supervisor (coordinates)

---

### 7️⃣ Advanced Deep Agent
**File:** `07_advanced_deep_agent.py`

Production-ready agent combining:
- ✅ Planning
- ✅ Tool use
- ✅ Reflection
- ✅ State management
- ✅ Quality assessment
- ✅ Confidence scoring

This is the **complete implementation** showing how all patterns work together!

---

## 🎯 Use Case Guide

| Your Need | Use This Example |
|-----------|------------------|
| Call external APIs/tools | #1 Basic Agent |
| Remember conversation history | #2 Stateful Agent |
| Improve output quality | #3 Reflection Agent |
| Handle complex multi-step tasks | #4 Planning Agent |
| Get human approval for actions | #5 Human-in-Loop |
| Divide work among specialists | #6 Multi-Agent System |
| Build production-ready agent | #7 Advanced Deep Agent |

## 🔑 Key Concepts Explained

### State Management
State is the data that flows through your agent graph. It's defined using TypedDict and can include:
- Messages (conversation history)
- User context (name, preferences)
- Task progress (current step, results)
- Metadata (iteration count, quality scores)

### Tools
Functions that agents can call to perform actions:
- API calls
- Database queries
- Calculations
- File operations
- External service integrations

### Nodes
Functions that process state and return updates:
- Agent nodes (LLM decision making)
- Tool nodes (execute tools)
- Processing nodes (data transformation)

### Edges
Connections between nodes:
- **Regular edges:** Always go from A → B
- **Conditional edges:** Route based on state (if/else logic)

### Checkpointing
Saves agent state for:
- Resuming interrupted workflows
- Multi-turn conversations
- Error recovery
- Debugging and replay

## 💡 Learning Path

**Recommended order:**

1. **Start:** Read `SETUP.md` and install dependencies
2. **Understand:** Run `python concepts_explained.py`
3. **Explore:** Run `python quick_start.py` for demos
4. **Study:** Go through examples 01 → 07 in order
5. **Practice:** Modify examples, change prompts, add features
6. **Build:** Create your own agent using these patterns

## 🛠️ Customization Ideas

Try these modifications to deepen your understanding:

1. **Add new tools** to basic agent (weather API, web search)
2. **Extend state** with custom fields (user preferences, history)
3. **Modify reflection criteria** (stricter quality checks)
4. **Change planning strategy** (parallel vs sequential)
5. **Add approval rules** (auto-approve safe actions)
6. **Create new agent roles** (editor, fact-checker, etc.)
7. **Combine patterns** (reflection + planning, multi-agent + HITL)

## 📊 Comparison: Deep Agents vs Simple Chatbots

| Feature | Simple Chatbot | Deep Agent |
|---------|---------------|------------|
| Memory | Basic context window | Rich state + checkpointing |
| Planning | None | Multi-step plans |
| Tool Use | Limited/None | Extensive |
| Self-Improvement | No | Reflection loops |
| Error Recovery | Minimal | Replanning, retry logic |
| Collaboration | Single agent | Multi-agent systems |
| Human Oversight | Rare | Built-in checkpoints |
| Complexity | Simple queries | Complex workflows |

## 🔍 Code Structure

Each example follows this pattern:

```python
# 1. State Definition
class AgentState(TypedDict):
    # Define state schema

# 2. Node Functions
def node_function(state: AgentState) -> AgentState:
    # Process state, return updates

# 3. Graph Construction
workflow = StateGraph(AgentState)
workflow.add_node("name", node_function)
workflow.add_edge("node1", "node2")

# 4. Compilation
app = workflow.compile()

# 5. Execution
result = app.invoke(initial_state)
```

## 📚 Additional Resources

- **LangGraph Docs:** https://langchain-ai.github.io/langgraph/
- **LangChain Docs:** https://python.langchain.com/
- **OpenAI API:** https://platform.openai.com/docs/

## 💰 Cost Considerations

All examples use **GPT-4o-mini** (very cost-effective):
- ~$0.15 per 1M input tokens
- ~$0.60 per 1M output tokens
- Running all examples: **< $0.10 total**

## ❓ Troubleshooting

### "Module not found"
```bash
pip install -r requirements.txt
```

### "OpenAI API key not found"
Set your API key as shown in Quick Start section

### "Rate limit exceeded"
Wait a few moments between runs or upgrade your OpenAI plan

### Import errors
Make sure you're in the correct directory:
```bash
cd c:\Users\Rakesh\vscode_projects\learning\09_deep_agents
```

## 🎓 What Makes an Agent "Deep"?

A deep agent exhibits these characteristics:

1. **🧠 Strategic Thinking** - Plans before acting
2. **🔄 Self-Improvement** - Reflects and improves outputs
3. **🛠️ Tool Mastery** - Effectively uses external tools
4. **💾 Memory** - Maintains context across interactions
5. **👥 Collaboration** - Works with other agents
6. **🎯 Goal-Oriented** - Persists until task completion
7. **🛡️ Safety-Aware** - Seeks approval for critical actions

## 🚀 Next Steps

After completing this tutorial:

1. **Experiment** with the examples
2. **Modify** prompts and parameters
3. **Combine** different patterns
4. **Build** your own agent for a real use case
5. **Share** what you've learned!

## 📝 Notes

- All examples are **self-contained** and can run independently
- Code is **heavily commented** for learning
- Examples use **realistic scenarios**
- Patterns are **production-ready**

## 🤝 Contributing

Feel free to:
- Add new examples
- Improve documentation
- Fix bugs
- Share use cases

---

**Happy Learning! 🎉**

Built with ❤️ using LangGraph and OpenAI

*Last Updated: December 2025*
