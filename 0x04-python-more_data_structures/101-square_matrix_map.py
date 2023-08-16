#!/usr/bin/python3

def square_matrix_map(my_list=[]):
    return list(map(lambda x, m=matrix: list(map(lambda y, m=m: y**2, x)), matrix))
