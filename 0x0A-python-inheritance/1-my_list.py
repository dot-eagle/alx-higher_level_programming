#!/usr/bin/python3

"""
Python class MyList that inherits frm list
"""


class MyList(list):
    """ class MyList that inherits frm list """
    def print_sorted(self):
        """ prints the list, but in ascending sort order """
        print(sorted(self))
