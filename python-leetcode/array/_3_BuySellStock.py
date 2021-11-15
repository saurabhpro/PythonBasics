from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # remember i <= j , it means you can sell and buy stock on same day.
        # find the max profit = max(prices[j] - prices[i]) , j >= i
        if len(prices) == 0:
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(price - min_price, max_profit)

        return max_profit
