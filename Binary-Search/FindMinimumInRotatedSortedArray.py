# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# we perform binary search to find the pivot point of the array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums) # length of array
        l, r = 0, n - 1 # pointers at first and last

        while l < r: # while the arrays do not overlap
            m = (l + r) // 2 # find the middle index

            if nums[m] > nums[r]: # if number at middle is greater than that of number at right, means that the minimum lies in between middle and right
                l = m + 1
            else: # else the minimum lies between left and middle
                r = m
        # at the end l = r so doesn't matter
        return nums[l]

# Time: O(log n)
# Space: O(1)