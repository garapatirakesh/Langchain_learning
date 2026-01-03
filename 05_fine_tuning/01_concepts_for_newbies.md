# Fine-Tuning Concepts for New Bees

Welcome to the world of training your own AI! This guide explains the "Scary Words" of Fine-Tuning in plain English.

---

## 1. The Numbers: FP32 vs FP16 vs BF16
Computers store numbers in "bits". The more bits, the more precise the number, but the more memory (RAM) it takes.

### FP32 (Full Precision - 32-bit Float)
- **What is it?**: The standard high-quality number format. Like writing `3.14159265`.
- **Pros**: Extremely accurate.
- **Cons**: Huge memory usage. A 7B model in FP32 takes ~28GB VRAM. Too big for most home GPUs.

### FP16 (Half Precision - 16-bit Float)
- **What is it?**: Cutting the bits in half. Like writing `3.1416`.
- **Pros**: Uses half the memory (14GB for a 7B model). 2x faster.
- **Cons**: Precision loss. Sometimes numbers get too small and become zero (Underflow).

### BF16 (Brain Float 16)
- **What is it?**: A special format invented by Google Brain.
- **The Trick**: It keeps the same "Range" (exponent) as FP32 but sacrifices precision (mantissa).
- **Why use it?**: It is much more stable than FP16 during training. It doesn't crash as often.
- **Requirement**: You need a modern GPU (Nvidia Ampere / A100 / RTX 30 series or newer) to use it.

---

## 2. The Techniques: PEFT, LoRA, and QLoRA

### Full Fine-Tuning (The Old Hard Way)
Imagine you have a massive encyclopedia (The Model). You want to add a chapter on "Pokemon".
- **Full Fine-Tuning**: Rewriting the **entire** encyclopedia. You update every single weight.
- **Problem**: You need 4x-8x the memory of the model itself to store gradients. Impossible for most people.

### PEFT (Parameter-Efficient Fine-Tuning)
- **Concept**: Instead of rewriting the book, just **staple a sticky note** to the relevant pages.
- **Result**: You only train 1% of the parameters. The rest of the model is frozen (locked).

### LoRA (Low-Rank Adaptation)
- **What is it?**: The most popular PEFT method.
- **The Math**: It injects two tiny matrices (A and B) into the model.
- **Analogy**: Instead of learning a 100x100 grid of numbers (10,000 numbers), LoRA learns two lines of size 100x1 (200 numbers) that *approximate* the big grid.
- **Benefit**: Reduces trainable parameters by 10,000x. You can fine-tune Llama-3 on a free Google Colab.

### QLoRA (Quantized LoRA)
- **The "Q"**: Stands for **Quantization**.
- **Quantization**: Compressing numbers. Instead of using 16-bit or 32-bit, we use **4-bit** numbers.
    - It's like rounding `3.14159` to `3`.
- **The Magic**:
    1.  Load the massive model in 4-bit (super compressed).
    2.  Add LoRA adapters on top.
    3.  Train *only* the adapters in 16-bit.
- **Result**: You can train a 70B model on a single 24GB or 48GB GPU. This was impossible before QLoRA.

---

## 3. The Library Stack: TRL & Friends
When you write code, you will use these libraries from HuggingFace.

### 1. `transformers` (The Base)
- Loads the actual model and tokenizer.
- `AutoModelForCausalLM.from_pretrained(...)`

### 2. `peft` (The Adapter Manager)
- Handles the LoRA/QLoRA logic.
- Adds the "sticky notes" to your model.
- `LoraConfig(...)`

### 3. `bitsandbytes` (The Compressor)
- Doing 4-bit math is hard. This library does the heavy lifting of Quantization.
- Required for QLoRA to work.

### 4. `trl` (Transformer Reinforcement Learning)
- This is the "Trainer". It simplifies the training loop.
- It contains `SFTTrainer` (Supervised Fine-Tuning Trainer).
- Instead of writing a loop that iterates 1000 times, you just run: `trainer.train()`.

---

## 4. Example: How to Train (Pseudo-Code)

1.  **Load Model**:
    ```python
    # Load in 4-bit to save memory (QLoRA)
    bnb_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16)
    model = AutoModelForCausalLM.from_pretrained("llama-3-8b", quantization_config=bnb_config)
    ```

2.  **Add LoRA**:
    ```python
    # Staple the sticky notes
    peft_config = LoraConfig(r=16, lora_alpha=32, target_modules=["q_proj", "v_proj"])
    model = get_peft_model(model, peft_config)
    ```

3.  **Prepare Data**:
    ```python
    # Format: User asks -> Assistant answers
    dataset = load_dataset("my_company_emails")
    ```

4.  **Train (using TRL)**:
    ```python
    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        args=TrainingArguments(per_device_train_batch_size=2, learning_rate=2e-4) # Hyperparameters
    )
    trainer.train()
    ```

5.  **Save**:
    ```python
    trainer.save_model("my_new_ai")
    ```

---

## 5. Advanced Concepts: Beyond Basic Training

### DPO (Direct Preference Optimization)
- **The Old Way (RLHF)**: Train Reward Model -> Train PPO. Complex and unstable.
- **The New Way (DPO)**: Skip the Reward Model.
- **How**: You feed the model pairs of (Good Answer, Bad Answer). You mathematically force the model to increase the probability of the Good Answer and decrease the probability of the Bad Answer directly.
- **Why**: Stable, cheaper, and often better than PPO.

### Scaling Laws (Chinchilla)
- **The Rule**: "For every parameter in the model, you need 20 tokens of training data."
- **Meaning**: If you have a 7B model, you ideally need 140 Billion tokens to train it "optimally".
- **Fine-Tuning Relevance**: You don't need billions for fine-tuning. Usually, **1,000 to 10,000 high-quality examples** is the sweet spot for specialized tasks.

### Hyperparameters Decoded
- **Epochs**: How many times the model sees the *entire* dataset.
    - Too few: Underfitting (dumb).
    - Too many: Overfitting (memorizes the answers).
    - *Recommend*: 1 to 3 epochs.
- **Learning Rate**: How big are the steps we take to update weights?
    - Too high: The model diverges (gets worse).
    - Too low: It learns forever.
    - *Recommend*: `2e-4` (0.0002) for LoRA is standard.
- **Batch Size**: How many examples it looks at before updating weights.
    - *Recommend*: As big as your GPU memory allows.


## Summary
- **FP32**: Big, Gold Standard.
- **BF16**: Fast, Stable, Modern Standard.
- **PEFT/LoRA**: Training sticky notes instead of the whole book.
- **QLoRA**: Training sticky notes on a **compressed** book (4-bit).
- **TRL**: The library that runs the training loop for you.
