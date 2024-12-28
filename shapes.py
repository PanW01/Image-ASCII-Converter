from PIL import Image # type: ignore
import os

class Stair:
    def __init__(self, image):
        star_path = os.path.join(os.getcwd(), "default_shapes/star.png")
        self.star = Image.open(star_path)
        self.size = (image.width, image.height)

    def draw_shape(self):
        shape = self.star.resize(self.size)
        shape = shape.convert("L")
        pixel_list = list(shape.getdata())

        pixels_position = []
        actual_pixel = 0

        for y in range(shape.height):
            for x in range(shape.width):
                if pixel_list[y * shape.width + x] < 10:
                    pixels_position.append((x, y))
                actual_pixel += 1

        return pixels_position
