#!/usr/bin/python3
"""
Pickling custom Python objects:
Defines a CustomObject class with serialize and deserialize methods.
"""

import pickle


class CustomObject:
    """
    Custom object with name, age, is_student attributes
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print object attributes in a formatted way
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.
        Returns True if successful, None if error occurs.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            return True
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a file and return an instance of CustomObject.
        Returns None if file is missing or corrupted.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj
        except Exception:
            return None
