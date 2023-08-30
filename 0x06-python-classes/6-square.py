#!/usr/bin/python3

"""
This is module that defines Square class.
"""


class Square:
    """
    A class that represents a square.

    Attributes:
    - size (float): Length of square's sides
    - position (tuple): Position of square
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method for retrieving position of square

        Returns:
        - tuple: Position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for setting position of square.

        Args:
        - value (tuple): Position value to be assigned

        Raises:
        - TypeError: if position is not a tuple of 2 positive integers
        - ValueError: if position contains negative integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("Position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates area of square.

        Returns:
        - int: Area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints square using character '#'

        Prints empty line if size is 0
        Adjusts the print based on the position at tribute
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
