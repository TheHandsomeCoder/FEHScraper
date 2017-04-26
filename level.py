from PIL import Image, ImageEnhance, ImageFilter, ImageChops
import pytesseract
import numpy as np
import json
from datetime import datetime

image1 = Image.open("./images/8-0.png")
image1.crop((120, 780, 150, 810)).save('./assets/1star.png')



# print ImageChops.difference(image1, image2).getbbox() is None