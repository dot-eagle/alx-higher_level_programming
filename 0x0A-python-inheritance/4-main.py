#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
b = False
c = True

if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))

if inherits_from(b, bool):
    print("{} inherited from class {}".format(b, bool.__name__))

if inherits_from(c, object):
    print("{} inherited from class {}".format(c, object.__name__))
