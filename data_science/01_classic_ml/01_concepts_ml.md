# Classical Machine Learning Concepts

## 1. Types of Learning
- **Supervised Learning**: Teacher exists. You have input (X) and label (Y).
    - *Tasks*: Regression (Predict number), Classification (Predict category).
- **Unsupervised Learning**: No Teacher. Only input (X).
    - *Tasks*: Clustering (Grouping), Dimensionality Reduction (Compression).
- **Reinforcement Learning**: Learn by trial and error (Reward/Penalty).

## 2. Core Algorithms
- **Linear Regression**: Fitting a straight line ($y = mx + c$). Good for predicting house prices.
- **Logistic Regression**: It's a classifier! Uses Sigmoid function to squash output between 0 and 1. Good for Spam/Not Spam.
- **Decision Trees**: If-Else flowchart learned from data. Prone to overfitting.
- **Random Forest**: Averaging 100 Decision Trees to fix the overfitting. (Bagging).
- **SVM (Support Vector Machines)**: Finding the widest street (margin) between two classes.
- **K-Means**: Finding K centers in a cloud of points and grouping them.

## 3. The Bias-Variance Tradeoff (Critical Concept)
- **High Bias (Underfitting)**: Model is too simple. It misses the trend. (e.g., fitting a line to a curve).
    - *Fix*: Make model more complex.
- **High Variance (Overfitting)**: Model is too complex. It memorizes the noise. (e.g., connecting every dot with a squiggly line).
    - *Fix*: Get more data, regularization, or simplify model.

## 4. Evaluation Metrics
- **Accuracy**: % Correct. Bad for imbalanced data (99% generic health vs 1% cancer).
- **Precision**: "Of all the times you said Cancer, how many were right?" (Don't scare patients).
- **Recall**: "Of all the actual Cancer cases, how many did you find?" (Don't let patients die).
- **F1-Score**: Harmonic mean of Precision and Recall.
- **RMSE (Root Mean Squared Error)**: Standard metric for Regression errors.
