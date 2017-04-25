from PIL import Image, ImageEnhance, ImageFilter, ImageChops
import pytesseract
import numpy as np
import json
from datetime import datetime

def getTextFromImage(image):
    return pytesseract.image_to_string(image, config='-psm 7')

col = Image.open("./images/6-1.png")
gray = col.convert('L')

# Let numpy do the heavy lifting for converting pixels to pure black or white
bw = np.asarray(gray).copy()

# Pixel range is 0...255, 256/2 = 128
bw[bw < 200] = 0    # Black
bw[bw >= 200] = 255 # White

# Now we put it back in Pillow/PIL land
imfile = Image.fromarray(bw)
imfile = ImageChops.invert(imfile)
imfile = ImageEnhance.Sharpness(imfile).enhance(2)
startTime = datetime.now()
hero = {}

hero['name'] = getTextFromImage(imfile.crop((50, 950, 550, 1025)))
hero['title'] = getTextFromImage(imfile.crop((30, 830, 570, 915)))
hero["hm"] = getTextFromImage(imfile.crop((250, 1635, 500, 1710)))
hero["sp"] = getTextFromImage(imfile.crop((250, 1560, 500, 1635)))
hero["res"] = getTextFromImage(imfile.crop((250, 1485, 500, 1560)))
hero["def"] = getTextFromImage(imfile.crop((250, 1410, 500, 1485)))
hero["spd"] = getTextFromImage(imfile.crop((250, 1335, 500, 1410)))
hero["atk"] = getTextFromImage(imfile.crop((250, 1260, 500, 1335)))
hero["hp"] = getTextFromImage(imfile.crop((250, 1185, 500, 1260)))
hero["lv"] = getTextFromImage(imfile.crop((230, 1100, 350, 1175)))
hero["exp"] = getTextFromImage(imfile.crop((610, 1110, 900, 1165)))
hero["weapon"] = getTextFromImage(imfile.crop((620, 1195, 1075, 1270)))
hero["support"] = getTextFromImage(imfile.crop((620, 1270, 1075, 1345)))
hero["special"] = getTextFromImage(imfile.crop((620, 1345, 1075, 1420)))
hero["aSlot"] = getTextFromImage(imfile.crop((620, 1420, 1075, 1495)))
hero["bSlot"] = getTextFromImage(imfile.crop((620, 1495, 1075, 1570)))
hero["cSlot"] = getTextFromImage(imfile.crop((620, 1570, 1075, 1640)))
hero["sSlot"] = getTextFromImage(imfile.crop((620, 1645, 970, 1715)))
print str(hero)
print('Script Complete: ' + str(datetime.now() - startTime))