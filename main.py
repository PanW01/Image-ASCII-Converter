import clr
import os
clr.AddReference(os.getcwd() + r"\ConsoleRenderer\bin\Debug\net7.0\ConsoleRenderer.dll")
import ConsoleRendererLib
import System

from image_to_ascii import *
from video_to_ascii import *

from PIL import Image # type: ignore
import imageio
import video_options

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

video_path = input("Enter the video path: ")
video = imageio.get_reader(video_path)

init()
print("\nThe video is being processed...")

fps = video.get_meta_data()['fps'] * 1.9
ascii_video_result = ASCIIVideoGenerator(video).get_ascii_frames(1)

video_options.start("space")

ascii_video_result_csharp = System.Collections.Generic.List[str]()
for ascii_frame in ascii_video_result:
    ascii_video_result_csharp.Add("\n".join(ascii_frame))

video_options.change_video_color("Green")

renderer = ConsoleRendererLib.ConsoleRenderer()
renderer.DrawFrames(ascii_video_result_csharp, System.Int32(int(fps)))

image_path = input("Enter the image path: ")
image = Image.open(image_path)
ascii_result = ASCIIImageGenerator(image).get_ascii_image("grayscale")