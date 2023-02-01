#!/usr/bin/python3

"""
function that divides all elements of a matrix by 'div'
"""


def matrix_divided(matrix, div):
    """ Matrix must be a list of
    lists of integers, floats
    and returns a new matrix """

    divi_1 = "div must be a number"
    divi_2 = "division by zero"
    emsg_1 = "matrix must be a matrix (list of lists) of integers/floats"
    emsg_2 = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(emsg_1)

    for itm in matrix:
        if not isinstance(itm, list):
            raise TypeError(emsg_1)
        if len(matrix[0]) != len(itm):
            raise TypeError(emsg_2)
        for e in itm:
            if type(e) != int and type(e) != float:
                raise TypeError(emsg_1)

        if type(div) != int and type(div) != float:
            raise TypeError(divi_1)
        if div == 0:
            raise ZeroDivisionError(divi_2)

        ans = [[round(e / div, 2) for e in itm] for itm in matrix]

        return (ans)
