#!/usr/bin/python3

"""
add_integer:
    computes and returns integer sum of two digits
"""


def add_integer(a, b=98):
    """
    check if parameter if int, return sum
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return (a + b)
