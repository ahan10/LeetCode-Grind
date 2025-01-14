# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        lo = prices[0]
        hi = prices[0]
        profit = 0
        n = len(prices)

        while i < n - 1: # n-1 since we check the next index
            # where to buy
            while i < n - 1 and prices[i] >= prices[i + 1]: # we want to find where the price switches from high to low, and does not become lower, that becomes buying point
                i += 1
            lo = prices[i]

            # where to sell
            while i < n - 1 and prices[i] <= prices[i + 1]: # we want to find where the price switches from low to high, and does not become higher, that becomes selling point
                i += 1
            hi = prices[i]
            profit += hi - lo

        return profit