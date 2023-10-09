#!/usr/bin/python3

"""
This module defines an empty class BaseGeometry

"""


class BaseGeometry:
    """
    class that defines empty class basegeometry

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

        if not isinstance(name, str):
            raise TypeError("namemust be a string")
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

        super().__init__()
        try:
            self.integer_validator("width", width)
            self.integer_validator("height", height)
        except (TypeError, ValueError) as e:
            print(f"[{e.__class__.__name__}] {e}")
        else:
            self.__width = width
            self.__height = height

    def area(self):
        """
        Calculates area of rectangle

        Returns:
            int: area of rectangle.
        """
        return self.__width * self.__height
