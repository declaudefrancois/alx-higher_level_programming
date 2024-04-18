#!/usr/bin/python3
"""Defines the base Geometry class
"""


class BaseGeometry:
    """Parent class of all geometry class.
    """

    def area(self):
        """Calculates the area of the figure.

        Raises:
            Exception: If not implemented by the children.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value to be an integer.

        Args:
            name (str): The attribute name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If width or height is not integer.
            ValueError: If width or height is less than 0.
        """
        if value is None or value.__class__.__name__ != int.__name__:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
