# LC 2239. Find Closest Number to Zero
# https://leetcode.com/problems/find-closest-number-to-zero/
from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0] # initially assume the first number is closest

        for i in nums: #iterate through all the indices
            if abs(i) < abs(closest): # compare the absolute value of it to the absolute value of teh current closest and keep the closest value
                closest = i

        if closest < 0 and abs(closest) in nums: # if the current closest is negative and its positive version exists, return the positive version else return the negative one
            return abs(closest)
        return closest

    # Time = O(n)
    # Space = O(1)