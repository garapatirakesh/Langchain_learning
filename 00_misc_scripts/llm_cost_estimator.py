import tiktoken

def estimate_cost(model_name, prompt):
    # Prices per 1M tokens (Approximate values)
    pricing = {
        "gpt-4o": {"input": 5.00, "output": 15.00},
        "gpt-4o-mini": {"input": 0.15, "output": 0.60}
    }
    
    encoding = tiktoken.encoding_for_model(model_name)
    tokens = len(encoding.encode(prompt))
    
    if model_name in pricing:
        price_per_1k = pricing[model_name]["input"] / 1000 # Cost for 1k tokens
        total_cost = (tokens / 1_000_000) * pricing[model_name]["input"]
        
        print(f"--- Cost Estimate for {model_name} ---")
        print(f"Tokens: {tokens}")
        print(f"Estimated Input Cost: ${total_cost:8f}")
        return total_cost
    else:
        print("Model pricing not found.")
        return 0

if __name__ == "__main__":
    p = "Explain the history of the internet in great detail. I need at least 5 paragraphs."
    estimate_cost("gpt-4o", p)
    estimate_cost("gpt-4o-mini", p)
