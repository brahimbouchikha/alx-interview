#!/usr/bin/python3
"""
Optimized function to determine the fewest number of coins needed to meet a
given amount using a dynamic programming approach with greedy optimization.
"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet the total amount.

    Args:
        coins (list): A list of integers representing the available coin
        denominations.
        total (int): The total amount of money that needs to be made.

    Returns:
        int: The fewest number of coins needed to make the total.
             - Returns 0 if the total is 0 or less.
             - Returns -1 if it is not possible to make the total with the
             given coins.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
            if dp[i] != float('inf') and i == total:
                return dp[total]

    return dp[total] if dp[total] != float('inf') else -1