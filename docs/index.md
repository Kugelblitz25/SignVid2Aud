# Sign2Speech: Converting Sign Language to Audio without Text Intermediaries

Welcome to the Sign2Speech project documentation. This innovative project aims to convert American Sign Language (ASL) videos directly into speech without using text intermediaries, making communication between signers and non-signers more natural and accessible.

## Navigation

- [Project Overview](#project-overview)
- [ASL Info](asl_info.md)
- [Technical Architecture](architecture.md)
- [Dataset Information](datasets.md)
- [Experiments & Results](experiments.md)
- [Installation & Usage](installation.md)
- [Future Work](future.md)

# Project Overview

## Abstract

Sign2Speech presents a novel end-to-end approach for converting American Sign Language (ASL) videos directly into speech without text intermediaries. Our system combines three key components:
- An I3D network fine-tuned on the WLASL dataset for feature extraction
- A custom feature transformer model for mel-spectrogram generation
- A HiFi-GAN vocoder for high-quality audio synthesis

The primary innovation lies in our direct video-to-audio pipeline, which eliminates the need for text-based intermediary steps commonly used in existing systems.

## Key Features

- Direct video-to-audio conversion without text intermediaries
- Novel temporal synchronization techniques
- Modified non-maximal suppression for continuous sign processing
- Real-time communication capabilities

## Applications

1. Real-time communication assistance in everyday interactions
2. Educational settings where deaf students interact with hearing teachers
3. Professional environments to facilitate seamless workplace communication
4. Public services and emergency response situations


## Get Involved

- [Project Repository](https://github.com/Kugelblitz25/sign2speech/)
- [Download Pre-trained Weights](https://drive.google.com/drive/folders/150wd1GsVxnIXq3btG0EEhhXS9gBYnJ2f?usp=sharing)
- [Report Issues](https://github.com/Kugelblitz25/sign2speech/issues)