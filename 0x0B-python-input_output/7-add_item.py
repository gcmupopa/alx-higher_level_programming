#!/usr/bin/python3

import sys
import json

"""
This is module defines a script that adds all arguments to a Python list, and then save them to a file

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
        
    if __name__ == '__main__':
        try:
            milist = load_from_json_file('add_item.json')
        except(FileNotFoundError, json.JSONDecodeError):
            milist = []

        milist.extend(sys.argv[1:])

        save_to_json_file(milist, 'add_item.json')
