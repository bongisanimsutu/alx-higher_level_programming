#!/usr/bin/python3
"""
file: 10-class_to_json.py
functions:
-> class_to_json
"""


def class_to_json(obj):
    """Returns a dictionary representation with simple data structure.

    Args:
        obj: The object for which the dictionary representation is generated.

    Returns:
        dict: The dictionary representation of the object's attributes.
    """
    structure = {}
    if hasattr(obj, "__dict__"):
        structure = obj.__dict__.copy()
    return structure

