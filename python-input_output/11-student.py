#!/usr/bin/python3
"""
Defines a Student class with public attributes,
methods to return a JSON-serializable dictionary,
and reload the object from a dictionary.
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

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.
        If attrs is a list of strings, only attributes contained
        in this list are retrieved.

        Args:
            attrs (list, optional): list of attribute names to include

        Returns:
            dict: dictionary representation of the Student instance
        """
        if attrs is None:
            return self.__dict__.copy()
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        with the key-value pairs from json.

        Args:
            json (dict): dictionary with attributes to update
        """
        for key, value in json.items():
            setattr(self, key, value)
