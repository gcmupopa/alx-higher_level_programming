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

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
