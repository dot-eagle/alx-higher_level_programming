#!/usr/bin/python3

"""
Module 102-square: A class Square that defines a square
Defines class Square with private attribute size and public attribute area
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
        return (area)       # (self.__size * self.__size)

    def __eq__(self, others):
        """ Checks n compares equality """
        return (self.size == others.size)

    def __ne__(self, others):
        """ checks for inequality """
        return (self.size != others.size)

    def __lt__(self, others):
        """ checks if less than """
        return (self.size < others.size)

    def __le__(self, others):
        """ checks if less than or equal to """
        return (self.size <= others.size)

    def __gt__(self, others):
        """ checks if greater than """
        return (self.size > others.size)

    def __ge__(self, others):
        """ checks if greater than or equal to """
        return (self.size >= others.size)
