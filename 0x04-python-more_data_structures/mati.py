#!/usr/bin/python3

from math import sin, cos, tan, pi

def map_functions(x, functions):
    """ map an iterable of functions on the the object x """
    result = []
    for func in functions:
        result.append(func(x))
    return result
family_of_functions = (sin, cos, tan)
print(map_functions(pi, family_of_functions))


"""
def map_functions(x, functions):
    return [ func(x) for func in functions ]

"""
