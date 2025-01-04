from PIL import Image # type: ignore
import os
import math

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
        equal_dimensions = (self.image.height * 2, self.image.height)
        shape = self.shape.resize(equal_dimensions)
        shape = shape.convert("L")

        pixel_list = list(shape.getdata())
        pixels_position = [shape.width]

        offset_x, offset_y = self.get_center_image(shape, self.image)
        print(offset_x, offset_y)

        for index, value in enumerate(pixel_list):
            if value < 128:

                column_index = index % shape.width
                row_index = index // shape.width

                final_x_position = column_index + offset_x
                final_y_position = row_index + offset_y

                if 0 <= final_x_position < self.image.width and 0 <= final_y_position < self.image.height:
                    pixel_index = final_y_position * self.image.width + final_x_position
                    pixels_position.append(pixel_index)

        return pixels_position
    
    def get_center_image(self, shape, image):
        shape_center_x = shape.width // 2
        shape_center_y = shape.height // 2

        image_center_x = image.width // 2
        image_center_y = image.height // 2

        new_shape_x = image_center_x - shape_center_x
        new_shape_y = image_center_y - shape_center_y

        return new_shape_x, new_shape_y