# LangGraph Deep Agents Assignments

## Objective
Implement hierarchical and complex multi-agent systems using LangGraph's advanced features.

## Prerequisite Knowledge
- LangGraph Basics
- Deep Agents Concepts
- Notebook `00_concepts_deepagents.md`

## Practical Assignments

### Assignment 1: The Supervisor
**Goal:** effective routing between workers.
**Task:**
1.  Workers: Create 2 simple nodes/agents: `coder` (returns mocked code) and `reviewer` (returns mocked review).
2.  Supervisor: Create a node `supervisor` that uses an LLM to decide "Who should act next?".
3.  Output mapping: The LLM output should map to the node names `coder` or `reviewer` or `FINISH`.
4.  Graph: Connect Supervisor -> (Coder, Reviewer). Connect (Coder, Reviewer) -> Supervisor.

### Assignment 2: Hierarchical Teams
**Goal:** Graph within a Graph.
**Task:**
1.  Create a "Docs Team" graph (contains `outline_writer` -> `content_writer`). compile it.
2.  Create a "Code Team" graph (contains `programmer` -> `tester`). compile it.
3.  Create a Top-Level Graph. Nodes are `docs_team` and `code_team`.
4.  Note: Treat the compiled subgraphs as nodes in the parent graph.

## Conceptual Quiz
1.  How does state bubble up from a Subgraph to a Parent Graph?
2.  What is the benefit of a "Flat" multi-agent structure vs a "Hierarchical" one?
3.  How do we handle shared memory between independent teams?
