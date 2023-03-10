#!/usr/bin/python3

"""
A Module that writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8)
    and returns the number of characters written """

    with open(filename, mode="w", encoding="utf-8") as f:
        wf = f.write(text)
        return (len(text))
