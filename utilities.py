import glob
import os
from PIL import Image

prefix = "catsss"
filepath = "/Users/garrettdimick/Downloads/dcgan/data/clipart_cat/*"

def rename_files(filepath):
    f = glob.glob(filepath)
    # print(f)
    for i, file in enumerate(f):
        newname = filepath[:-1] + prefix + str(i) + '.png'
        try:
            newfile = open(file, "r+")
            os.rename(file, newname)
        except IOError:
            os.remove(file)

def resize_files(filepath):
    f = glob.glob(filepath)
    for file in f:
        im = Image.open(file)
        width = 108
        height = 108
        image = im.resize((width, height))
        image.save(file)

# rename_files(filepath)
# resize_files(filepath)
