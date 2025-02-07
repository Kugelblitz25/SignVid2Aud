# Technical Architecture

## System Components

### 1. Video Feature Extraction (I3D Model)
- Base Model: Inception-3D (I3D) pre-trained on Kinetics dataset
- Input Dimensions: [-1, 3, 32, 224, 224]
- Output Dimensions: [-1, 2048]
- Additional dense layers for 100-class classification

### 2. Feature Transformer Model
Architecture:
```
MLP Layers:
- Linear-1: 1024 units with BatchNorm and ReLU
- Linear-4: 512 units with BatchNorm and ReLU
- Linear-7: 256 units with BatchNorm and ReLU
- Linear-10: 1408 units with BatchNorm and ReLU
- Linear-13: 1760 units

De-convolution Layers:
- Layer 14: Output shape [64, 10, 22]
- Layer 16: Output shape [32, 20, 44]
- Layer 18: Output shape [16, 40, 88]
- Layer 20: Output shape [1, 80, 88]
```

### 3. Audio Generation Pipeline
- HiFi-GAN Vocoder (NVIDIA's NeMo)
- Input: Spectrograms [1, 80, 88]
- Output: Raw audio waveform (22050 Hz)