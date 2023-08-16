#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    nu_matrix = []

    for row in matrix:
        nu_ro = []

        for number in row:
            byself = number ** 2
            nu_ro.append(byself)

        nu_matrix.append(nu_ro)

    return nu_matrix
