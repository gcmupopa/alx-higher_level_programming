#!/usr/bin/python3
def read_file(filename=""):
    """
    Function that reads a text file and prints its contents to stdout

    Args:
        filename: name of file to be read

    Returns:
        None
    """

    with open(filename, 'r', encoding="UTF-8") as file:
        for line in file:
            print(line, end="")
