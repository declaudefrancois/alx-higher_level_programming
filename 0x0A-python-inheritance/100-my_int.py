#!/usr/bin/python3
"""Defines a custom int class (MyInt)
"""


class MyInt(int):
    """Custom int class.
    """

    def __eq__(self, other):
        """Magic method called for == operator.

        Args:
            other (int): The other side of comparison.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Magic method called for != operator.

        Args:
            other (int): The other side of the comparison.
        """
        return isinstance(other, int) and super().__eq__(other)
