#!/usr/bin/python3

"""
This module defines a function that returns True if the object is an instance

"""


def is_kind_of_class(obj, a_class):
    """
    checks if object is instance of or if object is instance of inheritance

    Args:
        obj: object to check
        a_class: class to compare against

    Returns:
        True or false.

    """
    return isinstance(obj, a_class)
