#!/usr/bin/python3

import json

"""
This is module defines a function that creates an Object from a “JSON file”

"""
def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”
        
    Args:
        filename (str): name of file tp save object to
        
            
    Returns:
        object: The loaded object from json file, or none if file is empty
    """

    with open(filename, 'r') as file:
        json_data = file.read()
        if json_data:
            return json.loads(json_data)
        else:
            return None
