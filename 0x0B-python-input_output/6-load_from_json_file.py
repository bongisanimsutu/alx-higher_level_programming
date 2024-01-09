#!/usr/bin/python3
"""Defines a function for reading a JSON file and creating a Python object."""
import json


def load_from_json_file(filename):
    """Reads a JSON file and returns the corresponding Python object.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        The Python object created from the contents of the JSON file.
    """
    with open(filename) as file:
        return json.load(file)

