#!/usr/bin/python3

import json

"""
This is module returns an object (Python data structure) represented by json

"""


def from_json_string(my_str):
    """
    function that returns convert a JSON string to python object

    Args:
        my_str: json string to be converted

    Returns:
        object: The python object represented by json string
    """

    try:
        return json.loads(my_str)
    except ValueError:
        erm = f"[ValueError] Invalid JSON string: {my_str}"
        return erm
