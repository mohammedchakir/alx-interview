#!/usr/bin/python3
"""fucntion making change"""

from collections import deque


def makeChange(coins, total):
    """initiate the makechange"""
    if total <= 0:
        return 0

    # Initialize the queue with the starting point
    # (total) and the number of coins used (0)
    queue = deque([(0, 0)])
    visited = set([0])

    while queue:
        current_total, num_coins = queue.popleft()

        for coin in coins:
            new_total = current_total + coin
            if new_total == total:
                return num_coins + 1
            if new_total > total:
                continue
            if new_total not in visited:
                visited.add(new_total)
                queue.append((new_total, num_coins + 1))

    return -1
