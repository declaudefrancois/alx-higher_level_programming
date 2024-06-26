#!/usr/bin/python3

"""Square module."""


class Square:
    """This class represents a geometrical square.

    The square is a quadrilateral figure with each side equal to each others.

    Attributes:
        size (int): The size of the square, a positive int.
    """

    def __init__(self, size=0):
        """This method instanciates a new Square.
        Args:
            size (int): The size of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
