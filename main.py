from converter import ImageConverter

imagePath = input("Ingrese la ruta de la imagen: ")
image = ImageConverter(imagePath)
image.writeTextImage()