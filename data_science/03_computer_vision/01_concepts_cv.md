# Computer Vision Concepts

## 1. Images as Numbers
To a computer, an image is a 3D Matrix: `(Height, Width, Channels)`.
- **Gray**: 1 Channel (Brightness).
- **RGB**: 3 Channels (Red, Green, Blue).
- Values are 0-255.

## 2. Convolutions (The "C" in CNN)
A "Fully Connected" network fails on images because it loses spatial info (it flattens the cat).
**Convolution**: Scanning a small filter (Kernel) over the image.
- **Filters learn features**: One filter might learn "Vertical Edges". Another learns "Curves".
- **Translation Invariance**: If a cat moves to the right, the filter still finds it.

## 3. Pooling
- **Max Pooling**: Taking the biggest number in a 2x2 square.
- **Why?**: reduce size (downsampling) and computation. Also adds robustness to small shifts.

## 4. Modern Architectures
- **ResNet**: Uses "Skip Connections" to allow Deep networks (150+ layers) without gradients vanishing.
- **YOLO (You Only Look Once)**: Real-time Object Detection. Instead of scanning window by window, it splits image into a grid and predicts bounding boxes in parallel.

## 5. Augmentation
Artificially increasing data by rotating, zooming, or flipping images. Critical for CV to prevent overfitting.
