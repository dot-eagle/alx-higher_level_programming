#!/usr/bin/python3

""" Python Module that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """ Function that inserts a line of text to a file,
    after each line containing a specific string """

    with open(filename, mode="r+", encoding="utf-8") as opf:
        tex = opf.readlines()

    num = 0
    with open(filename, mode="w", encoding="utf-8") as wrf:
        for lines in tex:
            num += 1
            if search_string in lines:
                tex.insert(num, new_string)
        for lines in tex:
            wrf.write(lines)
