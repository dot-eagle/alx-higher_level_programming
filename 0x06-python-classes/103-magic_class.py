#!/usr/bin/python3

import math

""" Define Python class module MagicClass """


class MagicClass:
    """ constructs & initializes ethods area and circumference """
    def __init__(self, radius=0):
        """Initialize MagicClass"""
        self.__radius = 0

        if type(radius) != int and if type(radius) != float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ compute area """
        area = math.pi * (self.__radius **2)
        return (area)

    def circumference(self):
        """ compute circumference """
        circ = math.pi * self.__radius * 2
        return (circ)
