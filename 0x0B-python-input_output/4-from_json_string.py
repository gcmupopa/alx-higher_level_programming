#!/usr/bin/python3
import json

"""
This is 4-from_json_string that uses from_json_string function
"""

def from_json_string(my_str):
    """
    Returns an object repr by json string.

    Arguments:
        my_str: json string to be converted to python object.

    Returns:
        object: py data structure repr by json string.
    """
    
    return json.loads(my_str)
