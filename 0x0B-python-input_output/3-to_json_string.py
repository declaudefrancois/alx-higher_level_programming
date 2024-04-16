#!/usr/bin/python3
"""Defines the to_json_string function.
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of
    an object (string).

    Args:
        my_obj (object): An object.

    Returns:
        str: The JSON representation of my_obj.
    """
    return json.dumps(my_obj)
