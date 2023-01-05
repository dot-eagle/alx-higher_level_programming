#!/usr/bin/python3
def uppercase(str):
    for s in str:
        s = ord(s)

        if (ord("a") <= s <= ord("z")):
            s = s - 32
        print(f"{s:c}".format(s), end='')
    print()
