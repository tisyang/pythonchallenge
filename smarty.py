from PIL import Image
import io
import urllib.request
import re

img = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read()
im = Image.open(io.BytesIO(img))
print(im.mode)
##for x in range(im.size[0]):
##    for y in range(im.size[1]):
##        pix = im.getpixel((x, y))
##        if pix[0] == pix[1] == pix[2]:
##            print(x, ':', y)

#0 : 43 -> 607:51
l = []
for i in range(0, 608, 7):
    pix = im.getpixel((i, 45))
    l.append(chr(pix[0]))

str = "".join(l)
ans = re.findall(r'\d+', str)
print("".join(map(chr, map(int, ans))))

