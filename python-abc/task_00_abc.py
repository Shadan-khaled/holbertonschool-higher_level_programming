#!/usr/bin/python3
"""
task_00_abc.py
Defines an abstract class Animal with an abstract method sound,
and its subclasses Dog and Cat implementing the sound method.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an Animal.
    All subclasses must implement the sound() method.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses.
        Should return the sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Dog class inheriting from Animal.
    Implements the sound method to return 'Bark'.
    """

    def sound(self):
        """
        Returns the sound of a Dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class inheriting from Animal.
    Implements the sound method to return 'Meow'.
    """

    def sound(self):
        """
        Returns the sound of a Cat.
        """
        return "Meow"
