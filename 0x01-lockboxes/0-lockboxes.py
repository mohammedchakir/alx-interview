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
    opened_boxes = {0}
    keys = set(boxes[0])
    visited = set()
    while keys:
        key = keys.pop()

        if key not in visited:
            opened_boxes.add(key)
            visited.add(key)
            keys.update(boxes[key])

    return len(opened_boxes) == len(boxes)
