# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf') # min price to be very large
        max_profit = 0 # max profit is 0 initially

        for price in prices:
            if price < min_price: # if the current price is less than the min price that we encountered till now, we use this as the new min price
                min_price = price

            profit = price - min_price # profit is the current price - hte min price we encountered till now

            if profit > max_profit: # if the new profit is greater than the profit we had till now, we use the new profit
                max_profit = profit

        return max_profit # return the max profit we found

# Time: O(n)
# Space: O(1)