#!/usr/bin/python3

"""
A Module that returns the JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """ Function that returns JSON representation of an object (string) """

    return json.dumps(my_obj)
