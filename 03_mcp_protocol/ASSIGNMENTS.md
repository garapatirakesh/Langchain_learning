# Model Context Protocol (MCP) Assignments

## Objective
Understand the architecture of the Model Context Protocol by building servers and clients.

## Prerequisite Knowledge
- Client-Server architecture basics
- JSON-RPC idea
- Python AsyncIO

## Practical Assignments

### Assignment 1: Basic Math Server
**Goal:** Create a simple MCP server that exposes tools.
**Task:**
1.  Use the `mcp` python package or the raw implementation guide.
2.  Initialize a Server instance.
3.  Register a tool `calculate_sum` that takes a list of numbers and returns the sum.
4.  Register a tool `calculate_product`.
5.  Run the server (over stdio is standard for MCP).
**Test:** Verify it works by running it and manually inputting a JSON-RPC request (or creating a dummy client script).

### Assignment 2: Resource Server
**Goal:** Expose data as Resources.
**Task:**
1.  Create a folder `my_data` with a few `.txt` files.
2.  Create a new MCP server.
3.  Implement the `list_resources` capability: it should scan the folder and return the list of files as URIs (e.g., `file:///path/to/my_data/file1.txt`).
4.  Implement the `read_resource` capability: Given a URI, return the file content.

### Assignment 3: Prompts Server
**Goal:** Expose reusable prompts.
**Task:**
1.  Add a `get_prompt` capability to your server.
2.  Define a prompt named `summarize_notes`.
3.  When called, it should return a prompt template structure with arguments (e.g., "Summarize the following notes: {notes}").

### Assignment 4: The Client (Optional but Recommended)
**Goal:** Connect an LLM to your server.
**Task:**
1.  Write a script that uses `mcp.ClientSession`.
2.  Connect to your Math Server via stdio.
3.  List available tools.
4.  Call the `calculate_sum` tool programmatically.

## Conceptual Quiz
1.  What are the three main primitives of MCP (Tools, ...)?
2.  Why does MCP typically use Stdio for transport?
3.  How does the "sampling" feature in MCP allow the server to ask the client/LLM for completions?
