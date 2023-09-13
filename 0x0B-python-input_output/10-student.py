#!/usr/bin/python3

"""
This is module defines a student by public instance attributes: first_name, last_name, age

"""

class Student:
    """
    Class representing a student

    Attributes:
        first_name (str): first name of the student
        last_name (str): last name of the student
        age (int): age of student

    """
def __init__(self, first_name, last_name, age):
    """
    initialise Student object.
        
    Args:
        first_name (str): first name of student
        last_name (str): last name of student
        age (int): age of student 
    """
    self.first_name = first_name
    self.last_name = last_name
    self.age = age       

    def to_json(self, attrs=None):
        """
        Retrieve dictionary representation of student object

        Args:
            attrs: list of attribute names to retrieve

        Returns:
            dict: dictionary representation of Student object
            
        """


        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
