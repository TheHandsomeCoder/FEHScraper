from PIL import Image, ImageEnhance, ImageFilter, ImageChops
import pytesseract

#Print the file

image = Image.open('3.png')
image = ImageEnhance.Color(image).enhance(0.0)
image = ImageChops.invert(image)
image = ImageEnhance.Contrast(image).enhance(1000).show()


# contrast = ImageEnhance.Contrast(image).enhance(2)
# # image.save('blackandwhite.png')
# print pytesseract.image_to_string(image)
print('done')