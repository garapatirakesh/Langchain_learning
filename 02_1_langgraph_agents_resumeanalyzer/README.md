# 02_1 LangGraph Resume & Gap Analyzer Agent

This module demonstrates a multi-node LangGraph agent designed to process messy job and resume text, perform a fit analysis, identify skill gaps, and simulate a final notification.

## 🏗️ Agent Architecture

The agent consists of 4 specialized nodes connected in a sequential pipeline:

1. **🔍 Extractor Node**: 
   - Uses `llm.with_structured_output` with your **Job** and **Resume** Pydantic models.
   - Cleans raw text into validated Python objects.
2. **⚖️ Matcher Node**: 
   - Compares the structured candidate data against the job requirements.
   - Generates a Match Score and Decision Reasoning.
3. **🎓 Gap Analysis Node**: 
   - Identifies specific missing skills (e.g., Terraform, GCP).
   - Dynamically suggests specific courses or certifications to fill those gaps.
4. **📧 Notification Node**: 
   - Simulates the final action of emailing the candidate their personalized report.

## 📁 Folder Structure

```
02_1_langgraph_agents_resumeanalyzer/
├── modules/
│   ├── job.py      <- Pydantic Model for Jobs
│   └── resume.py   <- Pydantic Model for Resumes
├── resume_analyzer_agent.py  <- The main LangGraph Logic
└── README.md
```

## 🚀 How to Run

1. Navigate to this directory.
2. Ensure your `.env` file (with `OPENAI_API_KEY`) is in the parent directory.
3. Run the agent:

```powershell
python resume_analyzer_agent.py
```

## 💡 Concepts Demonstrated

- **State Management**: Using `TypedDict` to pass complex objects (`Job`, `Resume`) between workers.
- **Task Decomposition**: Breaking a complex "HR Process" into 4 simple, testable functions.
- **LLM as a Tool**: Using the LLM for different roles (Data Cleaner, HR Specialist, Career Advisor).
- **Final Action**: Moving from "Thinking" (Analysis) to "Doing" (Notification).
