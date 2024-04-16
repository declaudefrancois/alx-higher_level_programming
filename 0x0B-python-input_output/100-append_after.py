#!/usr/bin/python3
"""Defines the append_after function.
"""


def append_after(filename="", search_string="", new_string=""):
    """nserts a line of text to a file, after each line
    containing the specified string.

    Args:
        filename (str): The file path.
        search_string (str): The string to check.
        new_string (str): The string to add.
    """
    lines = []
    with open(filename, "r") as f:
        for line in f.readlines():
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, "w") as f:
        f.write("".join(lines))
