#!/usr/bin/python3
"""Defines a function for converting a Python object to a JSON string."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a given Python object.

    Args:
        my_obj: The Python object to be converted to a JSON string.

    Returns:
        str: The JSON representation of the input object.
    """
    return json.dumps(my_obj)

