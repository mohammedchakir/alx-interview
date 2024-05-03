#!/usr/bin/env python3
"""
Module to generate Pascal's triangle up to the nth row.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.
    Args:
        n (int): Number of rows in Pascal's triangle.
    Returns:
        list of lists of int: Pascal's triangle up to the nth row.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print the triangle.
        Args:
            triangle (list of lists of int): Pascal's triangle.
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
