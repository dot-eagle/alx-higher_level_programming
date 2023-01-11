#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    new_matrix = []
    for indx in matrix:
        new_matrix[len(new_matrix):] = [[num ** 2 for num in indx]]
    return (new_matrix)
