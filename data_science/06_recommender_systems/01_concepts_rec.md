# Recommender Systems Concepts

## 1. The Goal
To predict **"Rating"** (how much a user will like an item) or **"Ranking"** (what is the next best item to show).

## 2. Types of Recommenders

### A. Content-Based Filtering
*   **Logic**: "You liked Item A. Item B is similar to Item A. So you will like Item B."
*   **How**: Use features of the item.
    *   Movie: Genre, Director, Actors.
    *   Books: Author, Keywords.
*   **Pros**: Doesn't need other users' data. Good for new items (Cold Start).
*   **Cons**: No serendipity. You never get recommended something outside your "bubble".

### B. Collaborative Filtering (User-User)
*   **Logic**: "You are similar to Alice. Alice liked Item C. So you will like Item C."
*   **How**: Find users who rated items similarly to you.
*   **Pros**: serendipitous. Can recommend completely new categories.
*   **Cons**: Cold Start Problem (New users have no history). Sparsity (Most users haven't rated most items).

### C. Matrix Factorization (SVD)
*   **The Math**: Decomposing the huge User-Item Matrix into two smaller matrices: User-Factors and Item-Factors.
*   **Latent Factors**: The math discovers hidden features (e.g., "User likes Action" vs "User likes Romance") without being explicitly told.
*   **Netflix Prize**: This technique won the famous \$1M Netflix competition.

## 3. Deep Learning Recommenders (NCF)
*   **Neural Collaborative Filtering**: Using Neural Networks instead of simple dot products to learn the interaction between User and Item embeddings.
*   **Two-Tower Models**: Standard industry architecture (YouTube/TikTok).
    *   Tower 1 encodes User History -> User Vector.
    *   Tower 2 encodes Video Features -> Item Vector.
    *   Dot Product -> Probability of Watch.

## 4. Metrics
*   **RMSE**: For predicting specific ratings (3.5 stars vs 4 stars).
*   **Map@K (Mean Average Precision at K)**: "If I show you 5 items, how many are actually relevant?"
