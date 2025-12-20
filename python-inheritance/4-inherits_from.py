#!/usr/bin/python3
"""
4-inherits_from.py
Defines a function that checks if an object is an instance of
a class that inherits (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherits
    from a_class, otherwise False.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare with.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
              False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
