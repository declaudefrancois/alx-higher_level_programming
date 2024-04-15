#!/usr/bin/python3
"""Defines inherits_from function.
"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.

    Args:
        obj(object): The object to check.
        a_class(str): The name of the class to check against.

    Returns:
        bool: True if the object is exactly an instance of the
              specified class ; otherwise False.
    """
    return (obj.__class__.__name__ != a_class.__name__ and
            issubclass(obj.__class__, a_class))
