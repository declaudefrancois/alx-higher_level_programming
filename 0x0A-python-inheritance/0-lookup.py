#!/usr/bin/ptyhon3
"""
Defines the lookup function module
to list of available attributes and methods of an object.
"""


def lookup(obj):
    """Returns the list of available attributes
    and methods of an object.

    Args:
        obj: An object of any type.

    return:
        list: Returns the list of attributes and methods in obj.
    """
    return dir(obj)
