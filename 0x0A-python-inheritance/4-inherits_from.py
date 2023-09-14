#!/usr/bin/python3

"""
This module defines a function that returns True if the object is an instance

"""


def inherits_from(obj, a_class):
    """
    checks if object is instance of class by inheritance

    Args:
        obj: object to check.
        a_class: class to compare against.

    Returns:
        True if object is instance of class false otherwise

    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
