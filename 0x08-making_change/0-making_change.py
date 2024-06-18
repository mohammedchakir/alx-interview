#!/usr/bin/python3
"""fucntion making change"""


def makeChange(coins, total):
    """initiate the makechange"""
    if total <= 0:
        return 0

    # Initialize the dp array with a large number (total + 1)
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
