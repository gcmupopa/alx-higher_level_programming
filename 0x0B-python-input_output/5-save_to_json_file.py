#!/usr/bin/python3

import json

"""
This is module defines a function that writes an Object to a text file, using a JSON representation

"""
def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, using a JSON representation
        
    Args:
        my_obj (object): object to be saved
        filename (str): name of file tp save object to
        
            
    Returns:
        None
    """

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
