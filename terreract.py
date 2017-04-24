from PIL import Image, ImageEnhance, ImageFilter, ImageChops
import pytesseract
import numpy as np

#Print the file

# image = Image.open('3.png')
# image = ImageEnhance.Color(image).enhance(0.0)
# image = ImageChops.invert(image)
# image = ImageEnhance.Contrast(image).enhance(1000).show()


col = Image.open("2.png")
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



# imfile = imfile.crop((250, 1635, 500, 1710)) #HM
# imfile = imfile.crop((250, 1560, 500, 1635)) #SP
# imfile = imfile.crop((250, 1485, 500, 1560)) #Res
# imfile = imfile.crop((250, 1410, 500, 1485)) #Def
# imfile = imfile.crop((250, 1335, 500, 1410)) #Spd
# imfile = imfile.crop((250, 1260, 500, 1335)) #Atk
# imfile = imfile.crop((250, 1185, 500, 1260)) #HP
# imfile = imfile.crop((230, 1100, 350, 1175)) #LV.
# imfile = imfile.crop((50, 950, 550, 1025)) #Name.
# imfile = imfile.crop((30, 830, 600, 915)) #Title.
# imfile = imfile.crop((610, 1110, 900, 1165)) #Exp.
# imfile = imfile.crop((620, 1195, 1075, 1270)) #Wpn.
# imfile = imfile.crop((620, 1270, 1075, 1345)) #Spt.
# imfile = imfile.crop((620, 1345, 1075, 1420)) #Spl.
# imfile = imfile.crop((620, 1420, 1075, 1495)) #A.
# imfile = imfile.crop((620, 1495, 1075, 1570)) #B.
# imfile = imfile.crop((620, 1570, 1075, 1640)) #C.
# imfile = imfile.crop((620, 1645, 970, 1715)) #S.

print pytesseract.image_to_string(imfile, config='-psm 7')
print('done')