#!/usr/bin/python3

import json

"""
This is module defines a function returns the dictionary description with simple data structure (list,
dictionary, string, integer and boolean) for JSON serialization of an object

"""
def class_to_json(obj):
    """
    function returns the dictionary description with simple data structure
        
    Args:
        obj: is an instance of a Class
        
            
    Returns:
        dict: dictionary description with simple data structure
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("Object is not an instance of a class.")
    
    outcome = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            outcome[key] = value

    return outcome
