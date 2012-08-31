file = "ocr.txt"
with open(file, "r") as f:
    c = f.read()
    s = set(c)
    print(s)
    print( len(s))
    d = []
    for x in s:
        if(c.count(x) == 1):
            d.append(c.index(x))

    d.sort()
    for x in d:
        print(c[x], end = "")

