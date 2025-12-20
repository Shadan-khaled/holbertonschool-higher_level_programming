#!/usr/bin/python3
"""
task_01_duck_typing.py
Defines an abstract class Shape with abstract methods area and perimeter,
and concrete classes Circle and Rectangle implementing these methods.
Includes shape_info function using duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    All subclasses must implement area() and perimeter() methods.
    """

    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle shape class inheriting from Shape.
    """

    def __init__(self, radius):
        """
        Initialize Circle with radius.
        """
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle.
        """
        return math.pi * (self.radius**2)

    def perimeter(self):
        """
        Returns the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape class inheriting from Shape.
    """

    def __init__(self, width, height):
        """
        Initialize Rectangle with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape object using duck typing.
    Assumes the object implements area() and perimeter().
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
