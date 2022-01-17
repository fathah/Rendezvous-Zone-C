import PIL
import os
import os.path
from PIL import Image

f = r'C:/Users/User/Desktop/garden/rendezvous/2021/Chest/out'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((1949,2569))
    img.save(f+"/cmp/"+file, optimize=True, quality=50)