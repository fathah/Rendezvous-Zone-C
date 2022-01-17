from PIL import Image

imgs = [
    '445',
    '446',
    '447',
    '448',
    '445',
    '446',
    '447',
    '448',
    '445',
    '446',
    '447',
    '448',
]

background = Image.new('RGBA', (3508, 4961), (255, 255, 255, 255))

for i in imgs:
    index = imgs.index(i)
    img = Image.open(f'out/{i}.png', 'r')
    w = 731
    h = 1050

    offH = 10
    img = img.resize((w, h), Image.ANTIALIAS)

    if(index+1==5):
        offH = h+30
    elif(index+1==9):
        offH = offH*2


    if(index == 0):
        offset = (10, 10)
    else:
        offset = (w*index, offH)

    background.paste(img, offset)

background.save('final/out.png')
