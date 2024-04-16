#!/usr/bin/python3
"""Defines save_to_json_file function.
"""
import json


def save_to_json_file(my_obj, filename):
    """Save the json represention of the given
    object to file whose name is passed as argument.

    Args:
        my_obj (object): The object to save.
        finename (str): The filename to save the object into.
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
