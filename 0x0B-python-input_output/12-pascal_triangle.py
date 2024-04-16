#!/usr/bin/python3
"""Define pascal_triangle function.
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal’s triangle of n.

    Args:
        n (int): The index of the suite.
    """
    if n <= 0:
        return []

    n_list = []
    for i in range(n):
        for j in range(i + 1):
            if j == 0:
                n_list.append([1])
            elif j == i:
                n_list[i].append(1)
            else:
                n_list[i].append(n_list[i - 1][j - 1] + n_list[i - 1][j])
    return n_list
