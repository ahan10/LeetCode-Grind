# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):  # make the hashmap with the value of the key as the latest index
            h[nums[i]] = i

        for i in range(len(nums)):  # iterate over the main array again
            y = target - nums[i]  # find the deficit that is, target - current element

            if y in h and h[y] != i:  # if the deficit amount is in the hashmap, and it is not the current index
                return [i, h[y]]  # return the current index and the latest index of the value

# Time: O(n)
# Space: O(n)