from PIL import Image  # type: ignore

class ImageConverter():
    def __init__(self, imagePath):
        self.imagePath = imagePath

    def writeTextImage(self):
        text = self.convertToText()
        with open('C:/Users/USUARIO/Desktop/bynaryImage.txt', 'w', encoding = 'utf-16') as file:
            for line in text:
                for pixel in line:
                    file.write(pixel)

    def convertToText(self):
        image = Image.open(self.imagePath)
        binaryImage = self.changeToBinaryColor(image)
        binaryImage = self.resizeImage(binaryImage)
        pixelList = list(binaryImage.getdata())

        textImage = list()
        for i in range(0, len(pixelList), binaryImage.width):
            line = ''.join(["■" if pixel == 0 else "□" for pixel in pixelList[i:i+binaryImage.width]])
            textImage.append(line + '\n')

        binaryImage.save(r"C:/Users/USUARIO/Desktop/binaryImage.png")
        return textImage

    def changeToBinaryColor(self, image):
        binaryImage = image.convert('L').point(lambda x: 255 if x > 128 else 0)
        return binaryImage
    
    def resizeImage(self, image):
        resizeImage = image.resize((128, 128))
        return resizeImage