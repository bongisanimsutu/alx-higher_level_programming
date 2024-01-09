#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a function for converting a JSON string to a Python object."""
import json


def from_json_string(my_str):
    """Returns the Python object representation of a given JSON string.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        The Python object represented by the JSON string.
    """
    return json.loads(my_str)

