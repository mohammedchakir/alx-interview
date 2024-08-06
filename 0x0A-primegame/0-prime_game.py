#!/usr/bin/python3
""" Module for solving prime game question """


def sieve(n):
    """
    Returns an array where index indicates if the number
    is prime (True) or not (False)
    """
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    return is_prime


def prime_count_up_to(n, is_prime):
    """
    Returns an array where index contains the count of prime
    numbers up to that index
    """
    prime_count = [0] * (n + 1)
    count = 0
    for i in range(n + 1):
        if is_prime[i]:
            count += 1
        prime_count[i] = count
    return prime_count


def isWinner(x, nums):
    """function that checks for the winner"""
    if not nums or x < 1:
        return None

    max_num = max(nums)
    is_prime = sieve(max_num)
    prime_count = prime_count_up_to(max_num, is_prime)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
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
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
