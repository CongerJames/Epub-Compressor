import os
import glob
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def compresser(source,compression_level = 30):
    image_dir = source + '/**/OEBPS/Images/*.jpg'
    compression_level = 30

    image_files = glob.glob(image_dir)

    for file in image_files:
        if 'Cover.jpg' not in file:
            image = Image.open(file)
            image.save(file, quality=compression_level)
