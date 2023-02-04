#!/usr/bin/python3

"""
Module 101i-square: A class Square that defines a square
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
        position(self)
        position(self, value)
        my_print(self)
        """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position
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

    @property
    def position(self):
        """ Getter; V Return: position """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Setter
        value: sets position to tuple if value is tuple of 2 positive ints """
        self.__position = value
        er_msg = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple or len(value) != 2:
            raise TypeError(er_msg)
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError(er_msg)
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        area = self.__size * self.__size
        """
        Calculates area of square
        Returns: area
        """
        return (area)       # (self.__size **2)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] + "#" * self.__size
                            for rows in range(self.__size)]))

    def __str__(self):
        """ String representation of square n call to print
        Example: print(my_square) """
        string = ""
        if self.__size == 0:
            return (string)

        string += "\n" * self.position[1]
        string += "\n".join([" " * self.__position[0] + "#" * self.__size
                            for rows in range(self.__size)])
        return (string)
