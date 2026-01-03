import torch
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, BitsAndBytesConfig
from trl import SFTTrainer

# ==========================================
# 1. Configuration (The "Hyperparameters")
# ==========================================
MODEL_NAME = "facebook/opt-350m" # Small model for demo purposes. In real life, use "meta-llama/Llama-2-7b-hf"
NEW_MODEL_NAME = "opt-350m-finetuned"

# BitsAndBytes Config (For QLoRA 4-bit quantization)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",      # Normalized Float 4 (Better for weights)
    bnb_4bit_compute_dtype=torch.float16, # Compute in 16-bit (faster)
)

# LoRA Config (The "Sticky Notes")
peft_config = LoraConfig(
    r=16,       # Rank: How complex the sticky note is. Higher = smarter but slower.
    lora_alpha=32, # Alpha: How much weight to give the sticky note.
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM", # We are training a Chatbot (Causal Language Model)
    target_modules=["q_proj", "v_proj"] # Apply LoRA to Query and Value projection layers (Standard for Transformers)
)

# ==========================================
# 2. Load Model & Tokenizer
# ==========================================
print(f"Loading {MODEL_NAME}...")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=bnb_config,
    device_map="auto" # Auto-distribute to GPU
)

# Enable gradient checkpointing to save memory
model.gradient_checkpointing_enable()
# Prepare model for k-bit training (freezes original weights)
model = prepare_model_for_kbit_training(model)
# Apply LoRA
model = get_peft_model(model, peft_config)

print("LoRA Model Ready:")
model.print_trainable_parameters() 
# Expect output like: "trainable params: 1,500,000 || all params: 350,000,000 || trainable%: 0.4%"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token # Fix padding issue
tokenizer.padding_side = "right" # Fix mixed precision issue

# ==========================================
# 3. Load Dataset
# ==========================================
# We use a tiny dataset for demonstration.
# In reality, this should be a JSONL file with {"text": "Question... Answer..."}
dataset = load_dataset("imdb", split="train[:1%]") # Using 1% of IMDB for speed

def formatting_prompts_func(example):
    output_texts = []
    for text in example['text']:
        # Format the text so the model learns: System -> User -> Assistant
        formatted_text = f"### Human: Analyze the sentiment of this review.\n{text}\n### Assistant: "
        output_texts.append(formatted_text)
    return output_texts

# ==========================================
# 4. Training (The TRL SFTTrainer)
# ==========================================
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=1,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=1,
    optim="paged_adamw_32bit", # Specialized optimizer for QLoRA
    logging_steps=25,
    learning_rate=2e-4,
    weight_decay=0.001,
    fp16=False,
    bf16=False, # Set to True if you have an Ampere GPU (RTX 30xx/40xx)
    max_grad_norm=0.3,
    max_steps=-1,
    warmup_ratio=0.03,
    group_by_length=True,
    lr_scheduler_type="constant",
)

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    peft_config=peft_config,
    max_seq_length=None,
    dataset_text_field="text", # The column name in the dataset
    tokenizer=tokenizer,
    args=training_args,
    packing=False,
)

print("Starting Training...")
# trainer.train() 

# Note: trainer.train() is commented out so this script doesn't accidentally 
# start a heavy training run if you execute it. Uncomment to run.

# ==========================================
# 5. Saving
# ==========================================
# trainer.save_model(NEW_MODEL_NAME)
print("Training script ready. Uncomment trainer.train() to execute.")
