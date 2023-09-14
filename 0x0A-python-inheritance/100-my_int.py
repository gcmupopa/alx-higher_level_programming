#!/usr/bin/python3

"""
This module defines a class MyInt that inherits from int

"""


class MyInt(int):
    """
    This class inherits from int.

    """

    def __ne__(self, other):
        """
        inequality op inverted.

        Args:
            other (Any): object to compare with

        Returns:
            bool: True if objects equal else false.

        """
        return super().__eq__(other)

    def __eq__(self, other):
        """
        equality op inverted.

        Args:
            other (Any): object to compare with.

        Returns:
            True if objects not equal else false.
        """
        return super().__ne__(other)
