#!/usr/bin/python3

"""
Module 6-square: A class Square that defines a square
Defines class Square with private attribute size and public attribute area
Able to access and update size
Able to print to stdout the square using #'s
"""


class Square:
    """
    class Square definition
    Args:
        init allow square class to be used
        size (int): size of the sides of a square
    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
        position(self, value)
        position(self)
        print(self)
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        """
        Initializes square
        Attributes:
            asign private instance attribute size
            __size (int): size of a side of square, defaults to 0 if none
           int position (int): tuple of two positive integers
        """
        try:
            self.position = position
        except TypeError as err:
            print(err)

    @property
    def position(self):
        """
        Getter
        Return: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        posta = "position must be a tuple of 2 positive integers"
        """
        Setter
        Args:
            value: sets position to tuple if value is tuple of 2 positive ints
        """
        if type(value) is not tuple or len(value) != 2:
            self.__position = None
            raise TypeError(posta)
        elif type(value[0]) is not int or type(value[1]) is not int:
            self.__position = None
            raise TypeError(posta)
        elif value[0] < 0 or value[1] < 0:
            self.__position = None
            raise TypeError(posta)
        else:
            self.__position = value

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

        if type(value) != int:
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
        if self.__size != 0:
            """
            Prints square with #'s
            """
            for nrow in range(self.__position[1]):
                print("\n", end="")
            for rows in range(self.__size):
                print("{}{}".format(" " * self.position[0], "#" * self.__size))
            if self.__size == 0:
                print("")
