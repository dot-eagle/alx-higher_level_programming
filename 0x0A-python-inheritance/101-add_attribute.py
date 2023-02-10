#!/usr/bin/python3

"""Python module that adds a new attribute
"""


def add_attribute(a_class, name, value):
    """ Adds new attribute to an object if it's possible """

    # Setup membership test
    attr_list = {int, str, float, list, dict, tuple, frozenset, type, object}

    if type(a_class) in attr_list:
        raise TypeError("can't add new attribute")

    a_class.__setattr__(name, value)
