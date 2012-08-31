import re
import zipfile

z = zipfile.ZipFile('channel.zip', 'r')
p = re.compile(r' (\d+)$')
nothing = 90052
cm = ''

while True:
    str = z.read("{0}.txt".format(nothing)).decode()
    cm += z.getinfo("{0}.txt".format(nothing)).comment.decode()
    result = p.search(str)

    try:
        nothing = int(result.group(1))
    except Exception as ex:
        print("{0}.txt : {1:s}".format(nothing, str))
        print(ex)
        break;

print(cm)
