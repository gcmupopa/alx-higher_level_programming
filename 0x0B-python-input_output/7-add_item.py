#!/usr/bin/python3
import sys
from 6-load_from_json_file import load_from_json_file
from 5-save_to_json_file import save_to_json_file

"""
This is 7-add_item that uses save_to_json_file from 5-save_to_json_file.py and load_from_json_file from 6-load_from_json_file.py
"""

def add_items():
    """
    adds all arguments to a Python list, and then save them to a file

    Returns:
        None
    """

    try:
        items = load_from_json_file('add_item.json')
    except ValueError:
        itm = []

    nui = sys.argv[1:]
    itm.extend(nui)

    save_to_json_file(itm, 'add_item.json')

if __name__ == '__main__':
    add_items()
