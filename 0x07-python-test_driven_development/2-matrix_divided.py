#!/usr/bin/python3

"""
This is a module that defines matrix_divided .
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    
    matrix must be a list of lists of integers or floats, otherwise raise a TypeError
    exception with the message matrix must be a matrix (list of lists) of
    integers/floats
    
    Each row of the matrix must be of the same size, otherwise raise a TypeError
    exception with the message. 
    
    Each row of the matrix must have the same size div must be a number (integer or float), otherwise raise a TypeError exception with
    the message div must be a number div can’t be equal to 0 , otherwise raise a ZeroDivisionError exception with the message division by zero
    
    All elements of the matrix should be divided by div , rounded to 2 decimal places
    
    Arguments:
    matrix -- a list of lists of integers or floats
    div -- number (integer or float)

    Raises:
    TypeError -- if matrix or div is not int or float
    TypeError -- each row of matrix should be of same size
    
    
    Returns:
    int -- new matrix
    """
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be list of lists of integers or floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
        
    if not isinstance(div, (int, float)):
        raise TypeError("div must be an number")

    if div == 0:
        raise ZeroDivisionError("div must be number")
        
    result = []
    for row in matrix:
        nuro = []
        for element in row:
            nu_el = round(element / div, 2)
            nuro.append(nu_el)
        result.append(nuro)

    return result
