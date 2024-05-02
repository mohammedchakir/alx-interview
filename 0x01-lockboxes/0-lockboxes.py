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
    total_boxes = len(boxes)
    setofkeys = [0]
    counter = 0
    index = 0

    while index < len(setofkeys):
        setkey = setofkeys[index]
        for key in boxes[setkey]:
            if 0 < key < total_boxes and key not in setofkeys:
                setofkeys.append(key)
                counter += 1
        index += 1

    return counter == total_boxes - 1