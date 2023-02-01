#!/usr/bin/python3

"""
python funcion
prints a text with 2 new lines 
"""


def text_indentation(text):
    """ checks if "text" is a str type or not """

    flag = True
    delimiters = ["?", ".", ":", ","]

    if type(text) != str:
        raise TypeError("text must be a string")

    for char in text:
        print("{}".format(char), end="")
        if char in delimiters:
            print("\n")

