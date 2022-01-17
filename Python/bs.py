from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
import png 
import pyqrcode 
from pyqrcode import QRCode 

 
ag_file = "C:/Users/User/Desktop/garden/rendezvous/2021/Chest/ag.png"
cc_file = "C:/Users/User/Desktop/garden/rendezvous/2021/Chest/cc.png"
ib_file = "C:/Users/User/Desktop/garden/rendezvous/2021/Chest/ib.png"

out_file = "C:/Users/User/Desktop/garden/rendezvous/2021/Chest/out/" 
qr_file = "C:/Users/User/Desktop/garden/rendezvous/2021/Chest/qr/" 

text = "Fathah"
light_font = "C:/Users/User/Desktop/garden/rendezvous/2021/Chest/fonts/ProductSans-Light.ttf"
bold_font = "C:/Users/User/Desktop/garden/rendezvous/2021/Chest/fonts/ProductSans-Bold.ttf"
reg_font = "C:/Users/User/Desktop/garden/rendezvous/2021/Chest/fonts/ProductSans-Regular.ttf"


users =[
# ["Mishab Musthafa", "401", "cc" ],
# ["Hashim Shafi", "402", "cc" ],
# ["Swabeeh Umar", "403", "cc" ],
# ["Mirsad Yusuf", "404", "cc" ],
# ["Abdul Qadar Alavi", "405", "cc" ],
# ["Badusha Muhammed", "406", "cc" ],
# ["Nazih Muhyiddeen", "407", "cc" ],
# ["Swadiq Moosa", "408", "cc" ],
# ["Anshif Ali", "409", "cc" ],
# ["Sinan Abdulmajeed", "410", "cc" ],
# ["ShibilI Jouhar Muhammed", "411", "cc" ],
# ["Yasir Muhammed Ali", "412", "cc" ],
# ["Shamil Shukoor", "413", "cc" ],
# ["Ameen Shafi", "414", "cc" ],
# ["Falulurahman Abdunnasar", "415", "cc" ],
# ["Sayyid Sahal Shihabuddeen", "416", "cc" ],
# ["Anees Abdul Azeez", "417", "cc" ],
# ["Minhaj Muhammed", "418", "cc" ],
# ["Fasalurahman Abdul Khader", "501", "cc" ],
# ["Shabeeb Ashraf", "502", "cc" ],
# ["Habeeb Moosa", "503", "cc" ],
# ["Abdul Hadi Aboobacker", "504", "cc" ],
# ["Bushair Yaqoob", "505", "cc" ],
# ["Safwan Musthafa", "506", "cc" ],
# ["Sayyid Muammil Bahasan", "507", "cc" ],
# ["Abdul Basith Hamza", "508", "cc" ],
# ["Zain Hassankutti", "509", "cc" ],
# ["Jabir Abdul Jabbar", "510", "cc" ],
# ["Faris Farooq", "511", "cc" ],
# ["Muhammed Ali Habeeb", "512", "cc" ],
# ["Suhail Ashraf", "513", "cc" ],
# ["Mashoor Ashraf", "514", "cc" ],
# ["Rafeeque Mon Rafi", "515", "cc" ],
# ["Sinan Yousuf", "516", "cc" ],
# ["Muaviya Zakariya", "517", "cc" ],
# ["Shahid Abdul Khader", "518", "cc" ],
# ["Umair Hamza", "519", "cc" ],
# ["Naeeb Ali Muhammed", "520", "cc" ],
# ["Mubashir Abdullah", "521", "cc" ],
# ["Muhammed Ali Moosa", "522", "cc" ],
# ["Rishad Razak", "523", "cc" ],
# ["Ibrahim Hamza", "524", "cc" ],
# ["Mubashir Jabbar", "525", "cc" ],
# ["Rashid Usman", "526", "cc" ],
# ["Amraz Abdul Sathar", "527", "cc" ],
# ["Junaid Aboobacker", "528", "cc" ],
# ["Ishaq Ibrahim", "529", "cc" ],
# ["Ramees Ameerali", "530", "cc" ],
# ["Majid Abdussamad", "531", "cc" ],
# ["Munavvir Abdurahman", "532", "cc" ],
# ["Rashid Abdurahman", "533", "cc" ],
# ["Falulurahman Muhammed", "534", "cc" ],
# ["Bujair Shafi", "419", "ag" ],
# ["Umarul Farooq Hassainar", "420", "ag" ],
# ["Irfan Ansari", "421", "ag" ],
# ["Miqdad Abdul Salam", "422", "ag" ],
# ["Naeem Ashraf", "423", "ag" ],
# ["Sabith Sulaiman", "424", "ag" ],
# ["Mubassir Ibrahim", "425", "ag" ],
# ["Jazeel Abdul Azeez", "426", "ag" ],
# ["Ameen Ashraf", "427", "ag" ],
# ["Vasil Mujeeb", "428", "ag" ],
# ["Usman Mohammed Ali", "429", "ag" ],
# ["Muhammed Abdul Hakeem", "430", "ag" ],
# ["Mubashir Abdussaleem", "431", "ag" ],
# ["Rafi Ahmad", "432", "ag" ],
# ["Thwahir Siddique", "433", "ag" ],
# ["Salim Yusuf", "434", "ag" ],
# ["Minhaj Muhammed A.M", "435", "ag" ],
# ["Sayyid Thahseen Hussain", "436", "ag" ],
# ["Iyas Sulaiman", "437", "ag" ],
# ["Muhammed Ali", "535", "ag" ],
# ["Fathah Abdussalam", "536", "ag" ],
# ["Khaja Mueenudheen Ismail", "537", "ag" ],
# ["Rameez Rafeek", "538", "ag" ],
# ["Midlaj Muhyuddin", "539", "ag" ],
# ["Mishab Abdulrahman", "540", "ag" ],
# ["Javead Abdulla", "541", "ag" ],
# ["Rishad Iqbal", "542", "ag" ],
# ["Saneer Muhammed", "543", "ag" ],
# ["Yaseen Sharafuddeen", "544", "ag" ],
# ["Alyasah Yousuf", "545", "ag" ],
# ["Aswif Abdulla", "546", "ag" ],
# ["Sardar Alavi", "547", "ag" ],
# ["Sabith Isamail", "548", "ag" ],
# ["Basith Abdurahman", "549", "ag" ],
# ["Arshad Muneer", "550", "ag" ],
# ["Favas Sulaiman", "551", "ag" ],
# ["Majid Musthafa", "552", "ag" ],
# ["Midlaj Abdulla", "553", "ag" ],
# ["Saad Yusuf", "554", "ag" ],
# ["Rashid Abdul Azeez", "555", "ag" ],
# ["Falil Abdul Azeez", "556", "ag" ],
# ["Mushtaq Abdul Rahman", "557", "ag" ],
# ["Mubaris Ali", "558", "ag" ],
# ["Suhail Abdulla", "559", "ag" ],
# ["Basith Sheikh", "560", "ag" ],
# ["Amjad Abdul Azeez", "561", "ag" ],
# ["Vajid Samad", "562", "ag" ],
# ["Muhammed Ali Yahya Khan", "563", "ag" ],
# ["Arshad Muhammed", "564", "ag" ],
# ["Shuhaib Muhammed", "565", "ag" ],
# ["Rauoof Rasheed", "566", "ag" ],
# ["Mubeen Rafeeq", "567", "ag" ],
# ["Jeelani Sulaiman", "568", "ag" ],
# ["Abdul Hafeez Muhyiddeen", "438", "ib" ],
# ["Hashir Anas Muhammed", "439", "ib" ],
# ["Suhail Sulaiman", "440", "ib" ],
# ["Shafeeq Abdul Hakeem", "441", "ib" ],
# ["Uvais Suhail", "442", "ib" ],
# ["Salim Moosa", "443", "ib" ],
# ["Shamil Minhaj Abdul Rasheed", "444", "ib" ],
["Sayyid Jasar Bafaqeeh", "445", "ib" ],
# ["Muhammed Swabeeh", "446", "ib" ],
# ["Haseeb Hamza", "447", "ib" ],
# ["Bishr Basheer", "448", "ib" ],
# ["Rishaq Rashid", "449", "ib" ],
# ["Sinan Yahya", "450", "ib" ],
# ["Sinan Abdurahman", "451", "ib" ],
# ["Jamaluddeen Ibrahim", "452", "ib" ],
# ["Jafar Ali", "453", "ib" ],
# ["Mukhthar Musthafa", "454", "ib" ],
# ["Mueen Hussain TP", "455", "ib" ],
# ["Ameen Basheer", "569", "ib" ],
# ["Sameer Abdul Azeez", "570", "ib" ],
# ["Fabiyas Saidalavi", "571", "ib" ],
# ["Iyas Ali", "572", "ib" ],
# ["Raheem Basheer", "573", "ib" ],
# ["Ashir Beeran", "574", "ib" ],
# ["Thasleem Abduraheem", "575", "ib" ],
# ["Saleem Saidalavi", "576", "ib" ],
# ["Ajmal Majeed", "577", "ib" ],
# ["Juraij Kareem", "578", "ib" ],
# ["Ihsan Ibrahim", "579", "ib" ],
# ["Miqdad Abdullah", "580", "ib" ],
# ["Shuhaib Aboobacker", "581", "ib" ],
# ["Unais Abdul Rahman", "582", "ib" ],
# ["Basith Haneefa", "583", "ib" ],
# ["Shafi Ashraf", "584", "ib" ],
# ["Ameen Muhammed C. K", "585", "ib" ],
# ["Muhammed Siraj Rahman", "586", "ib" ],
# ["Sayyid Fazal Zain", "587", "ib" ],
# ["Husain Abdul Kadar", "588", "ib" ],
# ["Savad Ashraf", "589", "ib" ],
# ["Hafiz Abdul Hakeem", "590", "ib" ],
# ["Mubashir Ibrahim", "591", "ib" ],
# ["Mubarak Abdullah", "592", "ib" ],
# ["Nusaif Yusaf", "593", "ib" ],
# ["Ajmal Aboobacker", "594", "ib" ],
# ["Shanavas Saleem", "595", "ib" ],
# ["Basheer Ismail", "596", "ib" ],
# ["Abdul Fathah Abdurahman", "597", "ib" ],
# ["Jabir Uhaimid", "598", "ib" ],
# ["Sahad Abdul Salam", "599", "ib" ],
# ["Ashiq Abdullah", "600", "ib" ],
# ["Raziq Muhammed", "601", "ib" ],
# ["Yaseer Abdul Razak", "602", "ib" ],
# ["Shammas Abdul Gafoo", "603", "ib"]

]

# for i in users:
#     s= f"Rendezvous/{i[1]}"
#     url = pyqrcode.create(s) 
#     url.png(f'qr/{i[1]}.png', scale = 50)

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



    