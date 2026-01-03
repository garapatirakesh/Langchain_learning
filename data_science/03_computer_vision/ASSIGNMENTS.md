# Computer Vision Assignments

## Objective
Build eyes for the machine using CNNs.

## Prerequisites
- `pip install opencv-python matplotlib`

## Practical Assignments

### Assignment 1: The Edge Detector
**Goal:** Understand Kernels.
1.  Load an image in Grayscale.
2.  Define a **Sobel Filter** (Vertical Edge Kernel): `[[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]`.
3.  Apply `cv2.filter2D` using this kernel.
4.  Visualize the result (You should see white lines on edges).

### Assignment 2: CIFAR-10 Classification
**Goal:** Build a CNN.
1.  Load CIFAR-10 (Tiny color images of planes, cars, birds...).
2.  Build a CNN:
    - Conv2D(32) -> ReLU -> MaxPool.
    - Conv2D(64) -> ReLU -> MaxPool.
    - Flatten -> Linear -> Output.
3.  Train it.
4.  *Challenge*: Use Data Augmentation (RandomHorizontalFlip) to improve accuracy.

### Assignment 3: Transfer Learning (The Pro Move)
**Goal:** Use a pre-trained brain.
1.  Load a pre-trained **ResNet18** from `torchvision.models`.
2.  Freeze weights (`param.requires_grad = False`).
3.  Replace the last layer (`fc`) with a new Linear layer for your classes (e.g., 2 classes: Cat vs Dog).
4.  Train ONLY the last layer.
5.  Experience the speed and accuracy boost.

## Conceptual Quiz
1.  What is the difference between Object Detection (YOLO) and Image Classification (ResNet)?
2.  Why is Max Pooling destructive?
3.  What is a "Stride"?
