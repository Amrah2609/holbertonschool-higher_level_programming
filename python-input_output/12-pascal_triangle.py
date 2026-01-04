#!/usr/bin/python3
"""Pascal's Triangle function."""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # first row

    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]  # first element
        # compute middle elements
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # last element
        triangle.append(row)

    return triangle
