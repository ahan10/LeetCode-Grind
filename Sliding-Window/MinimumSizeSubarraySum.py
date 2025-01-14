# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_length = float('inf') # initialize it to inf since we need a minimum value
        n = len(nums)
        summ = 0 # the sum of the window

        l = 0

        # we will iterate over right till the sum in the window is < target; once the sum is more than or equal to the target,
        # we shrink the window by bringing in the left pointer towards right pointer

        for r in range(n):
            summ += nums[r] # we calculate the sum by adding the right index since we are building up out window there

            while summ >= target: # while the sum >= target, we have a valid window, we will get the minimum and shrink it till the window becomes invalid
                min_length = min(min_length, r - l + 1)
                summ -= nums[l]
                l += 1

        if min_length == float('inf'): # if the length is infinity, we know that we did not find hte window size; return 0
            return 0

        return min_length