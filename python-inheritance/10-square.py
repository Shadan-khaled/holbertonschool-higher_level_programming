#!/usr/bin/python3
"""
10-square.py
Defines a Square class that inherits from Rectangle.
The Square class is instantiated with size.
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square class inheriting from Rectangle.
    Size is private and validated by integer_validator.
    """

    def __init__(self, size):
        """
        Initialize a Square with size.

        Args:
            size (int): Size of the square sides

        Raises:
            TypeError: if size is not an integer
            ValueError: if size <= 0
        """
        self.integer_validator("size", size)
        self.__size = size
        # Call Rectangle's __init__ with width and height as size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size * self.__size
