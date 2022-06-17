from PIL import Image
import os, sys
import glob

path = "E:\For Project\Segmentation\Training Data\maska"

for filename in glob.iglob(path + '*/.png', recursive=True):
    print(filename)
    im = Image.open(filename)
    imResize = im.resize((128,128), Image.ANTIALIAS)
    imResize.save(filename , 'PNG', quality=90)
