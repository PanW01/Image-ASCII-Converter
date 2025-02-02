from image_to_ascii import *
from PIL import Image
from typing import Optional

import imageio
import imageio_ffmpeg as ffmpeg

from colorama import Fore, init

init()

class ASCIIVideoGenerator:
    def __init__(self, video):
        self.video = video

    def get_ascii_frames(self, skip_frames: Optional[int] = None):
        total_frames = self.video.count_frames()
        ascii_frame_list = []

        for index, frame in enumerate(self.video):
            if skip_frames is not None and index % skip_frames == 0:
                pil_frame = Image.fromarray(frame)
                ascii_image = ASCIIImageGenerator(pil_frame).get_ascii_image("characters", True)
                ascii_frame_list.append(ascii_image)

                progress = index / total_frames * 100
                print(f"Loading frames... {progress:.2f}%", end="\r")

        print(Fore.GREEN + f"\rLoading frames... 100.00%" + Fore.RESET, end="\n")
        return ascii_frame_list