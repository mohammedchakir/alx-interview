#!/usr/bin/python3
"""
Defines a method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Returns the fewest number of operations needed to reach n H characters.
    Args:
        n (int): The desired number of H characters.
    Returns:
        int: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations


if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} characters: {}".
          format(n, minOperations(n)))

    n = 12
    print("Min number of operations to reach {} characters: {}".
          format(n, minOperations(n)))
