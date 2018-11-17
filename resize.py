import glob
import os
from PIL import Image

filepath = "/Users/garrettdimick/tempfiles/downloads/clipart_octopus/*"

def resize_files(filepath):
    f = glob.glob(filepath)
    for file in f:
        im = Image.open(file)
        width = 108
        height = 108
        image = im.resize((width, height))
        image.save(file)

resize_files(filepath)
