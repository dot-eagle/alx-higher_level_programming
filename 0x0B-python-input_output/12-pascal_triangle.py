#!/usr/bin/python3

"""
Pyhton Module that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """ Function hat returns a list of lists of integers
    representing the Pascal’s triangle of n """

    if n <= 0:
        return []

    sol1 = []
    if n > 0:
        for a in range (n):
            sol2 = [1 for _ in range(a + 1)]
            for c in range (a):
                if c != 0 and c != a:
                    sol2[c] = sol1[a - 1][c] +  sol1[a - 1][c - 1]
            sol1.append(sol2)
    return (sol1)

