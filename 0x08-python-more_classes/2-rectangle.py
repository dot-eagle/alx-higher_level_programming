#!/usr/bin/python3

"""
Module to define a class Rectangle
(based on 1-rectangle.py)
"""


class Rectangle:
    """
    creating a Rectangle class
    """
    def __init__(self, width=0, height=0):
        """ Instantiation Method for Rectangle
            Args:
                width (int type): of the rectangle
                height (int type): of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """ Private instance attribute and
        Getter for height: height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ Private instance attribute
             and Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """

        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """ Public instance method and
        getter for rectangle area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Public instance method and
        getter for  rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__height + self.__width))
