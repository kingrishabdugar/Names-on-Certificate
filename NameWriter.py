#!d:\program_files\python39\

import pandas as pd

from PIL import Image, ImageFont, ImageDraw

FONT_FILE = ImageFont.truetype(r'AnastasiaScript.ttf', 90) 

#up : font name , font size

FONT_COLOR = "#32312f"
WIDTH, HEIGHT = 992, 645

#image-map.net centre of text x,y


def make_cert(name):
    image_source = Image.open(r'Certificate.png')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name, font=FONT_FILE)
    draw.text((WIDTH-name_width/2, HEIGHT-name_height/2), name, fill=FONT_COLOR, font=FONT_FILE)
    image_source.save("./out/" + name +".png")
    print('printing certificate of: '+name)


data=pd.read_excel('data.xlsx')
names = list(data.Name)
for x in names:
    make_cert(x)
