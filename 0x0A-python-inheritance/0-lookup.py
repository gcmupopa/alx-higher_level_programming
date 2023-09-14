#!/usr/bin/python3

"""
This module defines a function that returns the list of available attributes

"""


def lookup(obj):
    """
    function that returns the list of available attributes and methods.

    Args:
        obj: object to lookup


    Returns:
        list of strings represnting names of methods and attributes
    """

    atme = []
    for am in dir(obj):
        atme.append(am)
    return atme
