# Title
title = doc.add_heading('Understanding the A2A Protocol Architecture', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Intro
p = doc.add_paragraph('While the code is a simulation (because A2A is usually handled by a transport layer like HTTPS or Stdio), it implements the exact architectural markers of the A2A protocol.')

doc.add_paragraph('Here is why this code "is" the A2A protocol:')

# 1. Agent Card
doc.add_heading('1. The "Agent Card" (Discovery)', level=1)
doc.add_paragraph('In a normal function call, you just call the function. In A2A, you must first discover what an agent can do.')
doc.add_paragraph('In the code: get_agent_card() returns a JSON object.', style='Quote')
doc.add_paragraph('A2A Marker: This is the industry-standard "Discovery" phase. An agent must advertise its capabilities and role so other agents can decide whether to hire it.')

# 2. JSON-RPC 2.0
doc.add_heading('2. JSON-RPC 2.0 Messaging', level=1)
doc.add_paragraph('A2A doesn\'t use "free text" for communication between the agent brains; it uses JSON-RPC 2.0.')

code_block = doc.add_paragraph()
run = code_block.add_run('{\n  "jsonrpc": "2.0",\n  "method": "create_task",\n  "id": 1,\n  "params": { ... }\n}')
run.font.name = 'Courier New'
run.font.size = Pt(10)

doc.add_paragraph('A2A Marker: Every request has a unique id and a specific method. This allows for Asynchronous tasks—the manager can send 10 tasks and know which response belongs to which task when they come back later.')

# 3. Task-Based Handoff
doc.add_heading('3. Task-Based Handoff (Not just Chat)', level=1)
doc.add_paragraph('In a simple chatbot, you just talk. In A2A, you create a Task.')
doc.add_paragraph('In the code: We use the method create_task.', style='Quote')
doc.add_paragraph('A2A Marker: A2A agents have a "Task Lifecycle." A task isn\'t just a message; it’s an object that can have a status (like in-progress or completed).')

# 4. Artifact Concept
doc.add_heading('4. The "Artifact" Concept', level=1)
doc.add_paragraph('In a standard script, a function returns a string. In A2A, an agent returns an Artifact.')

code_block2 = doc.add_paragraph()
run2 = code_block2.add_run('"artifacts": [{"name": "risk_report.txt", "content": answer}]')
run2.font.name = 'Courier New'
run2.font.size = Pt(10)

doc.add_paragraph('A2A Marker: Artifacts are the "output" of the protocol. They are structured objects that include metadata (filename, mime-type, size) so the receiving agent knows exactly how to handle the data (e.g., save it to a file or run it as code).')

# 5. Opacity
doc.add_heading('5. Architectural Opacity', level=1)
doc.add_paragraph('In the code: The Chaos-Bot (Manager) calls the Grumpy-GPT (Provider).')
doc.add_paragraph('A2A Marker: Chaos-Bot has no idea that Grumpy-GPT is using OpenAI. Grumpy-GPT could be using a team of humans, a local llama model, or a simple database lookup. This "Opacity" is a core pillar of A2A—it allows different companies to let their agents talk without giving away their secret internal tools.')

# Summary
doc.add_heading('Summary for the Class', level=1)
doc.add_paragraph('If you just did print(open_ai_call()), that\'s an API call. Because we wrapped it in an Agent Card, a JSON-RPC Wrapper, and an Artifact Output, it becomes A2A Protocol.')
doc.add_paragraph('It transforms a "Single Script" into a "Multi-Agent System."')

doc.save('A2A_Protocol_Explanation.docx')
print("Document created successfully.")