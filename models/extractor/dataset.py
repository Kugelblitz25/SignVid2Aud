import logging
from pathlib import Path

import pandas as pd
import torch
from pytorchvideo.data.encoded_video import EncodedVideo
from pytorchvideo.transforms import (
    ApplyTransformToKey,
    ShortSideScale,
    UniformTemporalSubsample,
)
from torch.utils.data import Dataset
from torchvision.transforms import Compose, Lambda
from torchvision.transforms._transforms_video import (
    CenterCropVideo,
)

# Model specific
side_size = 256
crop_size = 256
num_frames = 64
sampling_rate = 8
mean = [0.45, 0.45, 0.45]
std = [0.225, 0.225, 0.225]
frames_per_second = 25

# The duration of the input clip is also specific to the model.
clip_duration = (num_frames * sampling_rate) / frames_per_second

transform = ApplyTransformToKey(
    key="video",
    transform=Compose(
        [
            UniformTemporalSubsample(num_frames),
            Lambda(lambda x: (x / 255.0) * 2 - 1),
            # NormalizeVideo(mean, std),
            ShortSideScale(size=side_size),
            CenterCropVideo(crop_size=(crop_size, crop_size)),
        ]
    ),
)


class WLASLDataset(Dataset):
    def __init__(self, data: pd.DataFrame, video_dir: str) -> None:
        self.data = data
        self.video_dir = Path(video_dir)
        self.transform = transform
        self.classes = sorted(data.Gloss.unique())
        self.class_to_idx = {cls: idx for idx, cls in enumerate(self.classes)}

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, idx: int) -> tuple[torch.tensor, int]:
        item = self.data.loc[idx]
        video_path = self.video_dir / item["Video file"]
        label = self.class_to_idx[item["Gloss"]]
        try:
            video = EncodedVideo.from_path(video_path)
            video_data = video.get_clip(start_sec=0, end_sec=clip_duration)
            video_data = transform(video_data)
            return video_data["video"], label
        except Exception as e:
            logging.warning(f"Failed to load video {video_path}: {str(e)}")
            return torch.zeros((3, 32, 224, 224)), label
