#!/usr/bin/python3
"""Defines the base Geometry class
"""


class BaseGeometry:
    """Parent class of all geometry class.
    """

    def area(self):
        """Calculates the area of the figure.
        """
        raise Exception("area() is not implemented")
