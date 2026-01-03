# 🧠 LLM Architecture, Quantization & Performance: 200 Interview Questions

This document covers the deep technical foundations of Large Language Models, from basic probability to 1-bit quantization and advanced Transformer architectures.

---

## 🏗️ Section 1: Foundations & The Transformer Architecture (1-40)

1. **Q: What is the "Transformer" architecture?**
   - **A:** A neural network design that uses "Self-Attention" to process entire sequences of text at once, rather than one word at a time like older models (RNNs).

2. **Q: What is Self-Attention in plain English?**
   - **A:** It is a mechanism that allows the model to look at every other word in a sentence to understand the context of the current word. (e.g., in "The bank of the river," attention helps the model know "bank" isn't a financial institution).

3. **Q: Explain the "Scaled Dot-Product Attention" formula.**
   - **A:** It calculates how much "focus" a word (Query) should put on other words (Keys) to get a combined meaning (Value). It is divided by a scale factor to keep numbers stable.

4. **Q: What is Multi-Head Attention (MHA)?**
   - **A:** Running the attention process multiple times in parallel. Each "head" can focus on different things (e.g., one head for grammar, one for facts, one for sentiment).

5. **Q: What is Grouped Query Attention (GQA)?**
   - **A:** A faster version of MHA used in models like Llama 3. It shares "Keys" and "Values" across multiple "Queries" to reduce memory usage during inference.

6. **Q: Difference between Encoder-only, Decoder-only, and Encoder-Decoder?**
   - **A:** 
     - **Encoder-only** (BERT): Good for understanding text (classification).
     - **Decoder-only** (GPT, Llama): Good for generating text (chatting).
     - **Encoder-Decoder** (T5): Good for translation (Input -> Process -> Output).

7. **Q: Why are modern LLMs mostly "Decoder-only"?**
   - **A:** Because they are highly efficient at predicting the next word in a sequence, which is the core task of generative AI.

8. **Q: What is Positional Encoding?**
   - **A:** Since Transformers process all words at once, they don't know the order. Positional encoding adds "tags" to words to tell the model where they sit in a sentence.

9. **Q: Explain RoPE (Rotary Positional Embeddings).**
   - **A:** A modern way to encode position by rotating the word's vector. It is much better at handling very long conversations than older methods.

10. **Q: What is Layer Normalization?**
    - **A:** A math step after each layer that keeps the numbers (activations) from getting too big or too small, ensuring the model stays stable during training.

11. **Q: Difference between Pre-Norm and Post-Norm?**
    - **A:** Pre-Norm applies normalization *before* the layer's work; Post-Norm applies it *after*. Pre-Norm is more stable and common in modern Llama/GPT models.

12. **Q: What is an Activation Function (e.g., GeLU, SwiGLU)?**
    - **A:** A math "gate" that decides if a signal is important enough to pass through to the next layer. SwiGLU is the gold standard for Llama models.

13. **Q: What are Feed-Forward Networks (FFN) in a Transformer?**
    - **A:** After the model "listens" via attention, the FFN "thinks" about the data. It's where most of the model's factual knowledge is stored.

14. **Q: What is a "Residual Connection" (Skip Connection)?**
    - **A:** A "bypass" that allows data to flow directly from an early layer to a later one. This prevents "vanishing gradients" and allows models to be very deep (100+ layers).

15. **Q: What is the embedding dimension?**
    - **A:** The size of the list of numbers representing a single word. (e.g., in GPT-3, every word is a list of 12,288 numbers).

16. **Q: Explain "Tokenization" at the architecture level.**
    - **A:** It is the bridge between text and math. It converts words into unique ID numbers that the neural network can multiply.

17. **Q: What is BPE (Byte Pair Encoding)?**
    - **A:** A common tokenization method that breaks rare words into common sub-words (e.g., "unhappy" -> "un" + "happy") to keep the vocabulary size manageable.

18. **Q: What is a "Vocabulary Size"?**
    - **A:** The total number of unique tokens a model knows. Llama 3 knows ~128,000 tokens; GPT-4 likely knows more.

19. **Q: What are "Weight Matrices"?**
    - **A:** The actual numbers (parameters) stored in the model. When you "run" an LLM, you are performing billions of matrix multiplications using these weights.

20. **Q: What is the "Head Dim"?**
    - **A:** The size of each individual head in multi-head attention. Usually 64 or 128.

21. **Q: Explain "Attention Bias."**
    - **A:** Adding specific numbers to the attention score to force the model to ignore certain words (like padding) or focus on others.

22. **Q: What is the role of the "Softmax" function in attention?**
    - **A:** It turns "raw scores" into percentages that add up to 100%, allowing the model to say "Focus 80% on this word and 20% on that one."

23. **Q: What is "Sparsity" in LLMs?**
    - **A:** When many numbers in the model are zero or near-zero. Sparse models (like MoE) are faster because they don't use every parameter for every word.

24. **Q: What is a "Mixture of Experts" (MoE) model?**
    - **A:** Instead of one giant brain, the model has 8 "mini-brains." For every word, it only turns on the 2 best mini-brains to save energy/speed.

25. **Q: Explain the "Router" in an MoE model.**
    - **A:** The traffic cop that decides which "Expert" brain is best suited to handle the current word.

26. **Q: What is "Total Parameters" vs "Active Parameters"?**
    - **A:** In MoE, "Total" is all the mini-brains combined; "Active" is only the ones turned on at any given moment.

27. **Q: How does the "Context window" limit work?**
    - **A:** It's the maximum number of tokens the attention mechanism can remember at once. It's limited by the RAM of the GPU.

28. **Q: What is the "Quadratic Bottleneck" of attention?**
    - **A:** If you double the text length, the attention work quadruples ($N^2$). This is why long context is hard to achieve.

29. **Q: Explain "Flash Attention."**
    - **A:** A super-optimized way to calculate attention that avoids moving data back and forth to slow memory, making it 5-10x faster and memory-efficient.

30. **Q: What is a "Sliding Window Attention"?**
    - **A:** The model only looks at the last 500 words instead of everything, keeping the work constant even for 1-million-word books.

31. **Q: What is "Linear Attention"?**
    - **A:** Architectures that try to fix the quadratic bottleneck so that doubling text only doubles the work ($O(N)$).

32. **Q: Explain "Weight Tying."**
    - **A:** Using the same list of numbers for both the "input" and "output" of the model to save memory.

33. **Q: What is a "Temperature 0" decode?**
    - **A:** The model always picks the single most likely next word. No creativity, purely logical matching.

34. **Q: What is "Top-P" (Nucleus) sampling?**
    - **A:** The model looks at the top words that add up to P% probability (e.g., 90%). This ignores the "junk" low-probability words.

35. **Q: What is "Top-K" sampling?**
    - **A:** The model only considers the top K (e.g., 50) most likely words and ignores everything else.

36. **Q: Explain "Greedy Search."**
    - **A:** The simplest decoding where the model always takes the #1 most likely word immediately.

37. **Q: Explain "Beam Search."**
    - **A:** The model looks at multiple possible future sentences at once and picks the one that makes the most sense as a whole, not just the next word.

38. **Q: What is "Repetition Penalty"?**
    - **A:** A setting that makes a word less likely to be chosen if it was just used, preventing the model from saying "the the the the..."

39. **Q: What is "Logits"?**
    - **A:** The raw, unformatted scores the model produces before the "Softmax" turns them into percentages.

40. **Q: Explain "Inference Latency."**
    - **A:** The time it takes for the first word to appear (Time to First Token) and the speed of the rest of the generation.

---

## 📉 Section 2: Quantization & Compression (41-80)

41. **Q: What is Quantization in plain English?**
    - **A:** Shrinking a model by reducing the precision of its numbers. Like turning a high-res photo into a smaller, lower-quality JPEG to save space.

42. **Q: What is "FP16" (Half Precision)?**
    - **A:** Storing numbers using 16 bits instead of the standard 32. It cuts memory in half with almost zero loss in quality.

43. **Q: What is "BF16" (Brain Floating Point)?**
    - **A:** A 16-bit format designed by Google that is more stable for training than FP16 because it can handle much larger numbers.

44. **Q: What is "INT8" quantization?**
    - **A:** Squashing 16-bit numbers into 8-bit integers. It's 2x smaller than FP16 but starts to lose a little bit of "intelligence."

45. **Q: Explain "4-bit Quantization" (e.g., GPTQ, AWQ).**
    - **A:** Compressing the model by 4x. This allows a massive model that normally needs 48GB of RAM to run on a 12GB home computer.

46. **Q: Loss of perplexity during quantization?**
    - **A:** A fancy way of saying "how much stupider the model gets." 4-bit is usually ~99% as good as the original; 2-bit is where it starts to break.

47. **Q: What is GGUF (llama.cpp format)?**
    - **A:** The most popular file format for running quantized models on regular CPUs and Macs. It's designed for "everyday" hardware.

48. **Q: What is GPTQ?**
    - **A:** A method that looks at the data to decide how to squash the numbers without losing too much logic. Great for GPUs.

49. **Q: What is AWQ (Activation-aware Weight Quantization)?**
    - **A:** It realizes that some "weights" are more important than others. It keeps the important ones high-quality and squashes the rest.

50. **Q: Explain "1-bit LLMs" (e.g., BitNet 1.58b).**
    - **A:** A revolutionary architecture where every number is only -1, 0, or 1. It requires almost zero multiplication, making it insanely fast and efficient.

51. **Q: What is the benefit of "1.58 bits" over "1 bit"?**
    - **A:** The extra "0" option allows the model to essentially "turn off" a connection, which dramatically improves intelligence compared to just -1 and 1.

52. **Q: What is "Post-Training Quantization" (PTQ)?**
    - **A:** Compressing the model *after* it's already trained. Fast and easy, but can lose some quality.

53. **Q: What is "Quantization-Aware Training" (QAT)?**
    - **A:** Training the model while telling it "you will be 4-bits later." This helps the model learn to be smart even with low precision.

54. **Q: What is "Sparsification"?**
    - **A:** Pruning (deleting) the least useful parts of the model to make it smaller and faster.

55. **Q: Explain "Distillation."**
    - **A:** Using a giant model (Teacher) to teach a tiny model (Student). The tiny model learns the "essence" of the knowledge without needing 100 billion parameters.

56. **Q: What is "FP8"?**
    - **A:** A new format supported by H100 GPUs. It's the "sweet spot" for modern training and inference, being twice as fast as FP16.

57. **Q: What is a "Calibration Dataset"?**
    - **A:** A small sample of text used during quantization to help the algorithm see which numbers are most important to preserve.

58. **Q: Difference between "Static" and "Dynamic" quantization?**
    - **A:** Static uses fixed squash-rules; Dynamic calculates the best squash-rules on the fly for every word.

59. **Q: What is "Outlier Suppression" in quantization?**
    - **A:** Managing "Extreme" numbers that would normally break a squash-rule, keeping them high-precision so they don't ruin the rest of the data.

60. **Q: Explain "Weight De-quantization" during inference.**
    - **A:** The model is stored in 4-bits but "unpacked" back to 16-bits just for the split-second it takes to do a math calculation.

61. **Q: Why is quantization bad for "Reasoning" tasks sometimes?**
    - **A:** Complex logic (like math or coding) relies on fine details in the numbers. Squashing them can cause "rounding errors" in logic.

62. **Q: What is "K-Quants" (in GGUF)?**
    - **A:** A hybrid method that uses different bit-sizes (e.g., 5-bit for important parts, 4-bit for others) to get the best of both worlds.

63. **Q: What is "EXL2"?**
    - **A:** A super-fast format for NVIDIA GPUs that allows "Expanse" style fine-grained control over exactly how many bits (like 4.25 bits) to use.

64. **Q: Explain "Double Quantization."**
    - **A:** Quantizing the *parameters* that control the quantization itself. It saves an extra few megabytes but adds complexity.

65. **Q: What is "NF4" (NormalFloat 4)?**
    - **A:** A special 4-bit number system used in QLoRA that is mathematically optimized to fit the way neural weights are naturally distributed.

66. **Q: What is "QLoRA"?**
    - **A:** A way to fine-tune a giant model using only 4-bit memory. It made training 70B models possible on a single consumer GPU.

67. **Q: How does Quantization affect context memory?**
    - **A:** Usually, it doesn't. Context is stored in the "KV Cache." You have to quantize the KV Cache separately (e.g., FP8 cache) to save memory there.

68. **Q: What is "Per-channel" vs "Per-tensor" quantization?**
    - **A:** Per-tensor squashes the whole brain with one rule; Per-channel creates custom squash-rules for every individual "neuron connection."

69. **Q: Bit-width vs Model Size?**
    - **A:** Generally: 16-bit = 2GB per 1B parameters. 4-bit = 0.5GB per 1B parameters.

70. **Q: Explain "VRAM" vs "System RAM" for models.**
    - **A:** VRAM (GPU) is 100x faster but 10x more expensive. Quantization allows models to fit in VRAM instead of spilling over to slow System RAM.

71. **Q: What is "HQQ" (Half-Quadratic Quantization)?**
    - **A:** An extremely fast quantization method that doesn't need any calibration data.

72. **Q: Explain "SmoothQuant."**
    - **A:** A technique that "refactors" the math of the model to make it easier to quantize to 8-bit without losing accuracy.

73. **Q: What is "Binary Neural Networks"?**
    - **A:** The extreme version of 1-bit models where every weight is just 0 or 1.

74. **Q: What is "Ternary Neural Networks"?**
    - **A:** Models that use -1, 0, and 1. (This is what BitNet 1.58b is).

75. **Q: Energy efficiency of 1-bit models?**
    - **A:** They can be 10x-70x more energy efficient because they replace expensive multiplications with simple additions.

76. **Q: What is "Hardware-Aware" Quantization?**
    - **A:** Designing the compression specifically for a chip (like Apple's Neural Engine or NVIDIA's Tensor Cores).

77. **Q: What is "Overflow" in quantization?**
    - **A:** When a number is too large to fit into the small 8-bit or 4-bit bucket, resulting in "Infinity" and crashing the model.

78. **Q: What is "Zero-point" quantization?**
    - **A:** Adjusting the "center" of the number system so that 0 in the model aligns perfectly with 0 in the 8-bit integers.

79. **Q: Bit-rate vs Perplexity trade-off?**
    - **A:** As bit-rate goes down, perplexity (error rate) goes up. The goal is to find the "elbow" of the curve where you save the most space for the least error.

80. **Q: Future of 1-bit models on smartphones?**
    - **A:** 1-bit models could allow "GPT-4 level" intelligence to run locally on a phone without draining the battery.

---

## ⚡ Section 3: Performance Tuning & Optimization (81-120)

81. **Q: What is the "KV Cache"?**
    - **A:** Saving the "Keys" and "Values" of previous words so the model doesn't have to re-re-re-calculate them for every new word it generates.

82. **Q: Why does the KV Cache grow?**
    - **A:** Because every new word generated must be added to the memory. This is why long chats get slow or crash.

83. **Q: What is "PagedAttention" (vLLM)?**
    - **A:** Just like computer RAM, it breaks the KV Cache into "pages." This stops memory fragmentation and allows 2x-4x more people to use the same GPU.

84. **Q: Explain "Speculative Decoding."**
    - **A:** A tiny, fast model "guesses" the next 5 words, and the big model just checks if they are correct. If yes, you get 5 words for the price of 1.

85. **Q: What is "Continuous Batching"?**
    - **A:** Instead of waiting for 10 people to finish their chats, you start a new person's chat the second another person's word is finished.

86. **Q: Explain "Compute-bound" vs "Memory-bound".**
    - **A:**
      - **Compute-bound**: The chip is too slow at math.
      - **Memory-bound**: The chip is fast, but the data can't get to it fast enough. (LLMs are almost always memory-bound).

87. **Q: What is "Tensor Parallelism"?**
    - **A:** Splitting a single model across 2 or 4 GPUs. They work together like one giant brain to handle 70B+ models.

88. **Q: What is "Pipeline Parallelism"?**
    - **A:** GPU 1 handles layers 1-10, GPU 2 handles 11-20, etc. Data flows through them like a factory assembly line.

89. **Q: What is "ZeRO" (Zero Redundancy Optimizer)?**
    - **A:** A strategy to delete redundant copies of the model across multiple GPUs to save massive amounts of memory during training.

90. **Q: Explain "Prefill" vs "Decoding" phase.**
    - **A:**
      - **Prefill**: The model reads your whole prompt at once (Fast).
      - **Decoding**: The model generates words one by one (Slow).

91. **Q: What is "Context Caching"?**
    - **A:** If 1,000 people are asking questions about the same 100-page manual, you save the manual's "math" in memory so you don't re-read it 1,000 times.

92. **Q: Explain "Time to First Token" (TTFT).**
    - **A:** How fast the "Prefill" phase is. Crucial for making an agent feel responsive.

93. **Q: Explain "Tokens per Second" (TPS).**
    - **A:** The reading speed of the model. 50+ TPS feels like instant reading; 5 TPS feels like a slow typewriter.

94. **Q: What is "Kernel Fusion"?**
    - **A:** Combining 10 small math steps into 1 big step to reduce the "overhead" of talking to the GPU hardware.

95. **Q: Explain "RoPE Scaling."**
    - **A:** A trick to "stretch" a model trained for 4k context so it can work on 128k context without total retraining.

96. **Q: What is "YaRN" (Yet another RoPE extension)?**
    - **A:** A specific math formula to stretch context windows that keeps the model smarter than simpler methods.

97. **Q: What is "Multi-Query Attention" (MQA)?**
    - **A:** The extreme version of GQA where ALL queries share only 1 Key and 1 Value. It saves max memory but loses some intelligence.

98. **Q: Explain "Attention Sink."**
    - **A:** The discovery that LLMs focus heavily on the very first few tokens. If you delete them from memory, the model breaks.

99. **Q: What is "StreamingLLM"?**
    - **A:** A technique that keeps only the "Attention Sinks" and the most recent words, allowing an agent to chat forever without running out of memory.

100. **Q: What is "Chunked Prefill"?**
    - **A:** Breaking a 100k prompt into smaller pieces so it doesn't "lag" the whole GPU while it's being read.

101. **Q: Explain "vLLM" vs "TGI" (Text Generation Inference).**
    - **A:** Two popular "engines" for running LLMs in production. vLLM is famous for PagedAttention; TGI for being very stable.

102. **Q: What is "Model Sharding"?**
    - **A:** Breaking a large model file into smaller 5GB pieces so it's easier to download and load into memory.

103. **Q: Explain "Offloading" (CPU/Disk Offloading).**
    - **A:** Putting parts of the model on the CPU or Hard Drive if the GPU is full. It works, but it's 10x-100x slower.

104. **Q: What is "CUDA Graph"?**
    - **A:** Recording a sequence of GPU commands and playing them back like a macro to save time on every word.

105. **Q: Explain "NCCL" (NVIDIA Collective Communications Library).**
    - **A:** The "Internet" for GPUs. It's the high-speed software that lets GPUs talk to each other inside a server.

106. **Q: What is "NVLink"?**
    - **A:** The physical high-speed bridge between NVIDIA GPUs that is way faster than standard PCIe slots.

107. **Q: Explain "FP8 training" benefits.**
    - **A:** It allows for 2x faster training and fits 2x larger batches, which effectively cuts the cost of training a model in half.

108. **Q: What is "LoRA" (Low-Rank Adaptation)?**
    - **A:** Instead of training the whole 70B model, you only train a tiny "adapter" (like a patch). It's 1,000x more efficient.

109. **Q: Explain "Rank" in LoRA.**
    - **A:** The "thickness" of the adapter. Higher rank = more knowledge learned, but more memory used.

110. **Q: What is "Gradient Checkpointing"?**
    - **A:** Deleting intermediate math during training and re-calculating it later to save memory. (Trade-off: slower training for less RAM).

111. **Q: Explain "DeepSpeed."**
    - **A:** A library from Microsoft that makes it easy to train massive models across hundreds of GPUs.

112. **Q: What is "FSDP" (Fully Sharded Data Parallel)?**
    - **A:** Meta's version of ZeRO. It's the standard way Llama 3 models are trained today.

113. **Q: What is "Precision Mismatch"?**
    - **A:** When you try to run an FP16 model on hardware that only likes BF16, leading to weird errors or "NaN" outputs.

114. **Q: Explain "Throughput" vs "Latency."**
    - **A:**
      - **Throughput**: How many total words processed per second for 1,000 users.
      - **Latency**: How fast 1 individual user gets their specific answer.

115. **Q: What is "Token Bucket" rate limiting?**
    - **A:** A way to smooth out traffic so the GPU doesn't get overwhelmed by a "burst" of users.

116. **Q: Explain "Prompt Bottleneck."**
    - **A:** When your prompt is so long that the model spends all its time "reading" and has no memory left to "answer."

117. **Q: What is "System-2 Thinking" in models?**
    - **A:** Forced reasoning (like o1) where the model spends 30 seconds "thinking" to itself before giving you the first word.

118. **Q: How does System-2 Thinking affect pricing?**
    - **A:** You pay for the "thinking tokens" the model uses internally, even if you never see them.

119. **Q: What is "Compute Optimal" (Chinchilla Scaling)?**
    - **A:** The discovery that for every 2x increase in model size, you should also 2x the amount of training data.

120. **Q: What is "Over-training"?**
    - **A:** Training a small model on way more data than "Chinchilla" suggests. (e.g. Llama 3 was over-trained to make it smarter while staying small).

---

## 🧠 Section 4: Embeddings, Context & Reasoning (121-160)

121. **Q: What is an Embedding Vector?**
    - **A:** A coordinate in a 1,000+ dimensional space. "Cat" and "Kitten" will have coordinates that are very close to each other.

122. **Q: Explain Cosine Similarity.**
    - **A:** A math way to measure the "angle" between two vectors. Small angle = very similar meaning.

123. **Q: What is a "Bi-Encoder"?**
    - **A:** A model that turns text into a vector independently. Fast for searching millions of docs.

124. **Q: What is a "Cross-Encoder"?**
    - **A:** A model that looks at two pieces of text *together* to see how they relate. Slow, but much more accurate for ranking.

125. **Q: Explain "Long-form Context" challenges.**
    - **A:** Even if a model *can* read 1 million tokens, it often "forgets" what happened in the middle (Lost in the Middle).

126. **Q: What is "Reranking"?**
    - **A:** 1. Use a fast Bi-Encoder to find 100 docs. 2. Use a smart Cross-Encoder to pick the best 5.

127. **Q: Explain "Semantic Chunking."**
    - **A:** Instead of breaking text every 500 characters, you break it whenever the *topic* changes.

128. **Q: What is "Dense" vs "Sparse" retrieval?**
    - **A:**
      - **Dense**: Mathematical meaning (Embeddings).
      - **Sparse**: Exact word matches (Keyword search).

129. **Q: What is "Hybrid Search"?**
    - **A:** Combining Dense and Sparse search to get the benefits of both.

130. **Q: Explain "Vector Database" indexing (e.g., HNSW).**
    - **A:** A way to organize vectors so you can find the "nearest neighbor" without checking every single doc in the database.

131. **Q: What is "Prompt Compression"?**
    - **A:** Using a small AI to delete useless words from your prompt to save tokens before sending it to the big expensive model.

132. **Q: What is "Self-Querying"?**
    - **A:** The AI looks at your question and decides what "Filter" to apply to the vector database (e.g., "Find docs from 2024").

133. **Q: Explain "Knowledge Distillation" for embeddings.**
    - **A:** Making a small embedding model as good as a giant one by having it mimic the giant model's vector outputs.

134. **Q: What is "Dimension Reduction" (PCA)?**
    - **A:** Shrinking a 1,536-size vector to 256-size while trying to keep the relationships intact.

135. **Q: Explain "Vector Quantization" (Product Quantization).**
    - **A:** Compressing the vector database itself so you can store 1 billion docs in RAM.

136. **Q: What is "In-context Learning"?**
    - **A:** The model's ability to learn a new skill just by seeing examples in your prompt (Few-shot).

137. **Q: Explain "Instruction Tuning."**
    - **A:** The specific training that turns a "Base" model (which just predicts next words) into an "Assistant" (which follows orders).

138. **Q: What is "RLHF" (Reinforcement Learning from Human Feedback)?**
    - **A:** Humans rank AI answers from "Best" to "Worst," and the model learns to produce more "Best" answers.

139. **Q: Explain "DPO" (Direct Preference Optimization).**
    - **A:** A simpler, faster way to do RLHF without needing a separate "Reward Model."

140. **Q: What is "PPO" (Proximal Policy Optimization)?**
    - **A:** The classic, more complex algorithm used to train ChatGPT's personality.

141. **Q: What is "Constitutional AI" (Anthropic)?**
    - **A:** Having an AI model use a "set of rules" (a constitution) to train another AI, instead of relying only on human rankers.

142. **Q: Explain "Self-Play Alignment."**
    - **A:** Two AI models debating each other to find the most logical and safe answer.

143. **Q: What is "Over-refusal"?**
    - **A:** When a model is trained so strictly for safety that it refuses to help with harmless tasks (e.g., "I can't tell you how to kill a computer process").

144. **Q: Explain "Reward Hacking."**
    - **A:** When an AI finds a "cheat" to get a high score from its reward model without actually being helpful (e.g., being overly polite but empty).

145. **Q: What is "Chain of Thought" (CoT) fine-tuning?**
    - **A:** Training the model on datasets that include the "internal thoughts" so it learns to reason better naturally.

146. **Q: What is "Tree of Thoughts"?**
    - **A:** An advanced pattern where the AI generates multiple reasoning paths, critiques them, and follows the most promising one.

147. **Q: Explain "Self-Consistency" in reasoning.**
    - **A:** Asking the model the same math question 5 times and picking the answer that appears most often.

148. **Q: What is "Logical Probing"?**
    - **A:** Testing if a model actually understands a concept by asking it to explain the *inverse* of its logic.

149. **Q: Explain "Step-level Reinforcement Learning."**
    - **A:** Giving the model a "reward" for every individual correct step in a math problem, rather than just the final answer.

150. **Q: What is "Process Reward Models" (PRM)?**
    - **A:** A model that is trained to grade the *steps* of an argument, not just the conclusion.

151. **Q: Explain "Knowledge Cutoff."**
    - **A:** The literal date the model's training data ended. It knows nothing about the world after that date without RAG.

152. **Q: What is "Catastrophic Forgetting"?**
    - **A:** When fine-tuning a model on a new skill (e.g., Coding) causes it to "forget" its old skill (e.g., Writing Poems).

153. **Q: Explain "Alignment Tax."**
    - **A:** The fact that making a model "safe and helpful" usually makes it slightly worse at raw logic or creativity.

154. **Q: What is "Sycophancy" in LLMs?**
    - **A:** The tendency of models to agree with the user even if the user is wrong, just to be "helpful."

155. **Q: Explain "Hallucination Snowballing."**
    - **A:** When a model makes one small mistake early on and then invents a giant lie to try and stay consistent with that first mistake.

156. **Q: What is "Token-level reasoning"?**
    - **A:** The idea that reasoning happens *between* the generation of tokens.

157. **Q: Explain "Internal Monologue."**
    - **A:** A technique where the model writes its thoughts in a hidden <thought> tag before giving the final answer.

158. **Q: What is "Multi-step Deduction"?**
    - **A:** If A=B and B=C, does the model know A=C? Surprisingly hard for small models without CoT.

159. **Q: Explain "Zero-shot CoT" ("Let's think step by step").**
    - **A:** The discovery that simply adding that one phrase to a prompt dramatically increases reasoning scores.

160. **Q: Future of Reasoning Models (System 1 vs System 2).**
    - **A:** Moving from "Instant Chat" (System 1) to "Deep Problem Solving" (System 2) that takes time but produces flawless results.

---

## 🏗️ Section 5: Training, Hardware & Future Architectures (161-200)

161. **Q: What is a "Parameter"?**
    - **A:** A single number in the neural network's equations. GPT-3 has 175 billion of them.

162. **Q: Explain "Billion" (B) vs "Trillion" (T) parameter models.**
    - **A:** More parameters generally allow for more multi-lingual capability and deeper factual knowledge, but require more hardware.

163. **Q: What is a "GPU Tensor Core"?**
    - **A:** A special part of an NVIDIA GPU designed for 1 task only: multiplying giant matrices of numbers (the core work of AI).

164. **Q: Explain "HBM" (High Bandwidth Memory).**
    - **A:** Super-fast specialized RAM used on GPUs (like H100s). It is the main "limiting factor" for LLMs today.

165. **Q: What is "SRAM" vs "DRAM" on a chip?**
    - **A:** SRAM is tiny but instant (on the chip); DRAM is big but slower (attached to the chip). Flash Attention optimizes for this.

166. **Q: Explain "Model Sharding."**
    - **A:** Dividing the model layers across different physical storage units.

167. **Q: What is "Distributed Training"?**
    - **A:** Using 10,000+ GPUs to train a single model by syncing their math every few milliseconds.

168. **Q: Explain "Gradient descent."**
    - **A:** The math process of nudging the model's numbers slightly after every mistake until the error is minimized.

169. **Q: What is an "Epoch"?**
    - **A:** One complete pass of the model through the entire training dataset.

170. **Q: Explain "Learning Rate."**
    - **A:** How "big" of a nudge to give the parameters during training. Too big and the model breaks; too small and it takes forever.

171. **Q: What is a "Transformer Block"?**
    - **A:** The repeating unit (Attention + Feed Forward) that is stacked 32-100 times to create the model's depth.

172. **Q: Explain "State Space Models" (e.g., Mamba).**
    - **A:** A new architecture that is *Linear* (not quadratic) and doesn't use attention, making it much faster for long documents.

173. **Q: What is "Recurrent Memory" in modern models?**
    - **A:** Trying to bring back RNN-style memory to Transformers so they can "remember" without a big KV cache.

174. **Q: Explain "Linear Transformers."**
    - **A:** A modified attention that calculates "Meanings" without comparing every word to every other word.

175. **Q: What is "Token-free" / "Pixel-based" models?**
    - **A:** Models that look at the raw pixels of text on a screen instead of using a vocabulary of tokens.

176. **Q: Explain "World Models."**
    - **A:** AI that isn't just predicting text but is trying to simulate the actual laws of physics and reality (like SORA).

177. **Q: What is "Multimodal" (Native vs Adapter)?**
    - **A:** Native means the model was trained on text/image/audio together. Adapter means you "glued" a vision model to a text model.

178. **Q: Explain "Cross-Modal Attention."**
    - **A:** How an AI "looks" at a specific part of an image while writing a specific part of a sentence.

179. **Q: What is "Retrieval-Augmented Training" (RETRO)?**
    - **A:** A model that is built to "search" as its core way of thinking, rather than just memorizing facts in its weights.

180. **Q: Explain "LongRoPE."**
    - **A:** A specialized version of RoPE that allows models to reach context windows of 2 million tokens or more.

181. **Q: What is "Quantization Error"?**
    - **A:** The math difference between the original 16-bit answer and the new 4-bit compressed answer.

182. **Q: Explain "Dynamic Batching."**
    - **A:** Grouping different people's questions together based on their length to maximize GPU usage.

183. **Q: What is "Model Pruning"?**
    - **A:** Identifying "Dead" neurons that don't contribute to output and deleting them entirely.

184. **Q: Explain "Sparse Attention."**
    - **A:** The model only attends to a few "Global" words and a few "Local" neighbors to save math.

185. **Q: What is "Memory-efficient Attention"?**
    - **A:** Techniques like XFormers that reduce the "Peak RAM" needed during the attention math.

186. **Q: Explain "Layer-wise Optimal Brain Surgeon."**
    - **A:** An advanced way to prune models by mathematically identifying exactly which weights won't be missed.

187. **Q: What is "Weights & Biases" (WandB)?**
    - **A:** A popular tool for developers to watch "Charts and Graphs" of their model's performance while it trains.

188. **Q: Explain "Model Zoo."**
    - **A:** Collection of pre-trained models (like HuggingFace) that you can download and use immediately.

189. **Q: What is "Inference Optimization"?**
    - **A:** The overall science of making an LLM run fast and cheap enough for a real website.

190. **Q: Explain "On-device AI."**
    - **A:** Small, highly-quantized models (1B-3B) tailored for phone or laptop processors.

191. **Q: What is "Liquid Neural Networks"?**
    - **A:** Models that can change their "math equations" on the fly based on the input they see.

192. **Q: Explain "BitNet 1.58b" architecture specifics.**
    - **A:** It removes the "Matrix Multiplication" and replaces it with "Matrix Addition," fundamentally changing how chips work.

193. **Q: What is "FP4" quantization?**
    - **A:** A 4-bit format that uses "Floating Point" logic instead of Integers, favored by newer chips.

194. **Q: Explain "Sequence Parallelism."**
    - **A:** Scaling a single 1-million length context chat across 8 GPUs so it fits in memory.

195. **Q: What is "Pipeline Bubble"?**
    - **A:** The wasted time when one GPU is waiting for another GPU to finish its "layer" of the work.

196. **Q: Explain "Speculative Execution" in agents.**
    - **A:** An agent starting "Step 2" while "Step 1" is still being finalized to save time.

197. **Q: What is "LLM-as-a-Judge"?**
    - **A:** Using the most powerful model (GPT-4) to create the "Answer Key" for training smaller models.

198. **Q: Explain "RLAIF" (RL from AI Feedback).**
    - **A:** Replacing human rankers with AI rankers to speed up the alignment process.

199. **Q: What is "Instruction Over-fitting"?**
    - **A:** When a model becomes so good at following "Test Instructions" that it loses its ability to think outside of those specific prompts.

200. **Q: The future of "Infinite Context"?**
    - **A:** The shift from "Fixed RAM" to "Streaming Vector Memory" where models can remember years of conversation in real-time.
