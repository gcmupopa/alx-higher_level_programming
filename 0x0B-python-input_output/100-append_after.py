#!/usr/bin/python3

"""
This module defines a function that inserts a line of text to a file, after each line containing a specific string

"""

def append_after(filename="", search_string="", new_string=""):
    """
    inserts line of text to file after each line containing specific string.
        
    Args:
        filename (str): name of file
        search_string (str): string to search for in each line
        new_string (str): line of text to insert after each line containg search string
    """
    tee_filename = filename + "tmp"

    with open(filename, "r") as file, open(tee_filename, "w") as tee_file:
        for line in file:
            tee_file.write(line)
            if search_string in line:
                tee_file.write(new_string + "\n")

    with open(tee_filename, "r") as tee_file:
        input = tee_file.read()

    with open(filename, "w") as file:
        file.write(input)

    with open(tee_filename, "w") as tee_file:
        pass
