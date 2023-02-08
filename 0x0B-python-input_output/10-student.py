#!/usr/bin/python3

"""
class Student that defines a student
(based on 9-student.py)
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

    ''' def to_json(self): '''
    def to_json(self, attrs=None):
        """ Public method that retrieves a json dictionary
        representation of an instance (same as 8-class_to_json.py) """
        if attrs is None or type(attrs) is not list:
            return (self.__dict__)
        else:
            jdic = {}
            for n in attrs:
                if n in self.__dict__:
                    jdic[n] = self.__dict__[n]

                """ Public method  that retrieves a dictionary
        representation of class """

        return (jdic)
