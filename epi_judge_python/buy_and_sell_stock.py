from typing import List

from test_framework import generic_test


# for every day check all the following days
# time: O(n^2)
# space: O(1)
"""
def buy_and_sell_stock_once(prices: List[float]) -> float:
    max_profit = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit
"""

# divide and conquer
# time: O(n log n), because T(n) = 2T(n/2) + O(n)
# space: O(1)
"""
def find_max_profit(prices: List[float], i: int, j: int):
    if j - i < 2:
        return max(0, prices[j] - prices[i]), min(prices[i:j+1]), max(prices[i:j+1])
    mid = (i + j) // 2
    l_max_profit, l_min, l_max = find_max_profit(prices, i, mid)
    r_max_profit, r_min, r_max = find_max_profit(prices, mid + 1, j)
    max_profit = max(l_max_profit, r_max_profit, r_max - l_min)
    return max_profit, min(l_min, r_min), max(l_max, r_max)

def buy_and_sell_stock_once(prices: List[float]) -> float:
    max_profit, _, _ = find_max_profit(prices, 0, len(prices) - 1)
    return max_profit
"""

# compare current price with min price so far
# time: O(n)
# space: O(1)
def buy_and_sell_stock_once(prices: List[float]) -> float:
    max_profit = 0
    min_price = float('inf')
    for i in range(len(prices)):
        max_profit = max(max_profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])
    return max_profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
