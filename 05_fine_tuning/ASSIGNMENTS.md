# Fine-Tuning Assignments

## Objective
Understand the data preparation and configuration steps for fine-tuning LLMs.

## Prerequisite Knowledge
- Basics of Neural Networks (Weights, Gradients)
- HuggingFace Transformers
- LoRA/QLoRA concepts

## Practical Assignments

### Assignment 1: Dataset Preparation
**Goal:** specific Formatting for Fine-tuning.
**Task:**
1.  Source: A simple list of Q&A pairs (e.g., `[("Hi", "Hello"), ("Bye", "Goodbye")]`).
2.  Target: Chat Format.
3.  Write a script that converts the source into:
    `{"messages": [{"role": "user", "content": "Hi"}, {"role": "assistant", "content": "Hello"}]}`
4.  Save as `.jsonl`.

### Assignment 2: LoRA Configuration
**Goal:** Set up the PEFT (Parameter-Efficient Fine-Tuning) config.
**Task:**
1.  Import `LoraConfig` from `peft`.
2.  Create a config object with:
    - `r` (rank) = 16
    - `lora_alpha` = 32
    - `target_modules` = ["q_proj", "v_proj"] (standard for Llama-like models).
3.  Print the config to verify.
4.  (Optional) Load a small model and apply this config using `get_peft_model`.

## Conceptual Quiz
1.  What is "Catastrophic Forgetting"?
2.  Why does QLoRA use less memory than Full Fine-Tuning?
3.  What is the difference between "Pre-training" and "Fine-tuning"?
