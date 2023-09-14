#!/usr/bin/python3

"""
This module defines function returns True if object is an instance of a class

"""


def is_same_class(obj, a_class):
    """
    checks if object is exactly instance of specified class.

    Args:
        objs: object to check.
        a_class: class to compare against

    Returns:
        True or false.

    """

    return type(obj) is a_class
