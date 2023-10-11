#!/usr/bin/python3
""""
This is 1-write_file that uses write_file function
"""

def write_file(filename="", text=""):
    """
    Writes a string to text file (utf8) and returns num of characters written.

    Arguments:
        filename (str): name of file to be written

    Returns:
        int: num of characters written to file.
    """

    with open(filename, 'w', encoding='utf-8') as fl:
        chars = fl.write(text)
    return chars
