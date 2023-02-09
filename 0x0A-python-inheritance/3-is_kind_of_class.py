#!/usr/bin/python3

"""
Python module that returns True if the object is an instance of
the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """ Function that returns True if the object is an instance of
    the specified class ; otherwise False """

    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
