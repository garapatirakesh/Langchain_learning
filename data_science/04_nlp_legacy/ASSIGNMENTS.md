# NLP Assignments

## Objective
From counting words to understanding sequences.

## Practical Assignments

### Assignment 1: Spam Filter (Classical)
**Goal:** text classification with TF-IDF.
1.  Load a Spam/Ham dataset.
2.  Use `TfidfVectorizer` to convert text to numbers.
3.  Train a **Naive Bayes** classifier.
4.  Test it on: "Win a a free iPhone" vs "Hey mom, how are you?".

### Assignment 2: Word Arithmetic
**Goal:** Play with Embeddings.
1.  Load pre-trained GloVe vectors (using `gensim`).
2.  Perform vector math: `Result = Vector(Paris) - Vector(France) + Vector(Italy)`.
3.  Find the most similar word to `Result` (Should be "Rome").

### Assignment 3: Next Word Predictor (RNN)
**Goal:** Build a baby language model.
1.  Take a text file (e.g., Shakespeare).
2.  Create dataset of sequences: Input="To be or not to", Target="be".
3.  Train an **LSTM** or **GRU** layer -> Linear layer.
4.  Generate text by predicting next word, feeding it back in, and repeating.

## Conceptual Quiz
1.  Why is "One-Hot Encoding" bad for a vocabulary of 50,000 words?
2.  What is the limitation of Word2Vec for the word "Apple" (Fruit vs Company)?
3.  How does TF-IDF decide a word is "unimportant"?
