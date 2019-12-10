import pyimgur
import PIL
from PIL import Image,ImageDraw,ImageFont
import textwrap

def upload_graph(PATH):
    CLIENT_ID = '6b797f46b283856'
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
    return uploaded_image.link

#draw meme1
def draw_graph1_and_upload(str,str2):
    #123
    image = Image.open('./img/meme1.png')
    imgwidth, imgheight = image.size
    draw = ImageDraw.Draw(image) 
    size1 = 40
    size2 = 40
    font1 = ImageFont.truetype("./font/MSJHBD.TTC",size1, encoding="utf-8")
    font2 = ImageFont.truetype("./font/MSJHBD.TTC",size2, encoding="utf-8")
 
    #first line 
    left1, top1, right1, bottom1 = font1.getmask(str).getbbox()
    width = right1-left1
    while width >= imgwidth/2 - 30:
        size1 = size1-1
        font1 = ImageFont.truetype("./font/MSJHBD.TTC",size1, encoding="utf-8")
        left1, top1, right1, bottom1 = font1.getmask(str).getbbox()
        width = right1-left1

    #second line
    left2, top2, right2, bottom2 = font2.getmask(str2).getbbox()
    width = right2-left2
    while width >= imgwidth/2 - 30:
        size2 = size2-1
        font2 = ImageFont.truetype("./font/MSJHBD.TTC",size2, encoding="utf-8")
        left2, top2, right2, bottom2 = font2.getmask(str2).getbbox()
        width = right2-left2

    left1, top1, right1, bottom1 = font1.getmask(str).getbbox()
    left2, top2, right2, bottom2 = font2.getmask(str2).getbbox()
    draw.text(((imgwidth/4-(right1-left1)/2),(120-(bottom1-top1))/2),str,'#000000',font1)
    draw.text(((imgwidth/4-(right2-left2)/2) + imgwidth/2,(120-(bottom2-top2))/2),str2,'#000000',font2)
    """
    draw.text((40,30),str,'#000000',font1)
    draw.text((imgwidth/2+40,30),str2,'#000000',font2)
    """  
    PATH = './img/meme1_custom.png'
    image.save(PATH,'png',quality=95)
    return upload_graph(PATH)


#draw meme2
def draw_graph2_and_upload(str,str2):
    image = Image.open('./img/meme2.png')
    imgwidth, imgheight = image.size
    draw = ImageDraw.Draw(image) 
    size1 = 50
    size2 = 50
    font1 = ImageFont.truetype("./font/MSJHBD.TTC",size1, encoding="utf-8")
    font2 = ImageFont.truetype("./font/MSJHBD.TTC",size2, encoding="utf-8")
    
    #first line
    arrays = str.splitlines()
    current=0
    i=0
    
    width, height = font1.getsize(arrays[0])
    print(width)
    for array in arrays:
        print(font1.getsize(array))
        if width < font1.getsize(array)[0]:
            width = font1.getsize(array)[0]
            current = i
        i=i+1
    
    while width >= 285:
        size1 = size1-1
        font1 = ImageFont.truetype("./font/MSJHBD.TTC",size1, encoding="utf-8")
        left1, top1, right1, bottom1 = font1.getmask(arrays[current]).getbbox()
        width = right1-left1
    
    #second line
    arrays = str2.splitlines()
    current=0
    i=0
    
    width, height = font2.getsize(arrays[0])
    for array in arrays:
        print(font1.getsize(array))
        if width < font2.getsize(array)[0]:
            width = font2.getsize(array)[0]
            current = i
        i=i+1
    
    while width >= 285:
        size2 = size2-1
        font2 = ImageFont.truetype("./font/MSJHBD.TTC",size2, encoding="utf-8")
        left2, top2, right2, bottom2 = font2.getmask(arrays[current]).getbbox()
        width = right2-left2

    draw.text((40,130),str,'#000000',font1)
    draw.text((35,imgheight/2+200),str2,'#000000',font2)
    PATH = './img/meme2_custom.png'
    image.save(PATH,'png',quality=95)
    return upload_graph(PATH)

def draw_graph3_and_upload(str,str2):
    #123
    image = Image.open('./img/meme3.png')
    imgwidth, imgheight = image.size
    draw = ImageDraw.Draw(image) 
    font = ImageFont.truetype("./font/MSJHBD.TTC",35, encoding="utf-8")
 
    #first line 
    left1, top1, right1, bottom1 = font.getmask(str).getbbox()
    #second line
    left2, top2, right2, bottom2 = font.getmask(str2).getbbox()
    
    draw.text(((imgwidth/4-(right1-left1)/2),20),str,'#000000',font)
    draw.text(((imgwidth/4-(right2-left2)/2) + imgwidth/2,20),str2,'#000000',font)
    PATH = './img/meme3_custom.png'
    image.save(PATH,'png',quality=95)
    return upload_graph(PATH)

if __name__ == "__main__":
    draw_graph1_and_upload("和同學抱怨pipenv install一直出錯","使用ubuntu的同學")