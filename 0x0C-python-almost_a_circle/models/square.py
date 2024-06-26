#!/usr/bin/python3
"""Contains the Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A rectangle with each side equals to each other.
    Inherits Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates a new Square object.

        Args:
            size (int): The length of a side.
            x (int): horizontal coordinate in a 2d plan.
            y (int): vertical coordinate in a 2d plan.
            id (int): The id of the object.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        fmt = "[{}] ({}) {}/{} - {}"
        return fmt.format(self.__class__.__name__, self.id, self.x,
                          self.y, self.width)

    @property
    def size(self):
        """Square's size getter.
        """
        return self.width

    @size.setter
    def size(self, size):
        """Square's size setter.

        Args:
            size (int): The Square's side lenght.
        """
        if type(size) is not int:
            self._must_be_int("width")
        if size <= 0:
            self._must_be_gt_0("width")

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Assigns attribute of a Square.

        Args:
            args: List of positional (no-keyword) args.
            kwargs: Keyword arguments.
        """
        if args is not None and len(args) > 0:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.size = v
                elif i == 2:
                    self.x = v
                elif i == 3:
                    self.y = v
            return

        if kwargs is None:
            return

        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation
        of a Square.
        """
        return super().to_dictionary()

    def __iter__(self):
        """Allows to iterate attributes of a
        square.
        """
        for k in ['id', 'size', 'x', 'y']:
            yield (k, getattr(self, k))
