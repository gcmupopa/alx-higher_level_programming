#!/usr/bin/python3

"""
This is module that defines append_write which appends a string to a text
"""


def append_write(filename="", text=""):
    """
    Function that appends a string to a text file and returns num chars

    Args:
        filename: name of file to be read
        text: string to be appended to the file

    Returns:
        int: The number of characters written to the file
    """

    with open(filename, 'a', encoding="UTF-8") as file:
        file.write(text)
        return len(text)
