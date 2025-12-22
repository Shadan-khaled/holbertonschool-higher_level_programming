#!/usr/bin/python3
"""
This module contains a function that generates Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n.

    Args:
        n (int): number of rows

    Returns:
        list: list of lists representing Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            for j in range(1, len(last_row)):
                row.append(last_row[j - 1] + last_row[j])
            row.append(1)
        triangle.append(row)

    return triangle
