#!/usr/bin/python3

"""
Python module of class BaseGeometry (based on 5-base_geometry.py).
"""


class BaseGeometry:
    """ Function of a class BaseGeometry
    (based on 5-base_geometry.py) """

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
