# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/description/

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        result = []
        # since the array is sorted, the biggest values will be on the edges
        while left <= right: #iterating with two pointers
            if abs(nums[left]) > abs(nums[right]): #if the absolute value of the left nums is bigger than that of right, square and append left to the array and move right
                result.append(nums[left]**2)
                left += 1
            else: #else if the right is bigger than left or equal, square the right one and move the pointer to left
                result.append(nums[right]**2)
                right -= 1

        result.reverse() #reverse the array at the end since we build in reverse order

        return result
# Time: O(n)
# Space: O(n)