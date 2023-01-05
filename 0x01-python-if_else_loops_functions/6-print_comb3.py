#!/usr/bin/python3
for numb in range(0, 9):
    for numb2 in range(numb + 1, 10):
        if (numb == 8 and numb2 == 9):
            print(f"{numb:d}{numb2:d}".format(numb, numb2))
        else:
            print(f"{numb:d}{numb2:d}".format(numb, numb2), end=", ")
