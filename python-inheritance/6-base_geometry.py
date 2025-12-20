#!/usr/bin/python3
"""
6-base_geometry.py
Defines a class BaseGeometry with an area() method
that raises an exception because it is not implemented.
"""


class BaseGeometry:
    """
    A class representing base geometry with an area method.
    """

    def area(self):
        """
        Raises an Exception indicating that area() is not implemented.
        """
        raise Exception("area() is not implemented")
