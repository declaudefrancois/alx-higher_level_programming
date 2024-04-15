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
        print(sorted(self))
