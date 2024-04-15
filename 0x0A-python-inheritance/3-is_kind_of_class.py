#!/usr/bin/python3
"""Defines is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of the specified
    class or a instance of a sub-class of a clas ; otherwise False.

    Args:
        obj(object): The object to check.
        a_class(str): The name of the class to check against.

    Returns:
        bool: True if the object is exactly an instance of the
              specified class ; otherwise False.
    """
    return isinstance(obj, a_class)
