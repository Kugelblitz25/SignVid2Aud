# Dataset Information

## WLASL Dataset

### Overview
- Total Glosses: 2000 (Project focused on top 100)
- Number of Videos: 12,000 (958 videos for 100 glosses)
- Type: Video data

### Structure
JSON file with attributes:
- gloss: Sign language word/sign name
- instances: Video instance information
- bbox: Bounding box coordinates
- fps: 25 frames per second
- signer_id: Unique performer identifier

### Preprocessing
1. Video Cropping
2. Data Augmentation
   - Rotation
   - Brightness adjustment
   - Hue modification
   - Saturation alteration
3. Subsampling
4. Normalization

## Tacotron-2 Features

### Overview
- Format: CSV
- Dimensions: 100 rows × 7041 columns
- Data types: Text (words) and numerical features (spectrograms)

### Processing Pipeline
Text → Tokens → Tacotron2 → Padding → Feature Transformer