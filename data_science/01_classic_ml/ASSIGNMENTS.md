# Classical ML Assignments

## Objective
Master Scikit-Learn (sklearn) and data manipulation with Pandas.

## Prerequisites
- Python
- Pandas (`pip install pandas`)
- Scikit-Learn (`pip install scikit-learn`)

## Practical Assignments

### Assignment 1: House Price Predictor (Regression)
**Goal:** Predict continuous values.
1.  Load the **California Housing Dataset** (`sklearn.datasets.fetch_california_housing`).
2.  Split data into Train (80%) and Test (20%).
3.  Train a **Linear Regression** model.
4.  Evaluate using **RMSE** (Root Mean Squared Error).
5.  *Challenge*: Try a **RandomForestRegressor** and compare the RMSE.

### Assignment 2: Titanic Survivor (Classification)
**Goal:** Handle categorical data and predict binary outcomes.
1.  Download Titanic dataset (or load from seaborn).
2.  Preprocess: Fill missing ages, encode "Sex" (Male=0, Female=1).
3.  Train a **Logistic Regression** model.
4.  Evaluate using **Accuracy** and **Confusion Matrix**.
5.  *Challenge*: Calculate the **F1-Score**.

### Assignment 3: Customer Segmentation (Clustering)
**Goal:** Group data without labels.
1.  Generate blobs of data (`sklearn.datasets.make_blobs`).
2.  Use **K-Means Clustering** with `K=3`.
3.  Visualize the clusters using Matplotlib (color points by their cluster label).
4.  *Challenge*: Use the **Elbow Method** to find the optimal K.

## Conceptual Quiz
1.  Why is Accuracy a bad metric for fraud detection models?
2.  What is the difference between specific "Parameters" and "Hyperparameters"?
3.  How does K-Fold Cross Validation help prevent overfitting?
