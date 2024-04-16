#!/usr/bin/python3
"""Defines the from_json_string function.
"""
import json


def from_json_string(my_str):
    """Returns a python object from the JSON string
    my_str.

    Args:
        my_str (str): A json string.

    Returns:
        object: The object.
    """
    return json.loads(my_str)
