import logging
import argparse
from pathlib import Path
import os
import cv2
import shutil

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")


def main(args):
    root_path = Path(args.save_path)
    for video_path in root_path.rglob("*.mp4"):
        cap = cv2.VideoCapture(str(video_path))
        frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
        if frame_rate == 25:
            continue
        logging.info(f"Start converting {video_path}, its frame rate is {frame_rate}")
        video_path = video_path.resolve()
        os.system(f"ffmpeg -i '{video_path}' -r 25 /tmp/sign.mp4 -y")
        shutil.move("/tmp/sign.mp4", str(video_path))


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument(
        "--save_path", help="Path to save the video", default="./videos", type=str
    )
    args = parse.parse_args()
    logging.info("Start converting SP-10 dataset")
    main(args)
    logging.info("Converting SP-10 dataset finished")
