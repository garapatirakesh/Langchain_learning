import os
from typing import TypedDict, Optional, List
from dotenv import load_dotenv

# LangGraph & LangChain imports
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Import our Pydantic models from our local modules folder
from modules.job import Job
from modules.resume import Resume

# Load environment variables (API Key etc.)
load_dotenv()

# ==========================================
# 1. DEFINE THE STATE
# ==========================================
class AgentState(TypedDict):
    # Inputs
    raw_job_text: str
    raw_resume_text: str
    
    # Processed Data
    structured_job: Optional[Job]
    structured_resume: Optional[Resume]
    
    # Analysis Reports
    fit_analysis: Optional[str]
    gap_analysis_report: Optional[str]
    
    # Final Action results
    notification_status: Optional[str]

# Create our LLM instance
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# ==========================================
# 2. DEFINE THE NODES (THE WORKERS)
# ==========================================

def extraction_node(state: AgentState):
    """
    Worker 1: Extracts structured data from messy text.
    Uses Pydantic models for guaranteed schema.
    """
    print("\n[Node] 🔍 EXTRACTOR: Converting raw text to objects...")
    
    # Extract Job
    job_extractor = llm.with_structured_output(Job)
    job_data = job_extractor.invoke(f"Extract job: {state['raw_job_text']}")
    
    # Extract Resume
    resume_extractor = llm.with_structured_output(Resume)
    resume_data = resume_extractor.invoke(f"Extract resume: {state['raw_resume_text']}")
    
    print(f" -> Found Job: {job_data.title}")
    print(f" -> Found Candidate: {resume_data.name}")
    
    return {
        "structured_job": job_data,
        "structured_resume": resume_data
    }

def matcher_node(state: AgentState):
    """
    Worker 2: Analyzes fit between candidate and job.
    """
    print("\n[Node] ⚖️ MATCHER: Analyzing Fit Score...")
    job = state["structured_job"]
    resume = state["structured_resume"]
    
    prompt = f"""
    Act as a HR Specialist. Compare this Candidate to the Job.
    
    CANDIDATE: {resume.name}, Summary: {resume.professional_summary}
    JOB: {job.title}, Requirements: {job.requirements}
    
    Provide:
    1. A Match Percentage (0-100%).
    2. A brief 'Decision Reasoning'.
    """
    
    analysis = llm.invoke(prompt).content
    print(" -> Fit analysis completed.")
    return {"fit_analysis": analysis}

def gap_analysis_node(state: AgentState):
    """
    Worker 3: Identifies missing skills and suggests learning paths.
    """
    print("\n[Node] 🎓 GAP ANALYSIS: Identifying missing skills & courses...")
    job = state["structured_job"]
    resume = state["structured_resume"]
    
    prompt = f"""
    Based on the following Job Requirements and Candidate Skills, 
    identify 3 CRITICAL SKILLS the candidate is missing.
    For each missing skill, suggest a specific course name or certification.
    
    JOB REQUIREMENTS: {job.requirements}
    CANDIDATE SKILLS: {resume.skills}
    
    Format output as:
    Skill 1: [Skill] - Recommended: [Course/Cert]
    ...
    """
    
    gap_report = llm.invoke(prompt).content
    print(" -> Gap report generated sample suggestions.")
    return {"gap_analysis_report": gap_report}

def notification_node(state: AgentState):
    """
    Worker 4: Simulates sending a final notification to the user.
    """
    print("\n[Node] 📧 NOTIFIER: Sending email notification...")
    
    report = f"""
    TO: {state['structured_resume'].name}
    SUBJECT: Your Resume Analysis for {state['structured_job'].title}
    
    {state['fit_analysis']}
    
    --- SUGGESTED IMPROVEMENTS ---
    {state['gap_analysis_report']}
    """
    
    # In a real app, you'd use SendGrid/SMTP here. 
    # For this demo, we just record that it 'sent'.
    status = f"Successfully notified {state['structured_resume'].name}. Length: {len(report)} chars."
    
    print(f" -> {status}")
    return {"notification_status": status}

# ==========================================
# 3. CONSTRUCT THE GRAPH
# ==========================================

workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("extractor", extraction_node)
workflow.add_node("matcher", matcher_node)
workflow.add_node("gap_analyzer", gap_analysis_node)
workflow.add_node("notifier", notification_node)

# Add Edges (Linear Flow for this analysis)
workflow.add_edge(START, "extractor")
workflow.add_edge("extractor", "matcher")
workflow.add_edge("matcher", "gap_analyzer")
workflow.add_edge("gap_analyzer", "notifier")
workflow.add_edge("notifier", END)

# Compile
app = workflow.compile()

# ==========================================
# 4. EXECUTE DEMO
# ==========================================

if __name__ == "__main__":
    job_txt = """
    Job: Senior Cloud Architect @ Google. 
    Salary: $250k. 
    Requirements: 10+ years Python, AWS Mastery, Kubernetes, 
    Experience with Terraform and GCP is a massive plus.
    """
    
    resume_txt = """
    Name: Alex Rivera. 
    Summary: Cloud developer with 7 years experience. 
    Skills: Python, AWS (Certified), Docker, Jenkins. 
    I have built microservices but haven't worked much with Terraform or GCP.
    """

    print("🚀 INITIALIZING DEEP RESUME ANALYZER...")
    
    final_state = app.invoke({
        "raw_job_text": job_txt,
        "raw_resume_text": resume_txt
    })
    
    print("\n" + "="*60)
    print("📊 FINAL AGENT REPORT SUMMARY")
    print("="*60)
    print(f"STATUS: {final_state['notification_status']}")
    print("\n--- FIT ANALYSIS ---")
    print(final_state['fit_analysis'])
    print("\n--- GAP ANALYSIS & COURSE SUGGESTIONS ---")
    print(final_state['gap_analysis_report'])
    print("="*60)
