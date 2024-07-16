#!/usr/bin/python3
"""Prime Game."""


def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_prime_list(n):
    """Generate a list of prime numbers up to n."""
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def count_primes_in_range(n):
    """Count the number of prime numbers up to n."""
    primes = generate_prime_list(n)
    return len(primes)


def isWinner(x, nums):
    """Determine the winner of each game."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = count_primes_in_range(n)
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    x = 5
    nums = [2, 5, 1, 4, 3]
    print("Winner: {}".format(isWinner(x, nums)))
