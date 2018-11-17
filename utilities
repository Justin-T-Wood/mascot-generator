import glob
import os

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

# rename_files(filepath)
