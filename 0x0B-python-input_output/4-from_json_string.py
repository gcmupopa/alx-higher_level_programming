#!/usr/bin/python3

import json

"""
This is module returns an object (Python data structure) represented by a JSON string

"""
def from_json_string(my_str):
    """
    function that returns convert a JSON string to python object
        
    Args:
        my_str: json string to be converted
        
            
    Returns:
        object: The python object represented by json string
    """
        
    return json.loads(my_str)
