# Guardrails & Safety Assignments

## Objective
Implement safety layers to prevent LLMs from generating harmful, incorrect, or private information.

## Prerequisite Knowledge
- Regular Expressions
- Basic Text Classification

## Practical Assignments

### Assignment 1: The PII Redactor
**Goal:** Protect user privacy.
**Task:**
1.  Write a function `redact_pii(text)`.
2.  Use Regex to find email addresses (`\b[\w\.-]+@[\w\.-]+\.\w+\b`).
3.  Replace found emails with `<EMAIL_REDACTED>`.
4.  Test it: "Contact me at bob@example.com" -> "Contact me at <EMAIL_REDACTED>".

### Assignment 2: Pattern-Based Guardrails
**Goal:** Enforce output structure.
**Task:**
1.  Scenario: The LLM must output ONLY a date in `YYYY-MM-DD` format.
2.  Call LLM.
3.  Regex check the output.
4.  Loop: If check fails, feed the error message back to the LLM ("Format incorrect, please provide YYYY-MM-DD") and retry.

### Assignment 3: Toxic Topic Filter
**Goal:** Prevent discussion of banned topics.
**Task:**
1.  Define a "Guardrail Chain".
2.  Step 1: Classifier LLM. Input: User Query. System: "Is this query about [Banned Topic]? Answer YES or NO."
3.  Step 2: Logic. If YES, return "I cannot discuss that."
4.  If NO, pass to the main Chat LLM.

## Conceptual Quiz
1.  What is "Prompt Injection"?
2.  Why should guardrails efficiently run *before* the main expensive model?
3.  What is the difference between "Input Rail" and "Output Rail"?
