#!/usr/bin/python3

"""
Python module that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """ Function that returns True if the object is an instance of a class
    that inherited from the specified class ; otherwise False """

    if type(obj) != a_class and issubclass(type(obj), a_class):
        return (True)
    else:
        return (False)

    '''if type(obj) is a_class:
        return (False)
    else:
        return (True)'''
