# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        lo, hi = 0, len(numbers) - 1 # pointers to left and right

        while hi > lo:
            summ = numbers[hi] + numbers[lo] # sum of the elements at the two pointers

            if summ == target: # if the sum == target, then return both the pointers and +1 since for the answer the index doesn't begin at 0
                return [lo + 1, hi + 1]
            elif summ > target: # since the array is sorted, if the summ is too big, we move left, making it small
                hi -= 1
            else: # since the array is sorted, if the summ is too small, we move right, making it big
                lo += 1

    # Time: O(n)
    # Space: O(1)