import sys
import os
from PIL import Image

image_folder = sys.argv[1]

output_folder = sys.argv[2]
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for imgName in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{imgName}')
    clean_name = os.path.splitext(imgName)[0]
    img.save(f'{output_folder}{clean_name}.png','png')
    