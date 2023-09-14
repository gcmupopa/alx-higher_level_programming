#!/usr/bin/python3

"""
This module defines a class BaseGeometry, class Rectangle and Square.

"""


class BaseGeometry:
    """
    base class for geometry

    """

    def area(self):
        """
        formulates area

        Raises:
             Exception: indicates area() method is not implemented.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates int value.

        Args:
            name (str): name of value.
            value (int): value to be validated

        Raises:
             TypeError: if value is not int.
             ValueError: if value is less or equal to 0.
        """

        if not isinstance(value, int) and not str(value).isdigit():
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    This is class Rectangle that inherits from BaseGeometry.

    """

    def __init__(self, width, height):
        """
        instantiate Rectangle instance.

        Args:
        width (int): width of rectangle
        height (int): height of rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates area of rectangle

        Returns:
            int: area of rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        returns string representation of rectangle.

        Returns:
            str: string representation of rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    """

    def __init__(self, size):
        """
        Instantiate Square instance.

        Args:
            size (int): Size of square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        formulates area of square.

        Returns:
            int: area of square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns string repr of square.

        Returns:
            str: string repr of square.
        """
        return f"[Square] {self.__size}/{self.__size}"
