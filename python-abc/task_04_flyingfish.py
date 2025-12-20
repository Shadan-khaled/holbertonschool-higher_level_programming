#!/usr/bin/python3
"""
task_04_flyingfish.py
Demonstrates multiple inheritance with Fish and Bird classes
by creating a FlyingFish class that inherits from both.
"""


class Fish:
    """A simple Fish class with swim and habitat methods."""

    def swim(self):
        """Prints a message indicating that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the natural habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """A simple Bird class with fly and habitat methods."""

    def fly(self):
        """Prints a message indicating that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Prints the natural habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A FlyingFish inherits from both Fish and Bird."""

    def swim(self):
        """Override Fish.swim to specify FlyingFish behavior."""
        print("The flying fish is swimming!")

    def fly(self):
        """Override Bird.fly to specify FlyingFish behavior."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override habitat to show FlyingFish lives in both environments."""
        print("The flying fish lives both in water and the sky!")
