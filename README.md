# MLSLT: Towards Multilingual Sign Language Translation

This repository contains the SP-10 dataset described in "MLSLT: Towards Multilingual Sign Language Translation".
The copyright of the data is owned by the non-profit association European Sign Language Centre, please ensure you have obtained permission before making any academic or commercial use.

## Download videos

1. Download repo.
```
git clone https://github.com/MLSLT/SP-10

```
2. Install dependencies

If you use conda you can create a virtual environment with the following command,
```
conda env create -f env.yaml
conda activate sp-10
```
or you can use pip to install the corresponding packages.
```
pip install -r requirements.txt
```
3. Install [ffmpeg](https://ffmpeg.org/) to process videos, if you use Ubuntu system you can use the following command to install.
```
sudo apt update
sudo apt install ffmpeg
```

4. Download videos.
```
python video_downloader.py [--save_path ${SAVE_PATH}]
```
The dataset is saved in the path ./videos by default, and you can also use --save_path to customize the save path.

4. Convert videos.
If you customize the save path, please make sure that the save_path of this step is the same as the previous step.
```
python video_converter.py [--save_path ${SAVE_PATH}]
```
## Folder structure
The storage structure of video data in folders is shown below.
```
.
├── dev
│   └── 635
│       ├── bg.mp4
│       ├── de.mp4
│       ├── en.mp4
│       ...
├── test
│   └── 1296
│       ├── bg.mp4
│       ├── de.mp4
│       ├── en.mp4
│       ...
└── train
    ├── 410
    │   ├── bg.mp4
    │   ├── de.mp4
    │   ├── en.mp4
        ...

```