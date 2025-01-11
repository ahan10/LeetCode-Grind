# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l, r = 0, n - 1

        # first we find the pivot of the array, i.e. where it switches from max to min
        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        # we find our min index
        min_index = l

        # in min index is 0, i.e. it was rotated n times and is in exactly the same place that it started; we perform normal binary search
        if min_index == 0:
            l, r = 0, n - 1
        elif target >= nums[0] and target <= nums[min_index - 1]: # else if the target is between the 0th index and the index where max element is; we set bounds accordingly
            l, r = 0, min_index - 1
        else: # else the target lies within the range were min elements are
            l, r = min_index, n - 1

        # perform nirmal binary search on the array between the ranges
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1

# Time: O(log n)
# Space: O(1)