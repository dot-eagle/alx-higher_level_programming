#!/usr/bin/python3
for numb in range(0, 100):
    if (numb == 99):
        print("{0:0=2d}".format(numb))
    else:
        print("{0:0=02d}".format(numb), end=", ")
