from image_to_ascii import *
from video_to_ascii import *
from PIL import Image # type: ignore
import os
import time
import pandas
import imageio

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

video = imageio.get_reader("C:/Users/USUARIO/Desktop/【東方】Bad Apple!! ＰＶ【影絵】.mp4")
ascii_video_result = ASCIIVideoGenerator(video).get_ascii_frames(2)

while True:
    os.system("mode con: cols=174 lines=63")
    for frame in ascii_video_result:
        frame_loaded = pandas.DataFrame(frame)
        print(frame_loaded.to_string(index=False, header=False))
        time.sleep(0.015)
        os.system('cls')

image_path = input("Enter the image path: ")
shape = Image.open("C:\\Users\\USUARIO\\Desktop\\figure-octagon-red-information-icon-260nw-2078450488.webp")
image = Image.open(image_path)
ascii_result = ASCIIImageGenerator(image).draw_ascii("grayscale", True)

with open(f"{desktop_path}/bynaryImage.txt", "w", encoding = "utf-16") as file:
            for row in ascii_result:
                for pixel in row:
                    file.write(pixel)