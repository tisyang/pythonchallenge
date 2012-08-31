import urllib.request
import re

if __name__ == '__main__':
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    index = '8022'
    counter = 1
    pattern = re.compile(r'nothing is (\d+)')

    while True:
        try:
            request = urllib.request.Request(url + index)
            response = urllib.request.urlopen(request)
            content = str(response.read().decode())
            response.close()
            print(counter, content)

            result = pattern.search(content)
            if not result:
                break;

            index = result.group(1)
            counter += 1
        except Exception as ex:
            print(ex)
            break

