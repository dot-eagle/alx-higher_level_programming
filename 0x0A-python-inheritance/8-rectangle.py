#!/usr/bin/python3

"""
Python module of class Rctangle that inherits from  (7-base_geometry.py)
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Function of a class Rectangle that inherits from BaseGeometry
    (based on 7-base_geometry.py) """

    def __init__(self, width, height):
        """ Instantiation with private instances - width and height """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
'''
    def area(self):
        """ area: Public instance method """
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
