#!/usr/bin/python3

"""
This is a module that prints prints a square with the character # .
"""
def text_indentation(text):
    """
     prints a text with 2 new lines after each of these characters: . , ? and :
     
     Args:
        text (str): The input text.
        
    Raises:
        TypeError: If text is not a string.
        
    Example:
        >>> text_indentation("Hello. How are you? This is, awesome.")
        
        Hello
        
        How are you
        
        This is
        
        awesome
        
    Preconditions:
        - text should be a string.
        
    Postconditions:
        - Text should be printed with 2 new lines after each occurrence of '.', '?' and ':'.
        
    """

    if not isinstance(text, str):
        raise TypeError("text should be a string.")
    
    divider = ['.', '?', ':']
    result = ""
    prev = ""

    for char in text:
        result += char

        if char in divider:
            result += "\n\n"

        prev = char

    print(result.strip())
