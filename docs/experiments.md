# Experiments & Results

## I3D Model Experiments

### 2000 Glosses
- Initial attempt with full dataset
- Challenges:
  - Long training time (3-4 hours per epoch)
  - Heavy overfitting
  - Data sparsity and class imbalance

### 100 Glosses
- Fine-tuned on top 100 glosses
- Architecture modifications:
  - Frozen initial layers
  - Layer normalization
  - Various classifier heads tested
- Learning rate optimization: 0.0001 found optimal

## Audio Generation Experiments

### 1. Librosa and HiFi-GAN
- Results: High-pitched sounds, not meaningful
- Adequacy: Poor
- Fluency: Poor

### 2. Librosa Only
- Results: Meaningful but robotic
- Adequacy: Good
- Fluency: Poor

### 3. Tacotron2 and HiFi-GAN
- Results: Human-like, meaningful audio
- Adequacy: Good
- Fluency: Good

## Performance Metrics

![I3D Training Results](assets/i3d_results.png)
![MLP Training Results](assets/mlp_results.png)