from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
import png 
import pyqrcode 
from pyqrcode import QRCode 

 
id_card = "C:/Users/User/Desktop/garden/rendezvous/2021/Chest/ag.png"


out_file = "C:/Users/User/Desktop/garden/rendezvous/2021/Chest/out/" 
qr_file = "C:/Users/User/Desktop/garden/rendezvous/2021/Chest/qr/" 

text = "Fathah"
C:\Users\Fathah\Desktop\garden\rendezvous\2021\Chest\fonts

raleway = "C:/Users/Fathah/Desktop/garden/rendezvous/2021/Chest/fonts/Raleway.ttf"
gotham_book = "C:/Users/Fathah/Desktop/garden/rendezvous/2021/Chest/fonts/GothamBook.ttf"
gotham_bold = "C:/Users/Fathah/Desktop/garden/rendezvous/2021/Chest/fonts/GothamBold.ttf"


users =[

# ["Abdul Fathah Abdurahman", "597", "ib" ],
# ["Jabir Uhaimid", "598", "ib" ],
# ["Sahad Abdul Salam", "599", "ib" ],
# ["Ashiq Abdullah", "600", "ib" ],
# ["Raziq Muhammed", "601", "ib" ],
# ["Yaseer Abdul Razak", "602", "ib" ],
# ["Shammas Abdul Gafoo", "603", "ib"]

]

def generate_qr():
    for i in users:
        s= f"Rendezvous/{i[1]}"
        url = pyqrcode.create(s) 
        url.png(f'qr/{i[1]}.png', scale = 50)

for i in users:
    img = ""
    if(i[2]=="cc"):
        img = Image.open(cc_file)
    elif(i[2]=="ib"):
        img = Image.open(ib_file)
    else:
        img = Image.open(ag_file)

    bg_w, bg_h = img.size

    qrImg = Image.open(qr_file+f"/{i[1]}.png", 'r')
    qrimg_w, qrimg_h = qrImg.size
    draw = ImageDraw.Draw(img)
    namefont = ImageFont.truetype(reg_font, 400)
    chestfont = ImageFont.truetype(bold_font, 500)
    idfont = ImageFont.truetype(light_font, 300)

    #Print Text
    draw.text((650, 3050),"Rendezvous ID:", (255, 255, 255), font=idfont)
    draw.text((650, 3400), i[1], (255, 255, 255), font=chestfont)
    draw.text((650, 4750), i[0].upper(), (255, 255, 255), font=namefont)
    img.paste(qrImg, (5700, 7950))
    img.resize((3898,5138), Image.ANTIALIAS )
    img.save(out_file+i[1].upper()+".png", optimize=True,quality=50)



    