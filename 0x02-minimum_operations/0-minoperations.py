#!/usr/bin/python3
"""
Calculate the fewest number of operations needed to result in
 exactly n H characters in the file
"""


def minOperations(n):
    """A method that calculates the fewest number of operations needed
      to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)

    return n


if __name__ == "__main__":
    n = 4
    print("operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print(" operations to reach {} char: {}".format(n, minOperations(n)))
