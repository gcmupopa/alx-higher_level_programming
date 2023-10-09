#!/usr/bin/python3

"""
This module defines a class MyList that inherits from list
"""


class MyList(list):
    """
    subclass of list providing extra functionality

    This class inherits from built-in list class and add method to print sort
    """

    def print_sorted(self):
        """
        prints list in sorted (ascending order)

        This method sorts list ascending and prints it.

        """

        sortlist = sorted(self)
        print(sortlist)
