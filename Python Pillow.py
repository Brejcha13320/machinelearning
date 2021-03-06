from PIL import Image, ImageFilter, ImageFont, ImageDraw

'''
#Open image using Image module
im = Image.open("D:\descarga.jpg")
#Show actual Image
im.show()
#Show rotated Image
im = im.rotate(45)
im.show()
'''



'''
def tnails():
   try:
      image = Image.open('D:\pug.jpg')

      image.show()

      image.thumbnail((90,90))
      image.save('D:\pug.jpg')
      image1 = Image.open('D:\pug.jpg')
      image1.show()
   except IOError:
      pass
tnails()
'''

'''
image = Image.open("D:\paisaje.jpg")
r, g, b = image.split()
image.show()
image = Image.merge("RGB", (b, g, r))
image.show()
'''


'''
#Open existing image
OriImage = Image.open('D:\pug.jpg')
OriImage.show()

blurImage = OriImage.filter(ImageFilter.BLUR)
blurImage.show()
#Save blurImage
blurImage.save('D:\pug.jpg')
'''

'''
# Open an already existing image
imageObject = Image.open("D:\paisaje.jpg")

# Do a flip of left and right
hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)

# Show the original image
imageObject.show()

# Show the horizontal flipped image
hori_flippedImage.show()
'''





'''

#Create an Image Object from an Image
im = Image.open('D:\paisaje2.jpg')
width, height = im.size

draw = ImageDraw.Draw(im)
text = "Estrellas"

font = ImageFont.truetype('arial.ttf', 36)
textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text
margin = 10
x = width - textwidth - margin
y = height - textheight - margin

# draw watermark in the bottom right corner
draw.text((x, y), text, font=font, fill=(255, 0, 0))
im.show()


#Save watermarked image
im.save('D:\pug.jpg')

'''

