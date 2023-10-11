#!/usr/bin/python3

"""
This is class_to_json module that uses class_to_json function 

"""

def class_to_json(obj):
    """
    returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object

    Arg:
        obj (object): to be serialised.

    Returns:
        dict: a dictionary repr with simple data structure repr onbject.

    Raises:
        TypeError: if object is not instance of a class.
    """
    
    if not isinstance(obj, type):
        raise TypeError("Object must be an instance of a class.")

    attrb = {}

    for nem, val in obj.__dict__.items():
        if isinstance(val, (list, dict, str, int, bool)):
            attrb[nem] = val

    return attrb
