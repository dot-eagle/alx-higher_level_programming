#!/usr/bin/python3

"""
Python module that writes an Object to a text file,
using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text
    file, using a JSON representation """

    with open(filename, mode="w", encoding="UTF-8") as jf:
        json.dump(my_obj, jf)
