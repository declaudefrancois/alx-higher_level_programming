#!/usr/bin/python3
"""Define the rectangle class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle.
    """

    def __init__(self, width, height):
        """Instantiates a new rectangle.

        Args:
            width (int): The width.
            height (int): The height.

        Raises:
            TypeError: If width or height is not integer.
            ValueError: If width or height is less than 0.
        """
        self.integer_validator('width', width)
        self._width = width

        self.integer_validator('height', height)
        self._height = height
