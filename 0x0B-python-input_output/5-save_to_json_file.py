#!/usr/bin/python3
import json

"""
This is 5-save_to_json_file module that writes an Object to a text file, using a JSON representation:
"""

def save_to_json_file(my_obj, filename):
    """
    This function writes an object to text file using json repr.

    Args:
        my_obj (object): object to be serialised and saved to the file.
        filename (str): name of file to save json data to.

    Returns:
        None
    """

    with open(filename, 'w') as fl:
        json.dump(my_obj, fl)
