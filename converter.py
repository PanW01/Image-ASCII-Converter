from PIL import Image  # type: ignore
import os

class TextConverter():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    def __init__(self, imagePath):
        self.imagePath =  imagePath

    def writeTextImage(self):
        text = self.convertToText("GrayScale")
        with open(f"{self.desktop_path}/bynaryImage.txt", "w", encoding = "utf-16") as file:
            for line in text:
                for pixel in line:
                    file.write(pixel)

    def convertToText(self, scale = "BinaryColor"):
        image = Image.open(self.imagePath)
        binaryImage = self.changeToBinaryColor(image)
        binaryImage = self.resizeImage(binaryImage)
        pixelList = list(binaryImage.getdata())

        textImage = []
        for i in range(0, len(pixelList), binaryImage.width):
            line = "".join([" ■" if pixel == 0 else " □" for pixel in pixelList[i: i + binaryImage.width]])
            textImage.append(line + '\n')
        
        binaryImage.save(f"{self.desktop_path}/binaryImage.png") # Save the binary image to test the conversion
        return textImage
    
    def convertToText(self, scale = "GrayScale"):
        image = Image.open(self.imagePath)
        grayScaleImage = self.changeToGrayScale(image)
        grayScaleImage = self.resizeImage(grayScaleImage)
        pixelList = list(grayScaleImage.getdata())

        textImage = []
        characters = ["█", "▓", "▒", "░"]
        for i in range(0, len(pixelList), grayScaleImage.width):
            line = "".join(
                characters[0] if pixel <= 64 else
                characters[1] if pixel <= 128 else
                characters[2] if pixel <= 192 else
                characters[3]
                for pixel in pixelList[i: i + grayScaleImage.width]
            )
            textImage.append(line + '\n')
        
        grayScaleImage.save(f"{self.desktop_path}/grayScaleImage.png") # Save the binary image to test the conversion
        return textImage

    def changeToBinaryColor(self, image):
        binaryImage = image.convert("L").point(lambda x: 255 if x >= 128 else 0)
        return binaryImage
    
    def changeToGrayScale(self, image):
        colors = [64, 128, 192, 255]
        binaryImage = image.convert("L").point(lambda x: next(colors[i] for i in range(4) if x <= colors[i] * (i)))
        return binaryImage
    
    def resizeImage(self, image):
        resizeImage = image.resize((32, 32))
        return resizeImage