#!/usr/bin/python3

"""
class Student that defines a student
"""


class Student:
    """ class Student that defines a student
        Args: Public instance attributes:
            first_name
            last_name
            age """

    def __init__(self, first_name, last_name, age):
        """ Instantiation with public instatnces """
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def to_json(self):
        """ Public method  that retrieves a dictionary
        representation of class """

        return (self.__dict__)
