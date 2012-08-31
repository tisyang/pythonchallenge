import re

file = "letters.txt"

pattern = re.compile(r"[a-z\A\Z]([A-Z]{3}[a-z][A-Z]{3})[a-z\A\Z]")

with open(file, "r") as f:
    c = f.read()
    m = pattern.findall(c)
    for i in m:
        print(i[3], end = "")