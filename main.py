from converter import TextConverter

imagePath = input("Enter the image path: ")
image = TextConverter(imagePath)
image.writeTextImage()