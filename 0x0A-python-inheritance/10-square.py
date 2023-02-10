#!/usr/bin/python3

"""
Python module of class Square that inherits from Rectangle (9-rectangle.py)
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Function of a class Square that inherits from Rectangle
    (based on 9-rectangle.py) """

    def __init__(self, size):
        """ Instantiation with private instances - size """

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ area: Public instance method
        to compute and return area of Square """

        area_sqr = self.__size * self.__size
        return (area_sqr)


'''
    def __str__(self):
        """ Magic method to return string description of Rectangle """

        str_rep = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return (str_rep)

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method that validates value """
        self.name = name
        self.value = value

        if type(value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
            '''
