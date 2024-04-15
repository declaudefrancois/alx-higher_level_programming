#!/usr/bin/python3
"""Defines the square class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square.
    """

    def __init__(self, size):
        """Instantiates a new square.

        Args:
            size (int): The size of one edge.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size <= 0.
        """
        self.integer_validator('size', size)
        self._size = size
        super().__init__(size, size)

    def area(self):
        """Calculates the square's area.

        Returns:
            int: The area value.
        """
        return self._size ** 2
