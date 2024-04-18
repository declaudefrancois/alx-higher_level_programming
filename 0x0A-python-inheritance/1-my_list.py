#!/usr/bin/python3
"""Defines the MyList class.
"""


class MyList(list):
    """Custom list class
    """

    def print_sorted(self):
        """Prints the sorted list in
        ascending order.
        """
        if len(self) == 0:
            return print(self)
        print(sorted(self))
