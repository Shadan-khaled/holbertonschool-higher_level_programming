#!/usr/bin/python3
"""
2-is_same_class.py
Defines a function that checks if an object is exactly an instance
of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class,
    otherwise False.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare with.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
