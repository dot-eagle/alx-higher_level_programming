#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    print("{}".format("\n".join([" ".join(["{:d}".format(t)
        for t in m]) for m in matrix])))


