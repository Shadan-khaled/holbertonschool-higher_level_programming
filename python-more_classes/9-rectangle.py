#!/usr/bin/python3
"""Rectangle with square class method."""
class Rectangle( __import__('8-rectangle').Rectangle):
    @classmethod
    def square(cls, size=0):
        return cls(size, size)
