# Deep Learning Assignments

## Objective
Understand the mechanics of Neural Networks using PyTorch or TensorFlow.

## Prerequisites
- `pip install torch torchvision`

## Practical Assignments

### Assignment 1: The Linear Neuron
**Goal:** Implement gradients manually (Understanding Autograd).
1.  Define a tensor `x = 2.0` with `requires_grad=True`.
2.  Define function `y = x**2 + 5*x`.
3.  Calculate `y` and call `y.backward()`.
4.  Print `x.grad`. Verify it matches the derivative ($2x + 5 = 9$).

### Assignment 2: MNIST Classifier (The "Hello World" of DL)
**Goal:** Build a Feed-Forward Network (MLP).
1.  Load MNIST dataset (Handwritten digits).
2.  Create an `nn.Sequential` model:
    - Linear(784, 128) -> ReLU -> Linear(128, 10).
3.  Use **CrossEntropyLoss** and **Adam** optimizer.
4.  Train for 5 epochs.
5.  *Challenge*: Get >97% accuracy.

### Assignment 3: Overfitting Trap
**Goal:** Visualize overfitting.
1.  Train a HUGE network (e.g., 5 layers of 512 units) on a TINY amount of data (e.g., 50 images).
2.  Watch Training Loss go to 0.
3.  Watch Test Loss go UP (or stay high).
4.  *Challenge*: Fix it using **Dropout** (`nn.Dropout(0.5)`).

## Conceptual Quiz
1.  Why do we need "Non-Linearity" (ReLU)?
2.  What happens if your Learning Rate is too high?
3.  What is the purpose of a "Batch" in Mini-Batch Gradient Descent?
