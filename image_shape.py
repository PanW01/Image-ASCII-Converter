from PIL import Image # type: ignore
from typing import Optional, Union
import os

class Shape:
    def __init__(self, image, shape: Union[str, Image.Image], inversed_colors: Optional[bool] = False):
        if isinstance(shape, str):
            shape_path = os.path.join(os.getcwd(), f"default_shapes/{shape}.png")
            actual_shape = Image.open(shape_path)
        elif isinstance(shape, Image.Image):
            actual_shape = shape
        else:
            raise TypeError("Shape must be a string or Image")

        self.shape = actual_shape
        self.inversed_colors = inversed_colors
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
        equal_dimensions = (self.image.height * 2, self.image.height)
        shape = self.shape.resize(equal_dimensions)
        shape = shape.convert("L")

        pixel_list = list(shape.getdata())
        pixels_position = [shape.width]

        offset_x, offset_y = self.get_offset(shape, self.image)

        for index, value in enumerate(pixel_list):
            color_threshold = self.shape_colors(value)

            if value < color_threshold:

                column_index = index % shape.width
                row_index = index // shape.width

                final_x_position = column_index + offset_x
                final_y_position = row_index + offset_y

                if 0 <= final_x_position < self.image.width and 0 <= final_y_position < self.image.height:
                    pixel_index = final_y_position * self.image.width + final_x_position
                    pixels_position.append(pixel_index)

        return pixels_position
    
    def get_offset(self, shape, image):
        shape_center_x = shape.width // 2
        shape_center_y = shape.height // 2

        image_center_x = image.width // 2
        image_center_y = image.height // 2

        new_shape_x = image_center_x - shape_center_x
        new_shape_y = image_center_y - shape_center_y

        return new_shape_x, new_shape_y
    
    def shape_colors(self, color_value):
        if self.inversed_colors:
            if color_value > 240:
                return 255
            else:
                return 0
        else:
            if color_value < 240:
                return 255
            else:
                return 0