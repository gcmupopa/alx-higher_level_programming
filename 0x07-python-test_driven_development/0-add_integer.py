#!/usr/bin/python3

"""
This is a module that defines add_integer.
"""

def add_integer(a, b=98):
    """
    Adds two integers
    
    This function takes two elems, a and b and return their sum.
    if a or b is not int or float raise exception error.
    if a or b is float, cast to an int before performing the addition.
    
    Arguments:
    a -- First int or float
    b -- Second int or float(default 98)
    
    Raises:
    TypeError -- if a or b is not int or float
    
    Returns:
    int -- Result of a and before
    """
    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
        
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
        
    a = int(a)
    b = int(b)
    return a + b
