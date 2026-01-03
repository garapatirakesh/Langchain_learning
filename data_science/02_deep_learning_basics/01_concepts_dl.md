# Deep Learning Basics

## 1. The Perceptron vs Multi-Layer Perceptron (MLP)
- **Perceptron**: Can only solve linear problems (draw a straight line). Fails at simple XOR logic.
- **MLP**: Adding "Hidden Layers" allows the network to fold space and solve non-linear problems.

## 2. Activation Functions
They decide "Does this neuron fire?". Without them, a Neural Network is just big Linear Regression.
- **Sigmoid**: Squashes to (0, 1). Old school. Problem: Vanishing Gradient.
- **ReLU (Rectified Linear Unit)**: `max(0, x)`. If positive, pass it. If negative, zero. Fast and Standard.
- **Softmax**: Converts a list of numbers into Probabilities (sum = 1). Used in Output layer for classification.

## 3. Loss Functions
How do we measure "Error"?
- **MSE (Mean Squared Error)**: For Regression.
- **Cross-Entropy Loss (Log Loss)**: For Classification. It punishes confident wrong answers heavily.

## 4. Optimizers
How do we update weights?
- **SGD (Stochastic Gradient Descent)**: Basic. Updates based on small batches. Can get stuck in "Valleys".
- **Adam (Adaptive Moment Estimation)**: The Gold Standard. It uses momentum (like a ball rolling down a hill). It speeds up in flat areas and slows down in sharp turns.
