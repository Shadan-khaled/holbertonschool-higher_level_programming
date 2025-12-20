#!/usr/bin/python3
"""
3-is_kind_of_class.py
Defines a function that checks if an object is an instance of
a specified class or if it inherits from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or of a class
    that inherits from a_class, otherwise False.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare with.

    Returns:
        bool: True if obj is an instance of a_class or inherits from it,
              False otherwise.
    """
    return isinstance(obj, a_class)

