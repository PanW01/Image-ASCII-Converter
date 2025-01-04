from PIL import Image # type: ignore
from typing import Optional
import image_shape
import math

class ASCIIGenerator:

    def __init__(self, imagePath):
        self.image = Image.open(imagePath)

    def draw_ascii(self, draw_type: str, shape: Optional[str] = None):
        image = self.image
        image = self.resize_with_aspect_ratio(64)
        image = self.normalize_image(image)

        if shape is not None:
            image = self.include_shape(shape, image)

        drawing_method = self.select_drawing_type(draw_type)
        picture = drawing_method.convert_to_ascii(image)
        return picture

    def resize_with_aspect_ratio(self, height):
        image = self.image
        size = (math.trunc(image.width / image.height * height), height)
        image.thumbnail(size)
        return image
    
    def resize_image(self, width, height):
        return self.image.resize((width, height))

    def normalize_image(self, image):
        width, height = image.size
        normalize_width = width * 2

        return image.resize((normalize_width, height))

    def include_shape(self, shape_name, image):
        shape = image_shape.Shape(shape_name, image)
        image = shape.apply_shape()
        return image

    def select_drawing_type(self, draw_type):
        draw_type = draw_type.lower()
        if draw_type == "binarycolor":
            return self.BinaryDrawing()
        elif draw_type == "grayscale":
            return self.GrayScaleDrawing()
        else:
            raise ValueError("Invalid drawing type")

    class BinaryDrawing:
        def convert_to_ascii(self, image):
            image = image.convert("L")
            characters = ["■", "□"]
            pixelList = list(image.getdata())
            asciiPicture = list()
            for i in range(0, len(pixelList), image.width):
                row = "".join([characters[0] if pixel < 128 else characters[1] for pixel in pixelList[i : i + image.width]])
                asciiPicture.append(row + "\n") 
            
            return asciiPicture

    class GrayScaleDrawing:
        def convert_to_ascii(self, image):
            image = image.convert("L")
            characters = ["█", "▓", "▒", "░"]
            pixelList = list(image.getdata())
            asciiPicture = list()
            for i in range(0, len(pixelList), image.width):
                row = "".join(
                    characters[0] if pixel <= 64 else
                    characters[1] if pixel <= 128 else
                    characters[2] if pixel <= 192 else
                    characters[3]
                    for pixel in pixelList[i : i + image.width]
                )
                asciiPicture.append(row + "\n")
            
            return asciiPicture