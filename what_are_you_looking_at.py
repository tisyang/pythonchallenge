# pythonchallenge 10
# http://www.pythonchallenge.com/pc/return/bull.html
#
#
# sequence: a = [1, 11, 21, 1211, 111221,
# 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211...
#
# puzzle: len(a[30]) = ?

import re
pattern = re.compile(r'(\d)\1*')


def repl(match):
    s = match.group(0)
    assert s
    return "{0:d}{1:s}".format(len(s), s[0])

def read_digit_str(str):
    # must be a digit string
    assert str.isdigit()

    return pattern.sub(repl, str)

def sequence():
    s = "1"
    while True:
        yield s
        s = read_digit_str(s)

for index, item in enumerate(sequence()):
    if index == 30:
        print(len(item))
        break
