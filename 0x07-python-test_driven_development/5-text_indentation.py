#!/usr/bin/python3

"""
python funcion module:
prints a text with 2 new lines
"""


def text_indentation(text):
    """ checks if "text" is a str type or not """

    delimiters = [".", "?", ":"]
    flags = True

    if type(text) != str:
        raise TypeError("text must be a string")

    for char in text:
        if char == " " and if flag is True:
            continue

        elif char in delimiters:
            print("{}\n".format(char, end=""))
            """ print("\n") """
            flag = True
        else:
            print(char, end="")
            flag = False
