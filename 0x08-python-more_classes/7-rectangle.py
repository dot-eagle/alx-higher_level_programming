#!/usr/bin/python3

"""
Module to define a class Rectangle
(based on 6-rectangle.py)
"""


class Rectangle:
    """
    creating a Rectangle class
    """

    """ Public attribute of Rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instantiation Method for Rectangle
            Args:
                width (int type): of the rectangle
                height (int type): of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Returns string representation of a class Rectangle"""
        string_rep = ""
        if self.__width == 0 or self.__height == 0:
            return (string_rep)

        for x in range(self.__height):
            string_rep += (str(self.print_symbol) * self.__width)
            if x != self.__height - 1:
                string_rep += "\n"
        return (string_rep)

    def __repr__(self):
        """ return a string representation of the rectangle
        class to recreate a new instance by using eval() """

        w = str(self.__width)
        h = str(self.__height)

        return ("Rectangle({}, {})".format(w, h))

    def __del__(self):
        """Printsthe message 'Bye rectangle...'
        when an instance of Rectangle is deletion is called
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
        ''' Rectangle.number_of_instances -= 1 '''
