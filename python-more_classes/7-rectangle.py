#!/usr/bin/python3
"""Rectangle with print symbol."""
class Rectangle( __import__('6-rectangle').Rectangle):
    print_symbol = "#"
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol)*self.width for _ in range(self.height)])
