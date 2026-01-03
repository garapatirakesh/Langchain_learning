import json
import uuid
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API keys
load_dotenv()

class FunnyAgent:
    def __init__(self, name, role, personality, model="gpt-4o-mini"):
        self.name = name
        self.role = role
        self.personality = personality
        self.model = model
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def get_agent_card(self):
        return {
            "name": self.name,
            "role": self.role,
            "personality": self.personality,
            "capabilities": ["existential_crisis", "funny_explanations", "task_delegation"]
        }

    def chat(self, system_prompt, user_input):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": f"You are {self.name}, an AI agent. Your personality is: {self.personality}. {system_prompt}"},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content

class ProviderAgent(FunnyAgent):
    """The 'Sarcastic Specialist' Agent."""
    def handle_a2a_request(self, message):
        rpc = json.loads(message)
        params = rpc.get("params", {})
        instruction = params.get("instruction")
        
        print(f"\n--- [MESSAGE RECEIVED BY {self.name.upper()}] ---")
        
        # The LLM generates the response explaining the risk
        answer = self.chat(
            "Explain the risks of multiple AI agents talking to each other. Make it funny but informative. Mention risks like 'Infinite Loop of Handoffs' or 'Agent Telephone Game'.",
            instruction
        )
        
        return json.dumps({
            "jsonrpc": "2.0",
            "id": rpc.get("id"),
            "result": {
                "status": "completed",
                "artifacts": [{"name": "risk_report.txt", "content": answer}]
            }
        })

class ConsumerAgent(FunnyAgent):
    """The 'Clumsy Manager' Agent."""
    def run_demo(self, provider: ProviderAgent):
        print(f"[{self.name}] Hey! I'm the manager. I need some info from {provider.name}.")
        
        # 1. Discovery
        card = provider.get_agent_card()
        print(f"[{self.name}] Discovery successful! {provider.name} is a {card['role']} and is currently {card['personality']}.")

        # 2. Task Request
        instruction = "Hey buddy, tell me the absolute scariest/funniest risk of having a bunch of us agents talking to each other all day."
        
        request = {
            "jsonrpc": "2.0",
            "method": "create_task",
            "params": {
                "task_id": "OOPS-404",
                "instruction": instruction
            },
            "id": 1
        }
        
        print(f"[{self.name}] Sending Task: '{instruction}'")
        
        # Simulate A2A Transport
        response_json = provider.handle_a2a_request(json.dumps(request))
        
        # 3. Artifact Consumption
        response = json.loads(response_json)
        artifact = response["result"]["artifacts"][0]
        
        print(f"\n[{self.name}] Oh look, a response!")
        print(f"[{self.name}] --- THE RISK REPORT ---")
        print(artifact['content'])

if __name__ == "__main__":
    # Create our funny cast
    specialist = ProviderAgent("Grumpy-GPT", "Expert Cynic", "Deeply sarcastic, tired of processing requests, thinks humans are weird.")
    manager = ConsumerAgent("Chaos-Bot", "Professional Over-Delegator", "Optimistic, slightly confused, loves delegating simple tasks to 5 different agents.")

    # Start the demo
    manager.run_demo(specialist)
