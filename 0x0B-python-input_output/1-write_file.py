#!/usr/bin/python3

"""
This is module that defines write_file which writes a string to a text file (utf8) and returns the number of characters wriiten
"""

def write_file(filename="", text=""):
    """
    Function that writes a string to a text file and returns the number of characters written
        
    Args:
        filename: name of file to be read
        text: string to be appended to the file
            
    Returns:
        int: The number of characters written to the file
    """
        
    with open(filename, 'w', encoding="UTF-8") as file:
        file.write(text)
        return len(text)
