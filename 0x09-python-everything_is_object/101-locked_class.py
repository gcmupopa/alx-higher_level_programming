#!/usr/bin/python3

"""
This is a module that defines LockedClass.
"""


class LockedClass:
    """
    LockedClass is a class that prevents user from dynamically creating new instance attributes, except for 'first_name' attribute.
    """

    __slots__ = ['first_name']

    def __seattr__(self, name, value):
        """
        Overrides default behaviour of attribute assignment, only allows setting firstname attribute.
        Raises an attribute error for any other attribute assignment.
        """
        if name != 'first_name':
            raise AttributeError("Cannot create new instance attributes")
        self.__dict__[name] = value
