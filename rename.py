import glob
import os

prefix = "cats"
filepath = "/Users/garrettdimick/tempfiles/downloads/clipart_cat/*"

def rename_files(filepath):
    f = glob.glob(filepath)
    # print(f)
    for i, file in enumerate(f):
        newname = filepath[:-1] + prefix + str(i) + '.jpg'
        try:
            newfile = open(file, "r+")
            os.rename(file, newname)
        except IOError:
            os.remove(file)

rename_files(filepath)
