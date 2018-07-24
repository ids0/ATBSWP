from PIL import Image, ImageDraw, ImageFont
import os
os.chdir(r'D:\Drive\Code\ATBSWP\Chapter_17')

im = Image.new('RGBA',(200,200),'white')
draw = ImageDraw.Draw(im)
draw.text((20,150),'Hello World!', fill='purple', )
fontsFolder = 'C:\Windows\Fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFolder,'arial.ttf'), 32)
draw.text((100,150),'Howdy', fill='gray', font=arialFont)
im.save('text.png')