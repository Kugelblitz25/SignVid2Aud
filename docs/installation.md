# Installation & Usage

## Prerequisites
- Python 3.8+
- CUDA-compatible GPU
- 32GB RAM minimum

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Kugelblitz25/sign2speech.git
cd sign2speech
```

2. Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Project

### Training

1. Download and prepare dataset:
```bash
curl -L -o archive.zip 'https://www.kaggle.com/api/v1/datasets/download/risangbaskoro/wlasl-processed'
```

2. Train the model:
```bash
./trainer.sh
```


> **Note**: If you get `ModuleNotFoundError: No module named 'models'`, run
>
> ```shell
> export PYTHONPATH=$(pwd)
> ```
>

### Testing

1. Download pre-trained weights:
- [Google Drive Link](https://drive.google.com/drive/folders/150wd1GsVxnIXq3btG0EEhhXS9gBYnJ2f?usp=sharing)
- Save extractor weights to `models/extractor/checkpoints`
- Save transformer weights to `models/transformer/checkpoints`

2. Run test script:
```bash
python3 test.py
```

### Using Gradio Interface
```bash
python3 ui.py
```