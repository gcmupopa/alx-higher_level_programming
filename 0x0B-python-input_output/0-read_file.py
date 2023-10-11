#!/usr/bin/python3
""""
This is 0-read_file that uses read_file function
"""

def read_file(filename=""):
    """
    Reads text file (utf8) and prints to stdout

    Arguments:
        filename (str): name of file to read

    Returns:
        None
    """

    with open(filename, 'r', encoding='utf-8') as fl:
        out = fl.read()
        print(out)
