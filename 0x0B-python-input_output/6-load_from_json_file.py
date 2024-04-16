#!/usr/bin/python3
"""Defines the load_from_json_file.
"""
import json


def load_from_json_file(filename):
    """Load an object from the file json content.

    Args:
        filename (str): The path to the file.
    """
    with open(filename, "r") as f:
        return json.loads(f.read())
