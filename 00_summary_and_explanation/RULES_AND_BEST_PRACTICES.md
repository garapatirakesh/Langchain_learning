# Universal Rules and Best Practices

## Golden Rules (Apply to Everything)

### **Rule 1: Start Simple, Add Complexity Only When Needed**

**Why:** Over-engineering wastes time and creates maintenance burdens

**How to apply:**
- Begin with the simplest solution that could work
- Add features incrementally
- Justify each addition of complexity
- Remove complexity that doesn't add value

**Example:**
- ❌ Don't build a multi-agent system for a simple FAQ bot
- ✅ Start with basic Q&A, add agents only if truly needed

---

### **Rule 2: Always Validate Inputs**

**Why:** User input is unpredictable and potentially malicious

**How to apply:**
- Check data types
- Validate formats
- Sanitize strings
- Set reasonable limits
- Reject invalid inputs early

**Example:**
- ❌ Directly using user input in prompts
- ✅ Validate, sanitize, then use

---

### **Rule 3: Handle Errors Gracefully**

**Why:** Things will fail - APIs, networks, LLMs, tools

**How to apply:**
- Use try-catch blocks
- Provide fallback responses
- Log errors for debugging
- Don't expose internal errors to users
- Retry with exponential backoff

**Example:**
- ❌ Let exceptions crash the app
- ✅ Catch, log, provide user-friendly message

---

### **Rule 4: Monitor Costs Continuously**

**Why:** LLM costs can escalate quickly

**How to apply:**
- Track token usage
- Set budget alerts
- Use cheaper models when possible
- Cache responses when appropriate
- Optimize prompt length

**Example:**
- ❌ Using GPT-4 for everything
- ✅ GPT-4 for complex tasks, GPT-3.5 for simple ones

---

### **Rule 5: Test Thoroughly Before Production**

**Why:** LLMs are non-deterministic and can behave unexpectedly

**How to apply:**
- Test with diverse inputs
- Test edge cases
- Test error scenarios
- Test at scale
- Use staging environments

**Example:**
- ❌ Deploying after one successful test
- ✅ Testing 100+ diverse scenarios

---

## Prompt Engineering Rules

### **Rule 6: Be Specific and Clear**

**Why:** Vague prompts produce vague results

**How to apply:**
- State exactly what you want
- Provide context
- Specify format
- Give examples
- Set constraints

**Example:**
- ❌ "Summarize this"
- ✅ "Summarize this article in 3 bullet points, focusing on key findings"

---

### **Rule 7: Use System Prompts for Behavior**

**Why:** Separates role/behavior from task

**How to apply:**
- Define AI's role in system prompt
- Set tone and style
- Establish constraints
- Keep task prompts focused on the task

**Example:**
```
System: "You are a helpful coding assistant. Be concise and provide working code."
User: "How do I sort a list in Python?"
```

---

### **Rule 8: Provide Examples (Few-Shot Learning)**

**Why:** Examples dramatically improve output quality

**How to apply:**
- Show 2-5 examples of desired output
- Use diverse examples
- Match example format to desired format
- Include edge cases in examples

**Example:**
```
Extract names from text:

Example 1:
Input: "John went to the store"
Output: ["John"]

Example 2:
Input: "Mary and Bob are friends"
Output: ["Mary", "Bob"]

Now extract from: "Alice, Charlie, and David went hiking"
```

---

### **Rule 9: Version and Track Prompts**

**Why:** Prompts are code - treat them as such

**How to apply:**
- Store prompts in version control
- Document changes
- A/B test prompt variations
- Roll back if quality degrades

---

## State Management Rules

### **Rule 10: Keep State Minimal**

**Why:** More state = more complexity and cost

**How to apply:**
- Only track what you actually need
- Remove unused fields
- Summarize old data
- Archive instead of keeping everything

---

### **Rule 11: Define State Schema Upfront**

**Why:** Prevents bugs and makes code predictable

**How to apply:**
- Use TypedDict or Pydantic
- Document each field
- Specify types clearly
- Plan for evolution

---

### **Rule 12: Never Mutate State Directly**

**Why:** Causes bugs and breaks immutability

**How to apply:**
- Return state updates, don't modify
- Use functional patterns
- Let framework handle merging

---

## Tool and Function Calling Rules

### **Rule 13: One Tool, One Purpose**

**Why:** Single responsibility makes tools reliable and reusable

**How to apply:**
- Each tool does one thing well
- Don't create Swiss Army knife tools
- Compose tools for complex operations

---

### **Rule 14: Document Tools Thoroughly**

**Why:** LLM uses docstrings to decide when to call

**How to apply:**
- Clear function description
- Document all parameters
- Specify return format
- Include examples in docstring

---

### **Rule 15: Validate Tool Outputs**

**Why:** Tools can fail or return unexpected data

**How to apply:**
- Check return types
- Validate data format
- Handle None/null
- Provide error messages

---

## Safety and Security Rules

### **Rule 16: Never Trust User Input**

**Why:** Security, safety, and reliability

**How to apply:**
- Sanitize all inputs
- Validate against schema
- Escape special characters
- Set length limits
- Reject suspicious patterns

---

### **Rule 17: Implement Rate Limiting**

**Why:** Prevent abuse and control costs

**How to apply:**
- Limit requests per user
- Limit requests per time period
- Implement quotas
- Graceful degradation when limits hit

---

### **Rule 18: Filter Sensitive Information**

**Why:** Privacy and compliance

**How to apply:**
- Don't log sensitive data
- Redact PII from prompts
- Don't store unnecessary data
- Encrypt sensitive information

---

### **Rule 19: Use Human-in-the-Loop for Critical Actions**

**Why:** Safety and accountability

**How to apply:**
- Pause before destructive operations
- Require approval for financial transactions
- Log all critical decisions
- Provide clear action summaries

---

## Performance and Optimization Rules

### **Rule 20: Cache When Possible**

**Why:** Saves time and money

**How to apply:**
- Cache frequent queries
- Cache tool results
- Set appropriate TTLs
- Invalidate when data changes

---

### **Rule 21: Use Streaming for Long Responses**

**Why:** Better user experience

**How to apply:**
- Stream chat responses
- Show progress indicators
- Allow cancellation
- Handle stream interruptions

---

### **Rule 22: Optimize Token Usage**

**Why:** Tokens = money

**How to apply:**
- Keep prompts concise
- Summarize long conversations
- Remove redundant context
- Use appropriate context windows

---

## Error Handling Rules

### **Rule 23: Fail Fast, Fail Clearly**

**Why:** Easier debugging and better UX

**How to apply:**
- Validate early
- Provide specific error messages
- Log error context
- Don't continue with invalid state

---

### **Rule 24: Implement Retry Logic**

**Why:** Transient failures are common

**How to apply:**
- Retry with exponential backoff
- Set maximum retry attempts
- Only retry retriable errors
- Log retry attempts

---

### **Rule 25: Have Fallback Strategies**

**Why:** Graceful degradation

**How to apply:**
- Primary method → fallback method → default
- Cached response if API fails
- Simpler model if primary unavailable
- Inform user of degraded service

---

## Testing Rules

### **Rule 26: Test with Diverse Inputs**

**Why:** LLMs behave differently with different inputs

**How to apply:**
- Test happy path
- Test edge cases
- Test error conditions
- Test with real user data
- Test different languages/formats

---

### **Rule 27: Monitor in Production**

**Why:** Catch issues before users do

**How to apply:**
- Track error rates
- Monitor latency
- Track token usage
- Log unusual patterns
- Set up alerts

---

## Deployment Rules

### **Rule 28: Use Environment Variables for Secrets**

**Why:** Security

**How to apply:**
- Never hardcode API keys
- Use .env files locally
- Use secret managers in production
- Rotate keys regularly

---

### **Rule 29: Version Your Deployments**

**Why:** Rollback capability

**How to apply:**
- Tag releases
- Keep previous versions available
- Document changes
- Test before deploying

---

### **Rule 30: Start with Conservative Settings**

**Why:** Safety first

**How to apply:**
- Lower temperature initially
- Shorter max tokens
- Stricter validation
- More human oversight
- Relax gradually based on data

---

## Architecture Rules

### **Rule 31: Separate Concerns**

**Why:** Maintainability and testability

**How to apply:**
- Prompts in separate files
- Tools in separate modules
- State management isolated
- Clear boundaries between components

---

### **Rule 32: Make Components Reusable**

**Why:** Don't repeat yourself

**How to apply:**
- Generic tools
- Reusable prompts
- Common utilities
- Shared state patterns

---

### **Rule 33: Document Your Decisions**

**Why:** Future you will thank you

**How to apply:**
- Why this architecture?
- Why this model?
- Why this prompt?
- What alternatives were considered?

---

## Cost Management Rules

### **Rule 34: Choose the Right Model**

**Why:** Balance quality and cost

**How to apply:**
- Use cheapest model that works
- Reserve expensive models for complex tasks
- A/B test model performance
- Monitor cost per request

---

### **Rule 35: Set Budget Limits**

**Why:** Prevent runaway costs

**How to apply:**
- Set daily/monthly budgets
- Alert at thresholds
- Automatic shutoff at limits
- Review costs regularly

---

## Quality Rules

### **Rule 36: Measure Quality Objectively**

**Why:** "Feels good" isn't enough

**How to apply:**
- Define success metrics
- Track accuracy
- Measure user satisfaction
- A/B test changes
- Use evaluation datasets

---

### **Rule 37: Iterate Based on Data**

**Why:** Continuous improvement

**How to apply:**
- Collect user feedback
- Analyze failures
- Identify patterns
- Test improvements
- Deploy incrementally

---

## Collaboration Rules

### **Rule 38: Make Code Readable**

**Why:** Others (and future you) will read it

**How to apply:**
- Clear variable names
- Comment complex logic
- Document assumptions
- Explain non-obvious choices

---

### **Rule 39: Use Consistent Patterns**

**Why:** Predictability and maintainability

**How to apply:**
- Establish conventions
- Follow them consistently
- Document patterns
- Review for consistency

---

### **Rule 40: Share Knowledge**

**Why:** Team effectiveness

**How to apply:**
- Document learnings
- Share prompt strategies
- Explain architectural decisions
- Conduct code reviews

---

## Quick Decision Framework

### **When to use which approach:**

**Simple Chain:**
- One-off tasks
- Linear workflows
- No state needed

**LangGraph Agent:**
- Multi-step reasoning
- Conditional logic
- State management needed

**Deep Agent:**
- Complex tasks
- Quality critical
- Multiple patterns needed

**Multi-Agent:**
- Requires different expertise
- Parallel processing beneficial
- Very complex tasks

---

## Common Anti-Patterns to Avoid

### ❌ **Anti-Pattern 1: Prompt Stuffing**
Cramming everything into one massive prompt
**Instead:** Break into focused prompts

### ❌ **Anti-Pattern 2: No Error Handling**
Assuming everything works
**Instead:** Expect and handle failures

### ❌ **Anti-Pattern 3: Infinite Loops**
No exit conditions
**Instead:** Always set maximum iterations

### ❌ **Anti-Pattern 4: Ignoring Costs**
Not tracking token usage
**Instead:** Monitor and optimize continuously

### ❌ **Anti-Pattern 5: Over-Engineering**
Building complex systems for simple tasks
**Instead:** Start simple, add complexity only when needed

---

## Remember

These rules are guidelines, not laws. Context matters. Sometimes you need to break a rule - just make sure you understand why and document your reasoning.

**The ultimate rule:** Build systems that are reliable, maintainable, and solve real problems for users.
