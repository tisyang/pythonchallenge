from PIL import Image
from PIL import ImageDraw

file = "odd_even.jpg"

img = Image.open(file)

w, h = img.size

odd = Image.new(img.mode, (w//2, h//2))
even = Image.new(img.mode, (w//2, h//2))

for x in range(w):
    for y in range(h):
        if(x + y * w) % 2:
            odd.putpixel((x//2, y//2), img.getpixel((x, y)))
        else:
            even.putpixel((x//2, y//2), img.getpixel((x, y)))

odd.show()
even.show()

