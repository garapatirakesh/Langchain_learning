# Data Science & AI Interview Questions

## Common Theory Questions

### 1. What is the Bias-Variance Tradeoff?
*Answer*: It is the balance between a model that is too simple (High Bias, Underfitting) and too complex (High Variance, Overfitting). The goal is to find the sweet spot where the model generalizes well to new data.

### 2. Explain Gradient Descent to a 5-year-old.
*Answer*: Imagine you are on a mountain at night (blindfolded). You want to reach the village at the bottom (Lowest Error). You feel the slope of the ground structure under your feet. If it goes down, you take a step that way. You keep taking small steps downhill until the ground is flat.

### 3. Precision vs Recall: When to use which?
*Answer*:
- **Precision**: Use when False Positives are costly (e.g., Email Spam - don't send important work email to junk).
- **Recall**: Use when False Negatives are costly (e.g., Cancer detection - better to double check a healthy person than miss a sick one).

### 4. What is the difference between Batch, Stochastic, and Mini-Batch Gradient Descent?
- **Batch**: Use ALL data to calculate 1 step. Slow but stable.
- **Stochastic**: Use 1 example to calculate 1 step. Fast but noisy/bumpy.
- **Mini-Batch**: Use 32 or 64 examples. The best of both worlds.

### 5. Why do Vanishing Gradients happen?
*Answer*: In deep networks (especially RNNs using Sigmoid/Tanh), the derivative is often a small number (< 1). When you multiply small numbers many times (Chain Rule), they become zero. The network stops learning. **ReLU** and **LSTMs** help fix this.

## Coding/Practical Checks

### 1. How do you handle imbalanced datasets?
- Resampling: Oversample minority class (SMOTE) or Undersample majority class.
- Metric change: Use F1-Score instead of Accuracy.
- Class Weights: Tell the Loss function to punish errors on the minority class more.

### 2. How to clean data?
- Handle Missing Values: Mean imputation, median imputation, or drop rows.
- Remove Duplicates.
- Handle Outliers (Z-Score or IQR).
- Standardize/Normalize numerical features.

### 3. Explain CNN Pooling.
*Answer*: Dimensionality reduction. Max Pooling takes the largest value in a window. It reduces the computational load and makes the model invariant to small translations (shifting pixels).
