#!/usr/bin/python3

"""
This is a module that prints prints a square with the character # .
"""

def print_square(size):
    '''
    prints a square with the character '#".
    
    Arguments:
        size (int): The length of the square.
    
    Raises:
        - TypeError: if size is not an int or a float.
        - ValueError: if size is less than 0.

    Example:
        >>> print_square(3)
        ###
        ###
        ###
        >>> print_square(5)
        #####
        #####
        #####
        #####
        #####

    Preconditions:
        - size must be an integer.
        - last_name must be a string i.

    Postconditions:
        - Square is printd to the console.
    
    Returns:
        Nothing
    
    '''

    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError("Size must be an integer.")
    if isinstance(size, float) and size < 0:
        raise TypeError("Size must be an integer.")
    if size < 0:
        raise ValueError("Size must be >= 0.")
    
    for _ in range(size):
        print("#" * size)
    
    
