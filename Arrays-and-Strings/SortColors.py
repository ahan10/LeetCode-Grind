# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/description/
# We implement a count sort

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3

        for num in nums: # build our count array
            count[num] += 1

        for i in range(len(nums)): # iterate and replace the numbers
            if count[0] != 0:
                nums[i] = 0
                count[0] -= 1
            elif count[1] != 0:
                nums[i] = 1
                count[1] -= 1
            elif count[2] != 0:
                nums[i] = 2
                count[2] -= 1

# Time: O(n) {O(n+k)[k = number of elements to be counted]; Since we have only 3 counts; O(n+3) = O(n)}
# Space: O(1)

# Intuitive:
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]

        for color in nums:
            counts[color] += 1

        R, W, B = counts

        nums[:R] = [0] * R
        nums[R:R + W] = [1] * W
        nums[R + W:] = [2] * B