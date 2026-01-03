import os
from typing import TypedDict, Optional, List
from dotenv import load_dotenv

# LangGraph & LangChain imports
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Import our Pydantic models from the modules folder
from modules.job import Job
from modules.resume import Resume

# Load environment variables
load_dotenv()

# Define the State of our Graph
# This is the "memory" of our agent that gets passed between nodes
class AgentState(TypedDict):
    raw_job_text: str
    raw_resume_text: str
    structured_job: Optional[Job]
    structured_resume: Optional[Resume]
    fit_analysis: Optional[str]

# Create our LLM with Structured Output capability
# We use gpt-4o-mini as a smart, low-cost model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# --- Define the Nodes (The "Workers" of our Graph) ---

def extraction_node(state: AgentState):
    """
    This node takes raw text and uses the LLM to 'extract' data 
    into our structured Job and Resume Pydantic models.
    """
    print("\n--- NODE: EXTRACTOR ---")
    
    # 1. Extract Job Data
    job_extractor = llm.with_structured_output(Job)
    job_data = job_extractor.invoke([
        HumanMessage(content=f"Extract structured job information from this text: {state['raw_job_text']}")
    ])
    
    # 2. Extract Resume Data
    resume_extractor = llm.with_structured_output(Resume)
    resume_data = resume_extractor.invoke([
        HumanMessage(content=f"Extract structured resume information from this text: {state['raw_resume_text']}")
    ])
    
    print(f"Successfully extracted Job: {job_data.title} at {job_data.company}")
    print(f"Successfully extracted Resume for: {resume_data.name}")
    
    # Return updates to the state
    return {
        "structured_job": job_data, 
        "structured_resume": resume_data
    }

def matcher_node(state: AgentState):
    """
    This node compares the structured job and resume to see if there's a match.
    """
    print("\n--- NODE: MATCHER ---")
    job = state["structured_job"]
    resume = state["structured_resume"]
    
    # We ask the LLM to behave as a Career Expert to compare them
    prompt = f"""
    Compare this Candidate with the Job Description.
    
    CANDIDATE: {resume.name}
    SKILLS: {', '.join(resume.skills)}
    SUMMARY: {resume.professional_summary}
    
    JOB: {job.title} at {job.company}
    REQUIREMENTS: {', '.join(job.requirements)}
    
    Task: Provide a 3-bullet point 'Fit Analysis':
    1. Overall Match Score (0-100)
    2. Top 2 Matching Skills
    3. Top 1 Missing Skill/Gap
    """
    
    analysis = llm.invoke(prompt).content
    
    print("Match Analysis Complete.")
    return {"fit_analysis": analysis}

# --- Build the Graph ---

# 1. Initialize the Graph Builder with our state type
workflow = StateGraph(AgentState)

# 2. Add our nodes to the graph
workflow.add_node("extractor", extraction_node)
workflow.add_node("matcher", matcher_node)

# 3. Define the edges (The "Paths")
workflow.add_edge(START, "extractor")   # Start at extractor
workflow.add_edge("extractor", "matcher") # Then go to matcher
workflow.add_edge("matcher", END)        # Then finish

# 4. Compile the Graph into a runnable Application
app = workflow.compile()

# --- Run the Demo ---

if __name__ == "__main__":
    # Sample Raw Text (In a real app, this comes from PDFs or Job Boards)
    raw_job = """
    We are hiring a Senior Python Developer at OpenAI. 
    You need 5+ years of Python experience, familiarity with LangGraph, 
    and experience building AI Agents. Location: San Francisco.
    Salary: $200k. Benefits include health insurance and 401k.
    """
    
    # We can use our mock() data for the resume part if we want, 
    # but here we'll use raw text to show the extractor in action.
    raw_resume = """
    Rakesh Kumar. Professional Summary: AI Engineer with 6 years of coding. 
    Expert in Python, LangChain, and React. I have built several agentic workflows 
    using LangGraph and OpenAI. Based in India, looking for remote roles.
    """

    print("🚀 Starting LangGraph Job Matcher...")
    
    # Invoke the app with initial state
    final_output = app.invoke({
        "raw_job_text": raw_job,
        "raw_resume_text": raw_resume
    })

    print("\n" + "="*50)
    print("🎯 FINAL MATCH ANALYSIS")
    print("="*50)
    print(f"JOb: {final_output['structured_job'].title} @ {final_output['structured_job'].company}")
    print(f"Candidate: {final_output['structured_resume'].name}")
    print("-" * 30)
    print(final_output['fit_analysis'])
    print("="*50)
