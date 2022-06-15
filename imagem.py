from PIL import Image, ImageDraw, ImageFont

# creating new Image object 
img = Image.new("RGB", (220,50), color=(255,255,255,0))

font = ImageFont.truetype('Arimo-BoldItalic.ttf', 50)
text = '0000035'
# create rectangle image
img1 = ImageDraw.Draw(img)
img1.text((0,0), text=text, font=font, fill=0, align="center")
img.show()
img.save('img.png', "PNG")