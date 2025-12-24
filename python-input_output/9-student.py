#!/usr/bin/python3
"""
Defines a Student class with public attributes and
a method to return JSON-serializable dictionary.
"""


class Student:
    """
    Student class with first_name, last_name, age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance

        Args:
            first_name (str)
            last_name (str)
            age (int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the Student instance
        """
        return self.__dict__
