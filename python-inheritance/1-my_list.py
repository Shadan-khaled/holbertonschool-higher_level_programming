#!/usr/bin/python3
"""
1-my_list.py
Defines a class MyList that inherits from list and adds a method
to print the list in ascending sorted order.
"""


class MyList(list):
    """
    A class that inherits from list and adds a method print_sorted.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying
        the original list.
        """
        print(sorted(self))
