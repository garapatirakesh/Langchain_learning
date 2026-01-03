import tiktoken

def demo_tokenization():
    print("--- Tokenization with Tiktoken ---")
    
    # OpenAI context windows are measured in tokens, not words.
    encoding = tiktoken.encoding_for_model("gpt-4o")
    
    text = "Tiktoken is great because it helps us understand context limits!"
    tokens = encoding.encode(text)
    
    print(f"Text: '{text}'")
    print(f"Token IDs: {tokens}")
    print(f"Token Count: {len(tokens)}")
    print(f"Word Count: {len(text.split())}")
    
    print("\nIndividual tokens decoded:")
    for t in tokens:
        print(f"ID {t} -> '{encoding.decode([t])}'")

    # Example of a large text hitting context limit (explanation)
    max_tokens = 128000 # GPT-4o
    print(f"\nMax capacity for GPT-4o: {max_tokens} tokens.")
    print("Rule of thumb: 1000 tokens ≈ 750 words.")

if __name__ == "__main__":
    demo_tokenization()
