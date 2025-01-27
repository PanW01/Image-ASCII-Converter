from image_to_ascii import *
from PIL import Image
from typing import Optional

class ASCIIVideoGenerator:
    def __init__(self, video):
        self.video = video

    def get_ascii_frames(self, skip_frames: Optional[int] = None):
        ascii_frame_list = []

        for index, frame in enumerate(self.video):
            if skip_frames is not None and index % skip_frames == 0:
                pil_frame = Image.fromarray(frame)
                ascii_image = ASCIIImageGenerator(pil_frame).get_ascii_image("grayscale", True)
                ascii_frame_list.append(ascii_image)

        return ascii_frame_list