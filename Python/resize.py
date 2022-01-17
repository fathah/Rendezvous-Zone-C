from PIL import Image
import os, sys
import shutil


path = "C:/Users/User/Desktop/garden/rendezvous/2021/Chest/out/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((187,246), Image.ANTIALIAS)
            imResize.save(f + ' resized.png', quality=90)

def move():
    for item in dirs:
        name = os.path.splitext(path+item)
        if('resized' in name):
            print(name)



move()