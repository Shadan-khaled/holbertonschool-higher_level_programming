#!/usr/bin/python3
"""Rectangle with deletion message."""
class Rectangle( __import__('4-rectangle').Rectangle):
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        super().__init__(width, height)
        type(self).number_of_instances += 1
    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
