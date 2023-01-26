#!/usr/bin/python3

"""
Module 5-square: A class Square that defines a square
Defines class Square with private attribute size and public attribute area
Able to access and update size
Able to print to stdout the square using #'s
"""


class Square:
    """
    class Square definition
    Args:
        init allow square class to be used
        size (int): size of a side in square
    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
        print(self)
    """
    def __init__(self, size=0):
        self.__size = size
        """
        Initializes square
        Attributes:
            asign private instance attribute size
            __size (int): size of a side of square, defaults to 0 if none
        """

    @property
    def size(self):
        """
        Getter
        Returns: size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter
        Args:
            value: sets size to value, if int and >= 0
        """
        self.__size = value

        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        area = self.__size * self.__size
        """
        Calculates area of square
        Returns: area
        """
        return (area)       # (self.__size ** 2)

    def my_print(self):
        if self.__size >= 0:
            """
            Prints square with #'s
            """
            for x in range(self.__size):
                print("{}".format("#" * self.__size))
            else:
                print()
