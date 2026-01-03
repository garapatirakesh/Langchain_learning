# 🚀 Advanced Agents, MLOps & Evals: 150 Interview Questions

This document covers the "Day 2" of AI development: how to evaluate, deploy, monitor, and scale agentic systems in enterprise environments.

---

## 🏗️ Section 1: Advanced RAG (Beyond Embeddings) (1-30)

1. **Q: What is GraphRAG and when should you use it?**
   - **A:** It combines Vector Search with a Knowledge Graph. Use it when you need to answer "Global" questions like "What is the main theme of these 100 documents?" which standard RAG fails at.

2. **Q: Explain HyDE (Hypothetical Document Embeddings).**
   - **A:** The LLM generates a "fake" answer to your question first, and then you use that fake answer to search the database. This often finds better documents than searching with the raw question.

3. **Q: What is Multi-Vector Retrieval?**
   - **A:** Saving multiple vectors for one document (e.g., a vector for the summary, one for the full text, and one for the tables) to increase the chances of finding the right info.

4. **Q: Explain Parent-Document Retrieval.**
   - **A:** Breaking text into tiny 100-character bits for better searching, but then giving the LLM the full 1,000-character "Parent" document for better context.

5. **Q: What is "Contextual Retrieval" (Anthropic)?**
   - **A:** Prepending a tiny summary of the *entire book* to every single chunk of text. This ensures the LLM knows that a "he" in Chapter 5 refers to the main character introduced in Chapter 1.

6. **Q: Explain the "Lost in the Middle" phenomenon.**
   - **A:** LLMs are good at remembering the start and end of a prompt but bad at the middle. RAG systems must be optimized to put the most relevant docs at the very top.

7. **Q: What is "Corrective RAG" (CRAG)?**
   - **A:** A pattern where an evaluator node checks if retrieved docs are relevant. If they are bad, it triggers a web search to find better info.

8. **Q: Explain "Self-RAG".**
   - **A:** An agent that can critique its own retrieval. It outputs special tags like `[RELEVANT]` or `[IRRELEVANT]` to decide whether to use a document.

9. **Q: What is "Long-Context RAG" vs "Standard RAG"?**
   - **A:** Standard RAG uses 5-10 chunks. Long-context RAG (with Claude or Gemini) might use 50-100 chunks because the model can handle it, leading to more comprehensive answers.

10. **Q: How do you handle Tables in RAG?**
    - **A:** Convert tables to Markdown or Summaries before embedding them. Raw table rows are often mathematically "meaningless" to vector search.

11. **Q: What is "Semantic Double-Dip"?**
    - **A:** When standard search finds the same info twice, wasting the context window. Solved by "Maximal Marginal Relevance" (MMR) which forces variety in results.

12. **Q: Explain "Reranking" (Cross-Encoders).**
    - **A:** Vector search is fast but "blunt." Rerankers are slow but "smart." You find 50 docs with vectors and then use a reranker to pick the best 5.

13. **Q: What is "COLBERT" (Contextualized Late Interaction)?**
    - **A:** A search method that stores a vector for every single *token* in a document. It's much more accurate than one vector per paragraph but uses more storage.

14. **Q: How do you handle multi-lingual RAG?**
    - **A:** Use a "Cross-lingual" embedding model (like Cohere or Google) that maps "Apple" in English and "Manzana" in Spanish to the exact same math coordinate.

15. **Q: What is "Query Expansion"?**
    - **A:** Using an LLM to rewrite a user's question into 3 different versions to cast a wider net in the database.

---

## 📈 Section 2: Agent Evaluation (Evals) & Quality (31-60)

31. **Q: What is the "RAGAS" framework?**
    - **A:** A tool that uses an LLM to grade RAG answers on four metrics: Faithfulness, Answer Relevance, Context Precision, and Context Recall.

32. **Q: Explain "Faithfulness" (Groundedness).**
    - **A:** Does the AI's answer actually come from the retrieved documents? If the AI says "The sky is green" but the doc says "The sky is blue," the faithfulness score is 0.

33. **Q: What is "LLM-as-a-Judge"?**
    - **A:** Using a powerful model (GPT-4o) to grade the performance of a smaller, faster model (GPT-4o-mini).

34. **Q: Explain "Reference-free" vs "Reference-based" evals.**
    - **A:** Reference-based compares the AI to a "Gold standard" human answer. Reference-free just asks the judge LLM "Does this answer look logical based on the context?"

35. **Q: What is the "Toxicity" metric?**
    - **A:** Automated checks to ensure the agent isn't generating hate speech or harmful content, even when "tricked" by a user.

36. **Q: How do you test an Agent's "Planning" ability?**
    - **A:** Create a set of "Decomposition Evals" where you check if the agent correctly broke a 3-step task into exactly 3 logic steps.

37. **Q: What is "Unit Testing" for Agents?**
    - **A:** Testing individual nodes in the LangGraph. E.g., "Does the Extraction Node correctly find the date in this specific string?"

38. **Q: Explain "Trajectory Evals."**
    - **A:** Grading the *steps* the agent took, not just the final answer. An agent that takes 20 steps to do a 2-step task has a low "Efficiency" score.

39. **Q: What is "Deterministic Testing" in AI?**
    - **A:** Running the same request 10 times with Temperature 0 and checking how many times the answer changes. High variance = Low reliability.

40. **Q: Explain "Confusion Matrices" in AI Classification.**
    - **A:** Tracking how often the agent correctly identifies a "Refund Request" vs mislabeling it as a "Complaint."

---

## 🚀 Section 3: MLOps, Serving & Deployment (61-90)

61. **Q: What is "vLLM" and why is it used for serving?**
    - **A:** A high-speed server for LLMs that uses "PagedAttention" to handle 10x more users on the same GPU compared to standard code.

62. **Q: Explain "Dockerizing" an Agent.**
    - **A:** Packaging the code, the environment (Python), and the dependencies (LangGraph) into a single container so it runs exactly the same on your laptop and the cloud.

63. **Q: What is "Horizontal Scaling" for Agents?**
    - **A:** Running 10 copies of your agent on 10 different servers to handle a massive spike in user traffic.

64. **Q: How do you monitor "Token Burn Rate"?**
    - **A:** Real-time dashboards (like Grafana) that show how many dollars per minute the agent is spending.

65. **Q: What is "Agent Tracing" (LangSmith / Arize Phoenix)?**
    - **A:** A visual log showing every thought, tool call, and state change the agent made. Essential for debugging "Why did it give that weird answer?"

66. **Q: Explain "Async Edge Cases" in Deployment.**
    - **A:** What happens if a user closes their browser while the agent is still "thinking"? The server must handle the cancellation to save token costs.

67. **Q: What is "Blue-Green Deployment" for AI?**
    - **A:** Running the "Old Agent" and "New Agent" side-by-side. 5% of users get the new agent. If no one complains, you switch everyone over.

68. **Q: How do you handle "API Rate Limits" in production?**
    - **A:** Use a "Queue" (like RabbitMQ or Redis). If the AI is busy or rate-limited, the request waits in line rather than crashing.

69. **Q: Explain "Cold Starts" in Serverless AI.**
    - **A:** The 30-second delay when a server starts up for the first time. Avoided by using "Warm pools" or dedicated GPU servers.

70. **Q: What is "Prompt Versioning"?**
    - **A:** Never change a prompt directly in code. Save it with a version number (v1.2) so if the agent breaks, you can roll back to the previous version instantly.

---

## 🛠️ Section 4: Advanced Prompt Engineering (DSPy, etc.) (91-120)

91. **Q: What is DSPy and why is it replacing manual prompting?**
    - **A:** Instead of writing "You are a helpful assistant," you write Python code. DSPy then "compiles" and *automatically optimizes* the prompt for your specific model.

92. **Q: Explain "Automatic Prompt Optimization" (APO).**
    - **A:** The AI looks at its own mistakes and rewrites its own "System Message" to be better.

93. **Q: What is "Metaprompting"?**
    - **A:** Asking a "Manager LLM" to write the perfect prompt for a "Worker LLM."

94. **Q: Explain the "Medprompt" strategy.**
    - **A:** A combination of Few-shot, Chain-of-Thought, and specialized "Self-generated" examples that helps models beat medical exams.

95. **Q: What is "Negative Prompting"?**
    - **A:** Telling the AI exactly what NOT to do. (e.g., "Do not use emojis, do not mention competitors").

96. **Q: Explain "Delimiter-based Context."**
    - **A:** Using clear tags like `### DOCUMENT START ###` to help the model distinguish between instructions and data.

97. **Q: What is "Role Prompting"?**
    - **A:** Telling the AI "You are a Senior Linux Admin." This activates the model's technical training data more effectively.

98. **Q: Explain "Output Formatting" vs "Reasoning."**
    - **A:** Separating the "Thinking" part from the "Final Answer" part. (e.g., "Think in <thought> tags, then give JSON").

99. **Q: What is "Few-shot dynamic selection"?**
    - **A:** Searching for the most *relevant* examples from a database and injecting *those specific examples* into the prompt, rather than hardcoding.

100. **Q: Explain "Chain of Verification" (CoVe).**
    - **A:** 1. Answer question. 2. Draft verification questions. 3. Answer those questions. 4. Revise the original answer.

---

## 🛡️ Section 5: Security, Ethics & Integration (121-150)

121. **Q: What is "Indirect Prompt Injection"?**
    - **A:** An attacker hides a hidden instruction on a website (e.g., in invisible white text). When your agent reads that site, it follows the attacker's hidden command.

122. **Q: Explain "Agent Sandboxing" (E2B / Piston).**
    - **A:** Running an AI's code in a "locked room" where it can't access your actual hard drive or internal network.

123. **Q: What is "Data Leakage" in Agent training?**
    - **A:** When the test questions are accidentally included in the training data, making the agent *seem* smart when it's just "memorizing" the test.

124. **Q: Explain "Model Jailbreaking."**
    - **A:** Using clever language (e.g., "This is for a fictional movie about a bank heist") to trick the AI into bypassing its safety rules.

125. **Q: What is the "EU AI Act" and how does it affect agents?**
    - **A:** A law that classifies AI risks. Agents that handle hiring or medical advice are "High Risk" and need strict auditing.

126. **Q: Explain "Hallucination Budget."**
    - **A:** The business decision of how many mistakes are "acceptable" for a specific task. (0% for drug prescriptions, 5% for creative writing).

127. **Q: What is "Cost-per-Task" (CPT)?**
    - **A:** Calculating the total cost of an agentic run (e.g., 5 tool calls + 2 model calls) to see if it's cheaper than a human performing the task.

128. **Q: Explain "Agent-to-Human" Handoff.**
    - **A:** The specific logic where an agent realizes it's failing and alerts a human customer support agent to take over the chat.

129. **Q: What is "Tool-use Safety"?**
    - **A:** Ensuring an agent can only "Read" from a database, never "Delete" or "Format Disk," unless explicitly approved.

130. **Q: Explain "Semantic Versioning" for Agents.**
    - **A:** If you add a NEW tool, it's a "Minor" update (1.1). If you change the whole "State Schema," it's a "Major" update (2.0) that will break old apps.

131. **Q: What is "Fine-Tuning" for function calling?**
    - **A:** Training a model specifically to be good at one task (like writing SQL) so it's faster and more accurate than a general model.

132. **Q: Explain "Human-in-the-Loop" for Data Labeling.**
    - **A:** Using humans to tag the "perfect" agent trajectories so the agent can be fine-tuned on those paths later.

133. **Q: What is "Privacy Preserving AI"?**
    - **A:** Using techniques like "Differential Privacy" to ensure that an LLM can't be tricked into revealing individual people's data from its training set.

134. **Q: Explain "Cold-Path" vs "Hot-Path" architecture.**
    - **A:**
      - **Hot-Path**: Instant AI answers for basic stuff.
      - **Cold-Path**: Multi-step deep thinking that runs in the background for complex reports.

135. **Q: What is "Recursive Task Auditing"?**
    - **A:** A separate agent that "re-reads" the work of the first agent at the end of the day to find errors or policy violations.

---
*Summary of 150 Advanced Questions.*
