#!/usr/bin/python3
""""
This is 2-append_write file that uses append_write function
"""

def append_write(filename="", text=""):
    """
    appends a string to text file (utf8) and returns num of characters added.

    Arguments:
        filename (str): name of file to be appended.

    Returns:
        int: num of characters appendec to file.
    """

    with open(filename, 'a', encoding='utf-8') as fl:
        chars = fl.write(text)
    return chars
