#!/usr/bin/python3

"""
Python class MyList that inherits from list
"""


class MyList(list):
    """ class MyList that inherits from list """
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) order """
        print(sorted(self))
