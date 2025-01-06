from image_to_ascii import ASCIIGenerator
from PIL import Image # type: ignore
import os

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

image_path = input("Enter the image path: ")
shape = Image.open("C:\\Users\\USUARIO\\Desktop\\imagen.jpg")
ascii_result = ASCIIGenerator(image_path).draw_ascii("grayscale", shape)

with open(f"{desktop_path}/bynaryImage.txt", "w", encoding = "utf-16") as file:
            for row in ascii_result:
                for pixel in row:
                    file.write(pixel)