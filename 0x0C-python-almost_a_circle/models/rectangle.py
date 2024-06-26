#!/usr/bin/python3
"""Defines the rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """Represents a closed 2-D shape, having 4 sides
    4 corners, and 4 right angles (90°).

    Attributes:
        __width (int): The width.
        __height (int): The height.
        __x (int): The x coordinate of the rectangle in a 2D plan.
        __y (int): The y coordinate of the rectangle in a 2D plan.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Creates a new Rectangle.

        Args:
            width (int): The width.
            height (int): The height.
            x (int): X coordinate.
            y (int): y coordinate.
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Computes and returns the area of the
        rectangle instance.

        Returns:
            int: The area value.
        """
        return self.width * self.height

    def display(self):
        """Displays a Rectangle using #
        symbol as unit. (# = 1)
        """
        text = "\n" * self.y
        rows = ["#" * self.width for i in range(self.height)]
        rows = [(" " * self.x) + s for s in rows]
        text += "\n".join(rows)
        print(text)

    def update(self, *args, **kwarg):
        """Assigns an argument to each attribute.
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute

        Args:
            args (list(int)): "no-keyword" variable argument list.
            kwarg (dict): 'keyword' or named arguments.
        """
        if args is not None and len(args) > 0:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.width = v
                elif i == 2:
                    self.height = v
                elif i == 3:
                    self.x = v
                elif i == 4:
                    self.y = v
            return

        if kwarg is None:
            return

        for k, v in kwarg.items():
            setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle.

        Returns:
            dict: The dictionary representations of the rectangle.
        """
        return dict(self)

    def __iter__(self):
        """Allows to iterate the attributes of a Rectangle.
        """
        for k in ["id", "width", "height", "x", "y"]:
            yield (k, getattr(self, k))

    @property
    def width(self):
        """Gets the Rectangle's width.

        Returns:
            int: The width.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the Rectangle's width.
        Args:
            width (int): The width value.
        """
        if type(width) is not int:
            self._must_be_int("width")
        if width <= 0:
            self._must_be_gt_0("width")

        self.__width = width

    @property
    def height(self):
        """Gets the Rectangle's height.

        Returns;
            int: The rectangle's height.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the Rectangle's height.

        Args:
            height (int): The height value.
        """
        if type(height) is not int:
            self._must_be_int("height")
        if height <= 0:
            self._must_be_gt_0("height")

        self.__height = height

    @property
    def x(self):
        """Gets the Rectangle's x coordinate.

        Returns:
            int: The rectangle's x coordinate.
        """
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the Rectangle's x coordinate.

        Args:
            x (int): The x coordinate value.
        """
        if type(x) is not int:
            self._must_be_int("x")
        if x < 0:
            self._must_be_gte_0("x")

        self.__x = x

    @property
    def y(self):
        """Gets the Rectangle's y coordinate.

        Returns:
            int: The rectangle's y coordinate.
        """
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the Rectangle's y coordinate.

        Args:
            y (int): The y coordinate value.
        """
        if type(y) is not int:
            self._must_be_int("y")
        if y < 0:
            self._must_be_gte_0("y")

        self.__y = y

    def _must_be_int(self, name):
        """Throws a TypeError with the string
        `<name> must be an integer.`

        Args:
            name (str) : The name of the attribute.
        """
        raise TypeError("{} must be an integer".format(name))

    def _must_be_gte_0(self, name):
        """Throws a ValueError formated with the string
        `<name> must be >= 0`

        Args:
            name (str) : The name of the attribute.
        """
        raise ValueError("{} must be >= 0".format(name))

    def _must_be_gt_0(self, name):
        """Throws a ValueError formated with the string.
        `<name> must be > 0`

        Args:
            name (str) : The name of the attribute.
        """
        raise ValueError("{} must be > 0".format(name))

    def __str__(self):
        """Returns the human readable representation
        of a rectangle.
        """
        fmt = "[{}] ({}) {}/{} - {}/{}"
        return fmt.format(self.__class__.__name__, self.id, self.x,
                          self.y, self.width, self.height)
