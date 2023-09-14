#!/usr/bin/python3

"""
This module defines function that adds a new attribute to an object

"""


def add_attribute(obj, atname, atval):
    """
    adds new attribute to object if possible.

    Args:
        obj (object): object to add attribute to.
        atname (str): name of attribute.
        atval (any): value of attribute.

    Raises:
        TypeError: if object cannot have new attribute.


    Returns:
        None.
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("cannot add new attribute")

    setattr(obj, atname, atval)
