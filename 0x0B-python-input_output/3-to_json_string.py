#!/usr/bin/python3
import json

"""
This is 3-to_json_string that uses to_json_string function
"""

def to_json_string(my_obj):
    """
    Returns json repre of object string.

    Arguments:
        my_obj: object to be converted to json.

    Returns:
        str: json repr of object
    """
    if isinstance(my_obj, set):
        my_obj = list(my_obj)
    return json.dumps(my_obj)
