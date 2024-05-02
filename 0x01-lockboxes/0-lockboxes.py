#!/usr/bin/python3
"""determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.
    Args:
    - boxes (List[List[int]]): A list of lists representing
    boxes and their keys.
    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    # Initialize a set to keep track of opened boxes
    opened_boxes = {0}

    # Initialize a set to keep track of keys
    keys = set(boxes[0])

    # Initialize a set to keep track of visited boxes
    visited = set()

    # Iterate through keys and boxes
    while keys:
        # Get a key
        key = keys.pop()

        # Check if the key opens a new box
        if key not in visited:
            opened_boxes.add(key)
            visited.add(key)
            keys.update(boxes[key])

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)
