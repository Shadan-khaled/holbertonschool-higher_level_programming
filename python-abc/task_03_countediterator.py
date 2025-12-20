#!/usr/bin/python3
"""
task_03_countediterator.py
Defines a CountedIterator class that wraps any iterable
and keeps track of the number of items iterated over.
"""


class CountedIterator:
    """
    Iterator class that counts how many items have been iterated.
    """

    def __init__(self, iterable):
        """
        Initialize with the given iterable and set counter to 0.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.
        Raises StopIteration when the iterator is exhausted.
        """
        item = next(self.iterator)  # May raise StopIteration naturally
        self.count += 1
        return item

    def get_count(self):
        """
        Return the number of items iterated over so far.
        """
        return self.count

    def __iter__(self):
        """
        Iterator object must return itself as per Python protocol.
        """
        return self
