#!/usr/bin/python3

"""
Python Module for JSON serialization of an object
"""


def class_to_json(obj):
    """ Function that returns the dictionary description with simple
    data structure for JSON serialization of an objects.
    Args:
        obj - a serializable instance / attribute of the Class """

    return (obj.__dict__)
