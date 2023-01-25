#!/usr/bin/python3

"""
Module 2-square
Defines class Square with private attribute size and validates size
"""


class Square:
    def __init__(self, size=0): 
    """ 
    init allow square class to be used
    """
        self.__size = size
        """
        asign private instance attribute size
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
