#!/usr/bin/python3

"""
This is a module that prints first name.
"""

def say_my_name(first_name, last_name=""):
    '''
    prints first and last name 
    
    Arguments:
        first_name(str): The first name.
        last_name(str, optional): The last name. Defaults to ''.
    
    Raises:
        - TypeError: if first_name or last_name is not a string.

    Example:
        >>> say_my_name("Gamue", "Mupopa")
        'My name is Gamue Mupopa'
        >>> say_my_name("Palmer")
        'My name is Palmer'

    Preconditions:
        - first_name must be a string.
        - last_name must be a string if provided.

    Postconditions:
        - Full name is printed on terminal.
    
    Returns:
        Nothing
    
    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string.")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string.")
    
    funa = first_name + ' ' + last_name
    print("My name is", funa.strip())
