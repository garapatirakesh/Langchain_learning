"""
Concepts Explained - Deep Dive into LangGraph Deep Agents

This file provides detailed explanations of each concept with diagrams and examples.
"""


CONCEPTS = """
╔══════════════════════════════════════════════════════════════════════════╗
║                    LANGGRAPH DEEP AGENTS CONCEPTS                        ║
╚══════════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 CONCEPT 1: STATE MANAGEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What: State is the data that flows through your agent graph
Why: Enables agents to maintain context and make informed decisions
How: Use TypedDict to define state schema

┌─────────────────────────────────────────────────────────────┐
│  class AgentState(TypedDict):                               │
│      messages: list[BaseMessage]  # Conversation history    │
│      user_name: str              # User context             │
│      iteration: int              # Progress tracking        │
└─────────────────────────────────────────────────────────────┘

Key Points:
  ✓ State is immutable - nodes return updates, not mutations
  ✓ Use Annotated with operator.add for accumulating lists
  ✓ State persists across node executions
  ✓ Checkpointers save state for recovery and resumption

Example Use Cases:
  • Maintaining conversation history
  • Tracking user preferences
  • Storing intermediate results
  • Managing workflow progress


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔧 CONCEPT 2: TOOL CALLING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What: Tools are functions that agents can call to perform actions
Why: Extends agent capabilities beyond just text generation
How: Define functions and bind them to the LLM

Flow Diagram:
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  User    │───▶│  Agent   │───▶│  Tool    │───▶│  Agent   │
│  Query   │    │  Decides │    │  Executes│    │  Responds│
└──────────┘    └──────────┘    └──────────┘    └──────────┘

Tool Definition Pattern:
┌─────────────────────────────────────────────────────────────┐
│  def my_tool(param: str) -> str:                            │
│      '''Tool description for the LLM.                       │
│                                                              │
│      Args:                                                   │
│          param: Parameter description                       │
│      '''                                                     │
│      # Tool implementation                                   │
│      return result                                           │
└─────────────────────────────────────────────────────────────┘

Best Practices:
  ✓ Clear docstrings (LLM uses these to decide when to call)
  ✓ Type hints for parameters
  ✓ Error handling within tools
  ✓ Return strings or serializable objects


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔄 CONCEPT 3: REFLECTION PATTERN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What: Agent evaluates and improves its own outputs
Why: Increases output quality through self-correction
How: Generate → Critique → Improve → Repeat

Reflection Loop:
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│   ┌──────────┐      ┌──────────┐      ┌──────────┐        │
│   │ Generate │─────▶│ Reflect  │─────▶│ Improve  │        │
│   └──────────┘      └──────────┘      └──────────┘        │
│        ▲                                     │              │
│        │                                     │              │
│        └─────────────────────────────────────┘              │
│                   (if not approved)                         │
└─────────────────────────────────────────────────────────────┘

Implementation Pattern:
  1. Generator Node: Creates initial output
  2. Reflector Node: Critiques the output
  3. Conditional Edge: Decides to improve or finish
  4. Improvement Node: Revises based on critique

When to Use:
  • Writing tasks (essays, code, documentation)
  • Creative tasks (stories, designs)
  • Complex reasoning tasks
  • Quality-critical outputs


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 CONCEPT 4: PLANNING PATTERN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What: Agent creates a plan before executing
Why: Better results for complex, multi-step tasks
How: Plan → Execute Steps → Synthesize

Planning Flow:
┌─────────────────────────────────────────────────────────────┐
│  Task                                                        │
│    ↓                                                         │
│  ┌──────────┐                                               │
│  │ Planner  │ Creates: [Step 1, Step 2, Step 3]            │
│  └──────────┘                                               │
│    ↓                                                         │
│  ┌──────────┐                                               │
│  │ Executor │ Executes each step sequentially              │
│  └──────────┘                                               │
│    ↓                                                         │
│  ┌──────────┐                                               │
│  │Synthesize│ Combines results into final answer           │
│  └──────────┘                                               │
└─────────────────────────────────────────────────────────────┘

Advantages:
  ✓ Breaks down complex tasks
  ✓ More organized execution
  ✓ Easier to debug and track progress
  ✓ Can replan if needed

Example Tasks:
  • Research projects
  • Multi-step calculations
  • System design tasks
  • Tutorial creation


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👤 CONCEPT 5: HUMAN-IN-THE-LOOP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What: Agent pauses for human approval or input
Why: Safety, compliance, and quality control
How: Use interrupts and checkpointing

HITL Flow:
┌─────────────────────────────────────────────────────────────┐
│  ┌──────────┐      ┌──────────┐      ┌──────────┐         │
│  │ Propose  │─────▶│  Human   │─────▶│ Execute  │         │
│  │ Action   │      │ Approval │      │ Action   │         │
│  └──────────┘      └──────────┘      └──────────┘         │
│                         │                                   │
│                         ▼ (rejected)                        │
│                    ┌──────────┐                            │
│                    │  Revise  │                            │
│                    └──────────┘                            │
└─────────────────────────────────────────────────────────────┘

Use Cases:
  • Destructive operations (delete, modify)
  • Financial transactions
  • Sending communications
  • Production deployments
  • Sensitive data access

Implementation:
  1. Agent proposes action
  2. Execution pauses (interrupt)
  3. Human reviews and approves/rejects
  4. Agent continues based on decision


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👥 CONCEPT 6: MULTI-AGENT SYSTEMS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What: Multiple specialized agents collaborate
Why: Divide complex tasks among experts
How: Supervisor pattern or peer-to-peer collaboration

Supervisor Pattern:
┌─────────────────────────────────────────────────────────────┐
│                    ┌────────────┐                           │
│                    │ Supervisor │                           │
│                    └────────────┘                           │
│                          │                                  │
│         ┌────────────────┼────────────────┐                │
│         ▼                ▼                ▼                │
│   ┌──────────┐    ┌──────────┐    ┌──────────┐           │
│   │Researcher│    │  Writer  │    │ Reviewer │           │
│   └──────────┘    └──────────┘    └──────────┘           │
└─────────────────────────────────────────────────────────────┘

Agent Roles:
  • Researcher: Gathers information
  • Writer: Creates content
  • Reviewer: Quality control
  • Supervisor: Coordinates workflow

Benefits:
  ✓ Specialization improves quality
  ✓ Parallel processing possible
  ✓ Clear separation of concerns
  ✓ Easier to test and maintain


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 CONCEPT 7: DEEP AGENTS (COMBINING ALL CONCEPTS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What: Agents that combine multiple advanced patterns
Why: Handle complex, real-world tasks effectively
How: Integrate planning, tools, reflection, and state

Deep Agent Architecture:
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│  ┌──────────┐                                               │
│  │  Planner │ Creates multi-step plan                      │
│  └──────────┘                                               │
│       ↓                                                      │
│  ┌──────────┐                                               │
│  │ Executor │ Uses tools, maintains state                  │
│  └──────────┘                                               │
│       ↓                                                      │
│  ┌──────────┐                                               │
│  │Reflector │ Evaluates quality, decides to replan        │
│  └──────────┘                                               │
│       ↓                                                      │
│  ┌──────────┐                                               │
│  │Synthesize│ Produces final output with confidence        │
│  └──────────┘                                               │
│                                                              │
└─────────────────────────────────────────────────────────────┘

Characteristics:
  ✓ Self-improving through reflection
  ✓ Strategic through planning
  ✓ Capable through tool use
  ✓ Reliable through state management
  ✓ Safe through human oversight
  ✓ Collaborative through multi-agent patterns

Real-World Applications:
  • Research assistants
  • Code generation and review
  • Content creation pipelines
  • Data analysis workflows
  • Customer service automation
  • DevOps automation


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 KEY DIFFERENCES: DEEP AGENTS VS SIMPLE CHATBOTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────┬──────────────────┬──────────────────────┐
│ Feature             │ Simple Chatbot   │ Deep Agent           │
├─────────────────────┼──────────────────┼──────────────────────┤
│ Memory              │ Basic context    │ Rich state tracking  │
│ Planning            │ None             │ Multi-step plans     │
│ Tool Use            │ Limited/None     │ Extensive            │
│ Self-Improvement    │ No               │ Reflection loops     │
│ Error Recovery      │ Minimal          │ Replanning, retry    │
│ Collaboration       │ Single agent     │ Multi-agent systems  │
│ Human Oversight     │ Rare             │ Built-in checkpoints │
│ Complexity Handling │ Simple queries   │ Complex workflows    │
└─────────────────────┴──────────────────┴──────────────────────┘


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📖 LEARNING PATH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Recommended order to study the examples:

1. 01_basic_agent.py
   └─ Learn: State, tools, graph structure

2. 02_stateful_agent.py
   └─ Learn: Persistence, checkpointing, memory

3. 03_reflection_agent.py
   └─ Learn: Self-improvement, quality control

4. 04_planning_agent.py
   └─ Learn: Task decomposition, sequential execution

5. 05_human_in_loop.py
   └─ Learn: Interrupts, approval workflows

6. 06_multi_agent_system.py
   └─ Learn: Agent collaboration, specialization

7. 07_advanced_deep_agent.py
   └─ Learn: Combining all patterns

Each example builds on concepts from previous ones!


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


def print_concepts():
    """Print all concepts"""
    print(CONCEPTS)


def print_concept(number: int):
    """Print a specific concept"""
    concept_map = {
        1: "STATE MANAGEMENT",
        2: "TOOL CALLING",
        3: "REFLECTION PATTERN",
        4: "PLANNING PATTERN",
        5: "HUMAN-IN-THE-LOOP",
        6: "MULTI-AGENT SYSTEMS",
        7: "DEEP AGENTS"
    }
    
    if number in concept_map:
        lines = CONCEPTS.split('\n')
        in_section = False
        for line in lines:
            if concept_map[number] in line:
                in_section = True
            elif in_section and line.startswith('━━━━') and concept_map[number] not in line:
                break
            
            if in_section:
                print(line)
    else:
        print(f"Concept {number} not found. Choose 1-7.")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        try:
            concept_num = int(sys.argv[1])
            print_concept(concept_num)
        except ValueError:
            print("Usage: python concepts_explained.py [1-7]")
            print("Or run without arguments to see all concepts")
    else:
        print_concepts()
