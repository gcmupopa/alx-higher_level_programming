#!/usr/bin/python3

"""
This is module that defines Square class.
"""


class Square:
    """
    A class that represents a square.

    Attributes:
    - size (float): Length of square's sides
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
