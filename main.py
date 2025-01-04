from image_to_ascii import ASCIIGenerator
import os

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

image_path = input("Enter the image path: ")
ascii_result = ASCIIGenerator(image_path).draw_ascii("grayscale", "circle")

with open(f"{desktop_path}/bynaryImage.txt", "w", encoding = "utf-16") as file:
            for row in ascii_result:
                for pixel in row:
                    file.write(pixel)