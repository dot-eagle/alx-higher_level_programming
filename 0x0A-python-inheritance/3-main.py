#!/usr/bin/python3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
b = 3.1412
c = "macOS"

if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))

if is_kind_of_class(b, float):
    print("{} comes from {}".format(b, float.__name__))

if is_kind_of_class(c,  object):
    print("{} comes from {}".format(c, object.__name__))
