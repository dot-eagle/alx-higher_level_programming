#!/usr/bin/python3

from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        com = True

    except Exception as xp:
        stderr.write("Exception: {}\n".format(str(xp)))
        com = False

    return (com)
