#!/usr/bin/python3

"""
Python function that prints a square
with the character #
"""


def print_square(size):
    """ returns a square with size lenght """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    ''' elsereturn (None) '''

    for side1 in range(size):
        print("{}".format("#" * size))

        """ for side2 in range(size):
            if side1 < (size - 1):
                print() """
