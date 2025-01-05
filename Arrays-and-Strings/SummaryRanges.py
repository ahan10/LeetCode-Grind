# 228. Summary Ranges
# https://leetcode.com/problems/summary-ranges/description/
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []

        i = 0
        while i < len(nums):
            start = nums[i] # the starting index for the range to validate is the current one

            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]: # while i is not the last element, and the next number is sequentially after the current one
                i += 1 # we iterate i, till we satisfy the above condition

            if start != nums[i]: # if we have moved ahead form the current element, that means we have a range, so we add the range in the range notation
                ans.append(str(start) + '->' + str(nums[i]))
            else: # else, we did not have a range, and we only add the single digit
                ans.append(str(nums[i]))

            i += 1 # move the index ahead as we has found till the i-1th index

        return ans

# Time: O(n)
# Space: O(n)