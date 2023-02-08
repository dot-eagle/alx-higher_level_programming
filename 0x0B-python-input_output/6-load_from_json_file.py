#!/usr/bin/python3


"""
Python Module that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    ''' Function that creates & returns an Object from a “JSON file” '''

    with open(filename, mode="r", encoding="UTF-8") as jf:
        return json.load(jf)
