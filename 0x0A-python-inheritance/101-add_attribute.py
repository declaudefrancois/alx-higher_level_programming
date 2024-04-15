#!/usr/bin/python3
"""Defines add_attribute function.
"""


def add_attribute(obj, name, value):
    """Adds a new attribute to the given obj.

    Args:
        obj (object): An objet.
        name (str): The new attribute name.
        value (object): The value of the attribute.

    Raises:
        TypeError: If if the object can’t have new attribute.
    """
    try:
        setattr(obj, name, value)
    except (AttributeError, TypeError):
        raise TypeError("can't add new attribute")
