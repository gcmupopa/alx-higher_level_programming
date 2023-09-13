#!/usr/bin/python3

import json

"""
This is module returns the JSON representation of an object (string)

"""


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an object (string)

    Args:
        my_obj: name of file to be read

    Returns:
        str: The json representation of the object
    """

    return json.dumps(my_obj)
