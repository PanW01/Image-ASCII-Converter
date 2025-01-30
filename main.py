import clr
import os
clr.AddReference(os.getcwd() + r"\ConsoleRenderer\bin\Debug\net7.0\ConsoleRenderer.dll")
import ConsoleRendererLib

from image_to_ascii import *
from video_to_ascii import *

from PIL import Image # type: ignore
import imageio
import System

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

video = imageio.get_reader(input("Enter the video path: "))
ascii_video_result = ASCIIVideoGenerator(video).get_ascii_frames(1)

ascii_video_result_csharp = System.Collections.Generic.List[str]()
for ascii_frame in ascii_video_result:
    ascii_video_result_csharp.Add("\n".join(ascii_frame))

renderer = ConsoleRendererLib.ConsoleRenderer()
renderer.DrawFrames(ascii_video_result_csharp, 55)

image_path = input("Enter the image path: ")
shape = Image.open("C:\\Users\\USUARIO\\Desktop\\figure-octagon-red-information-icon-260nw-2078450488.webp")
image = Image.open(image_path)
ascii_result = ASCIIImageGenerator(image).draw_ascii("grayscale", True)

with open(f"{desktop_path}/bynaryImage.txt", "w", encoding = "utf-16") as file:
            for row in ascii_result:
                for pixel in row:
                    file.write(pixel)