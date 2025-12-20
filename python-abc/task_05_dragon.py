#!/usr/bin/python3
"""
task_05_dragon.py
Demonstrates Mixins by creating a Dragon class
that can swim and fly using SwimMixin and FlyMixin.
"""


class SwimMixin:
    """Mixin class to provide swimming capability."""

    def swim(self):
        """Prints a message indicating swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class to provide flying capability."""

    def fly(self):
        """Prints a message indicating flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can both swim and fly using mixins."""

    def roar(self):
        """Prints a message indicating the dragon roars."""
        print("The dragon roars!")
