# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/description/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = set() # make an empty set

        for num in nums: #iterate over the set
            if num in h: # it the current element is already in the set, then it means it is duplicate and return false
                return True
            else: # else add it to the set
                h.add(num)

        return False

# Time: O(n)
# Space: O(n)