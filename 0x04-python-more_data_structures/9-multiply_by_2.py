#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    for keys in a_dictionary:
        return dict(zip(a_dictionary.keys(), (b * 2 for b in a_dictionary.values())))
