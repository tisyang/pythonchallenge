from PIL import Image
from PIL import ImageDraw

coords = [179,284,214,311,255,320,281,226,319,224,363,309,339,222,371,225,411,229,404,242,415,252,428,233,428,214,394,207,383,205,390,195,423,192,439,193,442,209,440,215,450,221,457,226,469,202,475,187,494,188,494,169,498,147,491,121,477,136,481,96,471,94,458,98,444,91,420,87,405,92,391,88,376,82,350,79,330,82,314,85,305,90,299,96,290,103,276,110,262,114,225,123,212,125,185,133,138,144,118,160,97,168,87,176,110,180,145,176,153,176,150,182,137,190,126,194,121,198,126,203,151,205,160,195,168,217,169,234,170,260,174,282]

xy = []
for i in range(0, int(len(coords)/2)):
    x, y = coords[i*2], coords[i*2 + 1]
    xy.append((x, y))

new = Image.new("RGB", (640, 480))
draw = ImageDraw.Draw(new)

old = None
for x in xy:
    if not old:
        draw.point(x, (255, 255, 255))
    else:
        draw.line((old, x), (255, 255, 255))
    old = x

new.save("a.jpg", "JPEG")
