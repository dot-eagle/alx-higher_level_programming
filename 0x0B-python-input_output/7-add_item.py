#!/usr/bin/python3

"""
Python Module that adds all arguments to a Python list,
and then save them to a file
"""

import json
import sys


load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

try:
    jsonload = load_from_json_file("add_item.json")
except IOError:
    jsonload = []

arg_count = len(sys.argv)
for x in range(1, arg_count):
    jsonload.append(sys.argv[x])
save_to_json_file(jsonload + (sys.argv[1:]), "add_item.json")
