# Quick Reference Guide - Cheat Sheet

## LangChain Core - Quick Reference

### **Models**
```
Purpose: AI that generates text
Common: GPT-4o, GPT-4o-mini, GPT-3.5-turbo
Key Parameter: temperature (0=deterministic, 2=creative)
```

### **Prompts**
```
Structure:
1. Role/System: "You are a..."
2. Context: "The user is..."
3. Task: "Please..."
4. Format: "Respond as..."
5. Constraints: "Keep it..."
```

### **Memory Types**
```
Buffer: Last N messages
Summary: Summarized history
Entity: Facts about people/things
```

### **When to Use**
- ✅ Simple Q&A, chatbots, content generation
- ❌ Complex workflows, multi-step reasoning

---

## LangGraph - Quick Reference

### **Core Components**
```
State: Data flowing through graph
Nodes: Functions that do work
Edges: Connections between nodes
Graph: Complete workflow
```

### **Edge Types**
```
Regular: Always A → B
Conditional: Route based on state
```

### **Common Patterns**
```
Simple Tool Agent: User → Agent → Tool → Response
ReAct: Think → Act → Observe → Repeat
Plan-Execute: Plan → Execute Steps → Synthesize
Reflection: Generate → Critique → Improve
HITL: Propose → Human Approves → Execute
```

### **When to Use**
- ✅ Multi-step tasks, conditional logic, tool use
- ❌ Simple one-shot queries

---

## Deep Agents - Quick Reference

### **What Makes It Deep**
```
✓ Planning (thinks ahead)
✓ Reflection (improves quality)
✓ Tools (interacts with world)
✓ Memory (maintains context)
✓ Collaboration (multi-agent)
✓ Safety (human oversight)
```

### **Architecture**
```
1. Analyze Task
2. Create Plan
3. Execute Steps (with tools)
4. Reflect on Quality
5. Improve if Needed
6. Synthesize Results
7. Deliver Output
```

### **When to Use**
- ✅ Complex tasks, quality-critical, multi-step
- ❌ Simple queries, real-time needs

---

## Prompt Engineering - Quick Tips

### **Better Prompts**
```
❌ "Summarize this"
✅ "Summarize this article in 3 bullet points, focusing on key findings"

❌ "Write code"
✅ "Write a Python function that sorts a list of dictionaries by the 'age' key"

❌ "Be creative"
✅ "Generate 5 creative marketing slogans for an eco-friendly water bottle, targeting millennials"
```

### **Prompt Template**
```
Role: You are a [expert in X]
Context: The user needs [specific help]
Task: Please [specific action]
Format: Provide [output format]
Constraints: [limits/requirements]
Examples: [1-3 examples]
```

---

## State Management - Quick Tips

### **Good State Design**
```
✓ Minimal (only what you need)
✓ Typed (use TypedDict)
✓ Documented (comment each field)
✓ Immutable (return updates, don't mutate)
```

### **Common State Fields**
```
messages: Conversation history
current_step: Progress tracking
iteration_count: Loop control
results: Intermediate outputs
user_context: User information
metadata: Timestamps, scores, etc.
```

---

## Error Handling - Quick Patterns

### **Try-Catch Pattern**
```
try:
    result = risky_operation()
except SpecificError:
    result = fallback_value
    log_error()
```

### **Retry Pattern**
```
max_retries = 3
for attempt in range(max_retries):
    try:
        return operation()
    except RetriableError:
        if attempt == max_retries - 1:
            raise
        wait(2 ** attempt)  # Exponential backoff
```

### **Fallback Pattern**
```
try:
    return primary_method()
except:
    try:
        return fallback_method()
    except:
        return default_value
```

---

## Tool Design - Quick Guide

### **Good Tool Structure**
```
def tool_name(param: type) -> str:
    """Clear description of what tool does.
    
    Args:
        param: Description of parameter
        
    Returns:
        Description of return value
    """
    try:
        result = do_work(param)
        return f"Success: {result}"
    except Exception as e:
        return f"Error: {str(e)}"
```

### **Tool Best Practices**
```
✓ One purpose per tool
✓ Clear docstrings
✓ Type hints
✓ Error handling
✓ Descriptive names
```

---

## Cost Optimization - Quick Tips

### **Save Money**
```
1. Use cheapest model that works
2. Cache frequent queries
3. Optimize prompt length
4. Summarize long conversations
5. Set token limits
6. Monitor usage
```

### **Model Selection**
```
Simple tasks → GPT-3.5-turbo (cheapest)
Balanced → GPT-4o-mini (good value)
Complex tasks → GPT-4o (best quality)
```

---

## Testing - Quick Checklist

### **What to Test**
```
□ Happy path (normal usage)
□ Edge cases (unusual inputs)
□ Error cases (invalid inputs)
□ Long inputs (token limits)
□ Concurrent requests (race conditions)
□ Cost (token usage)
□ Latency (response time)
```

---

## Common Mistakes - Quick List

### **Top 10 Mistakes**
```
1. ❌ Not validating inputs
2. ❌ No error handling
3. ❌ Ignoring costs
4. ❌ Poor prompts
5. ❌ No iteration limits
6. ❌ Over-engineering
7. ❌ Not testing thoroughly
8. ❌ Hardcoding secrets
9. ❌ No monitoring
10. ❌ Mutating state directly
```

---

## Decision Tree - Which Approach?

### **Choose Your Tool**
```
Need simple Q&A?
└─ Use LangChain Simple Chain

Need conversation memory?
└─ Use LangChain with Memory

Need to call tools?
└─ Use LangGraph Tool Agent

Need conditional logic?
└─ Use LangGraph with Conditional Edges

Need multi-step reasoning?
└─ Use LangGraph ReAct or Plan-Execute

Need quality iteration?
└─ Use Reflection Pattern

Need human approval?
└─ Use Human-in-the-Loop Pattern

Need multiple specialists?
└─ Use Multi-Agent System

Need everything?
└─ Use Deep Agent
```

---

## Temperature Guide

### **When to Use What**
```
0.0 - 0.3: Deterministic
└─ Use for: Facts, code, structured data, math

0.4 - 0.7: Balanced
└─ Use for: General chat, explanations, Q&A

0.8 - 1.5: Creative
└─ Use for: Brainstorming, creative writing, ideas

1.6 - 2.0: Very Creative
└─ Use for: Experimental, artistic, very diverse outputs
```

---

## Token Management

### **Token Basics**
```
1 token ≈ 4 characters
"Hello world" = 2 tokens
Average word = 1.3 tokens
```

### **Context Windows**
```
GPT-3.5: 4K or 16K tokens
GPT-4: 8K, 32K, or 128K tokens
GPT-4o: 128K tokens
```

### **Cost Formula**
```
Total Cost = (Input Tokens × Input Price) + (Output Tokens × Output Price)
```

---

## Streaming vs Non-Streaming

### **Use Streaming When:**
```
✓ Chat interfaces
✓ Long responses
✓ User needs to see progress
✓ Want to allow cancellation
```

### **Use Non-Streaming When:**
```
✓ Need complete response first
✓ Parsing structured output
✓ Batch processing
✓ Simplicity is priority
```

---

## Memory Management

### **When Conversation Gets Long**
```
Option 1: Summarize old messages
Option 2: Keep only last N messages
Option 3: Extract key facts, discard details
Option 4: Start new conversation
```

---

## Safety Checklist

### **Before Production**
```
□ Input validation implemented
□ Output filtering in place
□ Rate limiting configured
□ Error handling complete
□ Logging set up
□ Monitoring enabled
□ Secrets in environment variables
□ Human oversight for critical actions
□ Budget limits set
□ Tested with malicious inputs
```

---

## Performance Optimization

### **Speed Up Your Agent**
```
1. Use faster models when possible
2. Implement caching
3. Parallel tool calls
4. Optimize prompt length
5. Use streaming
6. Reduce state size
```

---

## Debugging Tips

### **When Things Go Wrong**
```
1. Check logs
2. Verify state at each step
3. Test nodes individually
4. Validate tool outputs
5. Check token limits
6. Verify routing logic
7. Test with simpler inputs
8. Add more logging
```

---

## Production Checklist

### **Ready to Deploy?**
```
□ Thoroughly tested
□ Error handling complete
□ Monitoring set up
□ Costs estimated
□ Rate limits configured
□ Documentation written
□ Secrets secured
□ Rollback plan ready
□ Alerts configured
□ Team trained
```

---

## Quick Formulas

### **Estimate Tokens**
```
Characters ÷ 4 = Approximate tokens
Words × 1.3 = Approximate tokens
```

### **Estimate Cost**
```
(Prompt tokens + Response tokens) × Price per 1K tokens ÷ 1000
```

### **Estimate Time**
```
~50 tokens/second for streaming
~2-5 seconds for typical response
Add tool call time if applicable
```

---

## Remember

**Start Simple → Test Thoroughly → Deploy Carefully → Monitor Continuously → Iterate Based on Data**

This is your quick reference. For detailed explanations, see the full module documentation.
