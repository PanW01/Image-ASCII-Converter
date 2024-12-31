from PIL import Image # type: ignore
import os

class Shape:
    def __init__(self, shape_name, image):
        shape_path = os.path.join(os.getcwd(), f"default_shapes/{shape_name}.png")
        self.shape = Image.open(shape_path)
        self.image = image
    
    def apply_shape(self):
        image_gray_scale = self.image.convert("L")
        image_pixel_list = list(image_gray_scale.getdata())
        shape_pixel_list = self.get_pixels_list()

        new_image = Image.new("L", self.image.size, 255)

        for pixel_position in shape_pixel_list:
            x = pixel_position % self.image.width
            y = pixel_position // self.image.width

            new_image.putpixel((x, y), image_pixel_list[pixel_position])

        return new_image

    def get_pixels_list(self):
        shape = self.shape.resize((self.image.width, self.image.height))
        shape = shape.convert("L")

        pixel_list = list(shape.getdata())
        pixels_position = [shape.width]

        for index, value in enumerate(pixel_list):
            if value < 128:
                pixels_position.append(index)

        return pixels_position



