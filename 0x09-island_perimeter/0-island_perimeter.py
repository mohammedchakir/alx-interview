#!/usr/bin/python3
"""
This script contains a function to calculate the perimeter of an island
described in a grid. The grid is a list of list of integers where 0
represents water and 1 represents land. The function follows PEP 8 style
guidelines.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.
    Args:
        grid (list of list of int): The grid representing the island and water.
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
