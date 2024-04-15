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
            width(int): The width.
            height(int): The height.
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self._width = width
        self._height = height

    def area(self):
        """Calculates the rectangle's area.

        Returns:
            int: The area value.
        """
        return self._width * self._height

    def __str__(self):
        """Returns a human readable string
        representing the rectangle.

        Returns:
            str: The string representation.
        """
        return "[Rectangle] {}/{}".format(self._width, self._height)
