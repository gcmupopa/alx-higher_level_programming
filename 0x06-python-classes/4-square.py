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
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving size of square.

        Returns:
        - int: Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set size of square

        Args:
        - value (int): Size value to be assigned

        Raises:
        - TypeError: if size is not integer
        - ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates area of square.

        Returns:
        - int: Area of square
        """
        return self.__size ** 2
