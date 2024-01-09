#!/usr/bin/python3
'''
file: 7-save_to_json_file.py
functions:
-> save_to_json_file
'''
import json


def save_to_json_file(my_obj, filename):
    '''Writes the Python object to a text file using JSON representation.

    Args:
        my_obj: The Python object to be saved.
        filename (str): The name of the file to which the object will be saved.
    '''
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)

