import json
import uuid
import time
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()

class A2AAgent:
    """Base A2A Agent class to handle standard message formatting."""
    def __init__(self, name, capabilities):
        self.name = name
        self.capabilities = capabilities
        
    def get_agent_card(self):
        """Standard A2A 'Agent Card' discovery."""
        return {
            "name": self.name,
            "capabilities": self.capabilities,
            "protocol_version": "2024-05-01",
            "status": "available"
        }

class ResearcherAgent(A2AAgent):
    """The 'Provider' agent that performs specialized tasks using an LLM."""
    def __init__(self, name, capabilities):
        super().__init__(name, capabilities)
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def handle_request(self, message):
        rpc = json.loads(message)
        method = rpc.get("method")
        params = rpc.get("params", {})
        
        if method == "create_task":
            task_id = params.get("task_id")
            instruction = params.get("instruction")
            print(f"[{self.name}] Received Task {task_id}: '{instruction}'")
            print(f"[{self.name}] Consultng LLM for response...")
            
            try:
                # Use OpenAI to generate the response content
                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a professional researcher agent acting in an A2A (Agent-to-Agent) protocol environment. Provide concise, accurate responses."},
                        {"role": "user", "content": instruction}
                    ]
                )
                answer = response.choices[0].message.content
            except Exception as e:
                answer = f"Error consulting LLM: {str(e)}"

            # Return an A2A Artifact
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc.get("id"),
                "result": {
                    "status": "completed",
                    "artifacts": [
                        {
                            "name": "analysis_result.json",
                            "type": "application/json",
                            "content": {"summary": answer}
                        }
                    ]
                }
            })

class ManagerAgent(A2AAgent):
    """The 'Consumer' agent that orchestrates the workflow."""
    def run_demo(self, provider: ResearcherAgent):
        # 1. DISCOVERY PHASE
        print(f"[{self.name}] Discovering provider capabilities...")
        card = provider.get_agent_card()
        print(f"[{self.name}] Found: {card['name']} (Expert in: {card['capabilities']})\n")
        
        if "research" in card["capabilities"]:
            # 2. TASK DELEGATION PHASE
            task_id = str(uuid.uuid4())[:8]
            
            # The Manager decides on a complex question
            instruction = "Explain the fundamental difference between MCP and A2A protocols for AI agents."
            
            request = {
                "jsonrpc": "2.0",
                "method": "create_task",
                "params": {
                    "task_id": task_id,
                    "instruction": instruction
                },
                "id": 1
            }
            
            print(f"[{self.name}] Sending A2A Task Request: '{instruction}'")
            response_json = provider.handle_request(json.dumps(request))
            
            # 3. ARTIFACT CONSUMPTION PHASE
            response = json.loads(response_json)
            artifact = response["result"]["artifacts"][0]
            print(f"\n[{self.name}] Received Artifact Response for Task {task_id}")
            print(f"[{self.name}] --- FINAL ANALYSIS ---")
            print(artifact['content']['summary'])

if __name__ == "__main__":
    # Initialize the agents
    researcher = ResearcherAgent("Researcher-Bot", ["research", "summarization"])
    manager = ManagerAgent("Manager-Bot", ["orchestration"])
    
    # Execute the A2A handshake
    manager.run_demo(researcher)
