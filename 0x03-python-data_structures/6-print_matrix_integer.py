#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for ro in matrix:
        for elem in ro:
            print("{:d}".format(elem), end=' ')
        print()
