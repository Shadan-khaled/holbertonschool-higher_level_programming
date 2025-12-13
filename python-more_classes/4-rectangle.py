#!/usr/bin/python3
"""Rectangle with eval support."""
class Rectangle( __import__('3-rectangle').Rectangle):
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
