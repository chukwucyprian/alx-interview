#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount tota
    """
    if total <= 0:
        return 0

    # Initialize table to store minimum coins required for each total amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for total amount 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


# Testing the function
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))   # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))   # Output: -1
