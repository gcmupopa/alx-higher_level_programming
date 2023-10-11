#!/usr/bin/python3
import json

"""
This is 6-load_from_json_file which uses load_from_json_file function that creates an Object from a “JSON file”:
"""

def load_from_json_file(filename):
    """
    This function creates an Object from a “JSON file”:.

    Args:
        filename (str): name of json file to load.

    Returns:
        object: object created from json file.
    """

    with open(filename, 'r') as fl:
        return json.load(fl)
