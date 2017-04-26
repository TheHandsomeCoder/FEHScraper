from PIL import Image, ImageEnhance, ImageFilter, ImageChops
import pytesseract
import numpy as np
import json
import pprint
from datetime import datetime
import os

RARITY_IMAGES = [
    Image.open("./assets/1star.png"),
    Image.open("./assets/2star.png"),
    Image.open("./assets/3star.png"),
    Image.open("./assets/4star.png"),
    Image.open("./assets/5star.png")
]

def getTextFromImage(image):
    return pytesseract.image_to_string(image, config='-psm 7')

def getHeroRarity(image):
    for i, x in enumerate(RARITY_IMAGES):
        if ImageChops.difference(image, x).getbbox() is None:
            return i+1
    return -1

def getHeroDataFromImage(originalImage, transformedImage):
    hero = {}
    hero['name'] = getTextFromImage(transformedImage.crop((50, 950, 550, 1035)))
    hero['title'] = getTextFromImage(transformedImage.crop((30, 830, 570, 915)))
    hero["hm"] = getTextFromImage(transformedImage.crop((250, 1635, 500, 1710)))
    hero["sp"] = getTextFromImage(transformedImage.crop((250, 1560, 500, 1635)))
    hero["res"] = getTextFromImage(transformedImage.crop((250, 1485, 500, 1560)))
    hero["def"] = getTextFromImage(transformedImage.crop((250, 1410, 500, 1485)))
    hero["spd"] = getTextFromImage(transformedImage.crop((250, 1335, 500, 1410)))
    hero["atk"] = getTextFromImage(transformedImage.crop((250, 1260, 500, 1335)))
    hero["hp"] = getTextFromImage(transformedImage.crop((250, 1185, 500, 1260)))
    hero["lv"] = getTextFromImage(transformedImage.crop((230, 1100, 350, 1175)))
    hero["exp"] = getTextFromImage(transformedImage.crop((610, 1110, 900, 1165)))
    hero["weapon"] = getTextFromImage(transformedImage.crop((620, 1195, 1075, 1270)))
    hero["support"] = getTextFromImage(transformedImage.crop((620, 1270, 1075, 1345)))
    hero["special"] = getTextFromImage(transformedImage.crop((620, 1345, 1075, 1420)))
    hero["aSlot"] = getTextFromImage(transformedImage.crop((620, 1420, 1075, 1495)))
    hero["bSlot"] = getTextFromImage(transformedImage.crop((620, 1495, 1075, 1570)))
    hero["cSlot"] = getTextFromImage(transformedImage.crop((620, 1570, 1075, 1640)))
    hero["sSlot"] = getTextFromImage(transformedImage.crop((620, 1645, 970, 1715)))
    hero["rarity"] = getHeroRarity(originalImage.crop((120, 780, 150, 810)))
    return hero

def prepImageForTesseract(image):
    gray = image.convert('L')
    # Let numpy do the heavy lifting for converting pixels to pure black or white
    threasholdImage = np.asarray(gray).copy()
    # Pixel range is 0...255, 256/2 = 128
    threasholdImage[threasholdImage < 200] = 0    # Black
    threasholdImage[threasholdImage >= 200] = 255 # White

    # Now we put it back in Pillow/PIL land
    img = Image.fromarray(threasholdImage)
    img = ImageChops.invert(img)
    img = ImageEnhance.Sharpness(img).enhance(2)
    return img

def heroImageToKeyValuePairs(imagePath):
    originalImage = Image.open(imagePath)
    transformedImage = prepImageForTesseract(originalImage)
    hero = getHeroDataFromImage(originalImage, transformedImage)
    return hero;

if __name__ == '__main__':
    startTime = datetime.now()

    heroesList = []
    for file in os.listdir("./images"):
        if file.endswith(".png"):
            heroesList.append(heroImageToKeyValuePairs('./images/' + file))

    with open('herodata.json', 'w') as outfile:
        json.dump(heroesList, outfile)

    print('Script Complete: ' + str(datetime.now() - startTime))