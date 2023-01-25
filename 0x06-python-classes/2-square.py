#!/usr/bin/python3

"""
Module 2-square: A class Square that defines a square
Defines class Square with private attribute size and validates size
"""


class Square:
    """
    class Square definition
    Args:
        init allow square class to be used
        size (int): size of a side in square
    """
    def __init__(self, size=0):
        self.__size = size
        """
        Initializes square
        Attributes:
            asign private instance attribute size
            __size (int): size of a side of square, defaults to 0 if none
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
