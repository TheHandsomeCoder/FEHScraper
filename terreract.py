from PIL import Image, ImageEnhance, ImageFilter, ImageChops
import pytesseract
import numpy as np

#Print the file

# image = Image.open('3.png')
# image = ImageEnhance.Color(image).enhance(0.0)
# image = ImageChops.invert(image)
# image = ImageEnhance.Contrast(image).enhance(1000).show()


col = Image.open("3.png")
gray = col.convert('L')

# Let numpy do the heavy lifting for converting pixels to pure black or white
bw = np.asarray(gray).copy()

# Pixel range is 0...255, 256/2 = 128
bw[bw < 200] = 0    # Black
bw[bw >= 200] = 255 # White

# Now we put it back in Pillow/PIL land
imfile = Image.fromarray(bw)
imfile = ImageChops.invert(imfile)

# imfile.crop((left, top, right, bottom))
# contrast = ImageEnhance.Contrast(image).enhance(2)
# # image.save('blackandwhite.png')
print pytesseract.image_to_string(imfile)
print('done')