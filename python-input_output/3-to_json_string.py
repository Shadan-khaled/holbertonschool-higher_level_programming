#!/usr/bin/python3
"""
This module provides a function that returns the JSON
representation of a Python object.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: Python object to serialize

    Returns:
        str: JSON representation of the object
    """
    return json.dumps(my_obj)
