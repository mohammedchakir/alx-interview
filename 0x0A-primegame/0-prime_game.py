#!/usr/bin/python3
"""Prime Game."""


def sieve(n):
    """Returns a list of prime numbers up to n."""
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def isWinner(x, nums):
    """Determine the winner of each game and return the overall winner."""
    if x < 1 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = sieve(n)
        if not primes:
            ben_wins += 1
            continue

        move_count = 0
        while primes:
            smallest_prime = primes[0]
            primes = [num for num in primes if num % smallest_prime != 0]
            move_count += 1

        if move_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
