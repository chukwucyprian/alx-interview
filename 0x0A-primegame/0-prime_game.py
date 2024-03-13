#!/usr/bin/python3
"""A Prime Game Python Code"""


def isWinner(x, nums):
    """
    Determine the winner of a prime game for multiple rounds.

    Args:
        x (int): The number of rounds to play.
        nums (list):An array of integers for the upper bounds of each round.

    Returns:
        str or None: The name of the player that won the most rounds.
        If the winner cannot be determined, return None.
    """

    def is_prime(num):
        """
        Check if a number is prime.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        """
        Generate a list of prime numbers up to a given limit.

        Args:
            n (int): The upper bound for generating prime numbers.

        Returns:
            list: A list of prime numbers up to the given limit.
        """
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    # Dictionary to store the count of wins for each player
    winners = {"Maria": 0, "Ben": 0}

    # Iterate through each round
    for n in nums:
        primes = get_primes(n)  # Get prime numbers for the current round
        if len(primes) % 2 == 0:  # If the number of primes is even, Ben wins
            winners["Ben"] += 1
        else:  # Otherwise, Maria wins
            winners["Maria"] += 1

    # Determine the overall winner
    if winners["Maria"] == winners["Ben"]:
        return None
    elif winners["Maria"] > winners["Ben"]:
        return "Maria"
    else:
        return "Ben"
