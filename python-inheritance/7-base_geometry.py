#!/usr/bin/python3
"""
7-base_geometry.py
Defines a class BaseGeometry with:
- area() method raising an exception
- integer_validator() method to validate integers
"""


class BaseGeometry:
    """
    A class representing base geometry with area() and integer_validator() methods.
    """

    def area(self):
        """
        Raises an Exception indicating that area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0.

        Args:
            name (str): Name of the parameter (used in error messages)
            value (any): Value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
