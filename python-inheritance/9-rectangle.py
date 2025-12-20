#!/usr/bin/python3
"""
9-rectangle.py
Defines a Rectangle class that inherits from BaseGeometry with:
- width and height private and validated
- area() method implemented
- custom __str__ method
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inheriting from BaseGeometry.
    Width and height are private attributes validated by integer_validator.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with width and height.

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle

        Raises:
            TypeError: if width or height are not integers
            ValueError: if width or height <= 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle:
        [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
