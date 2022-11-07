from PIL import Image, ImageFilter

img = Image.open('./211 astro.jpg')
img.thumbnail((400,400))
img.save('./new/thumnai.jpeg')

