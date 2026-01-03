# Recommender Assignments

## Objective
Build engines that suggest movies or products.

## Prerequisites
- `pip install scikit-surprise` (A great library for recommenders)

## Practical Assignments

### Assignment 1: Content-Based Movie Recommender
**Goal:** Recommend based on Genre.
1.  Create a tiny dataset:
    *   `Movies = [{"id": 1, "genres": "Action, Sci-Fi"}, {"id": 2, "genres": "Romance"}]`
2.  Use TF-IDF Vectorizer on the "genres" string.
3.  Calculate **Cosine Similarity** between all movies.
4.  Function `recommend(movie_id)`: returns the top 3 most similar movies.

### Assignment 2: Collaborative Filtering (SVD)
**Goal:** Predict missing ratings.
1.  Load the **MovieLens 100k** dataset (built into `surprise`).
2.  Use the `SVD` (Singular Value Decomposition) algorithm.
3.  Train on 75% of data.
4.  Predict the specific rating User X will give to Movie Y.
5.  Evaluate RMSE.

### Assignment 3: The Cold Start Problem
**Goal:** Handle a new user.
1.  Add a new user "Rakesh" to the dataset who has rated NOTHING.
2.  Try to predict ratings for him. (Observe the result).
3.  *Fix*: Implement a fallback strategy (e.g., Recommend the globally most popular movies).

## Conceptual Quiz
1.  Why is "Sparsity" a problem in a 1 Million User x 10,000 Item matrix?
2.  What is the "Harry Potter Problem" (Popularity Bias)?
3.  How does a Hybrid Recommender work?
