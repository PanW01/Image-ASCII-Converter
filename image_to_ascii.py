from PIL import Image # type: ignore
from typing import Optional
import shapes
import math

class ASCIIGenerator:

    def __init__(self, imagePath):
        self.image = Image.open(imagePath)

    def draw_ascii(self, draw_type: str, shape: Optional[str] = None):
        image = self.image
        image = self.resize_with_aspect_ratio(image, 128)
        image = self.normalize_image(image)
        image = self.include_shape(image, shape)

        drawing_method = self.select_drawing_type(draw_type)
        picture = drawing_method.convert_to_ascii(image)
        return picture

    def resize_with_aspect_ratio(self, image, height):
        size = (math.trunc(image.width / image.height * height), height)
        image.thumbnail(size)
        return image
    
    def resize_image(self, width, height):
        return self.image.resize((width, height))

    def normalize_image(self, image):
        width, height = image.size
        normalize_width = width * 2

        return image.resize((normalize_width, height))

    def include_shape(self, image, shape):
        shape = shapes.Stair(image)
        star_position = shape.draw_shape()
        pixel_list = list(image.getdata())
        new_image = Image.new("L", image.size, 255)
        
        for y in range(image.height): # It spends a lot of time because is a loop with the original image size
            for x in range(image.width):
                if (x, y) in star_position:
                    index = y * image.width + x
                    pixel_value = pixel_list[index]
                    r, g, b = pixel_value
                    gray_value = int(0.299 * r + 0.587 * g + 0.114 * b)
                    new_image.putpixel((x, y), gray_value)


        return new_image



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
            characters = ["█", "▓", "▒", "░", "   "]
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