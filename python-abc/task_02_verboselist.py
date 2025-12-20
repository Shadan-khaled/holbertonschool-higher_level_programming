#!/usr/bin/python3
"""
task_02_verboselist.py
Defines a class VerboseList extending Python's list with notifications
for append, extend, remove, and pop operations.
"""


class VerboseList(list):
    """
    List subclass that prints a notification whenever it is modified.
    """

    def append(self, item):
        """
        Append item to the list and print a notification.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend list by iterable and print a notification with number of items.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """
        Remove first occurrence of item from list and print a notification.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Pop item at index (default last) and print a notification.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
