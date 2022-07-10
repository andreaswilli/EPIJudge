from typing import List

from test_framework import generic_test

# find max for all possible slices of the list
# time: O(n^2)
# space: O(1)
"""
def buy_and_sell_stock_twice(prices: List[float]) -> float:
    max_profit = 0
    for i in range(1, len(prices)):
        profit = find_max_profit(prices, 0, i) + find_max_profit(prices, i + 1, len(prices) - 1)
        max_profit = max(max_profit, profit)
    return max_profit

# helper (buy and sell once)
def find_max_profit(prices, i, j) -> float:
    max_profit = 0
    min_price = float('inf')
    for price in prices[i:j+1]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return max_profit
"""


# save max profit for each position
# time: O(n)
# space: O(n)
def buy_and_sell_stock_twice(prices: List[float]) -> float:
    profits = [-1.0] * len(prices)
    max_profit = 0
    min_price = float('inf')
    for i in range(len(prices)):
        max_profit = max(max_profit, prices[i] - min_price)
        profits[i] = max_profit
        min_price = min(min_price, prices[i])
    profits.insert(0, 0)
    max_price = float('-inf')
    for i in reversed(range(len(prices))):
        max_profit = max(max_profit, max_price - prices[i] + profits[i])
        max_price = max(max_price, prices[i])
    return max_profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
