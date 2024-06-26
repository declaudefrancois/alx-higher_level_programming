#!/usr/bin/python3

"""Square module."""


class Square:
    """This class represents a geometrical square.

    The square is a quadrilateral figure with each side equal to each others.

    Attributes:
        size (int|float): The size of the square, a positive int.

    """

    def __init__(self, size=0):
        """This method instanciates a new Square.

        Args:
            size (int|float): The size of the square.
        """
        self.__check_size_value(size)
        self.__size = size

    def __eq__(self, other):
        """Magic method to use for == or != comparison between two square."""
        return (self.__size == other.__size)

    def __gt__(self, other):
        """Magic method to use for > comparison between two square."""
        return (self.__size > other.__size)

    def __ge__(self, other):
        """Magic method to use for >= comparison between two square."""
        return (self.__size >= other.__size)

    def __le__(self, other):
        """Magic method to use for <= comparison between two square."""
        return (self.__size <= other.__size)

    def __lt__(self, other):
        """Magic method to use for < comparison between two square."""
        return (self.__size < other.__size)

    def __check_size_value(self, size):
        """Checks if a value cannot be used as squre size.

        If the value is compliant, continues otherwise raises an exception.
        Raise a TypeError if value is not int or float.
        Raise a ValueError if value is less than 0.
        """
        if not isinstance(size, int) and not isinstance(size, float):
            raise TypeError("size must be a number")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of the square and returns the result.

        Returns:
            The result of size times size.
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """Size property getter.

        Returns:
            The value of the square size (int or float).
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square instance.

        Raise an exception if the new value is not int or is less than 0,
        otherwise sets the new value of the square size.

        Args:
            value (int|float): The new value of the square size to set.
        """
        self.__check_size_value(value)
        self.__size = value
