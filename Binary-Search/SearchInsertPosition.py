# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1  # 2 pointers at left and right

        while left <= right:  # until the pointers aren't equal
            middle = (left + right) // 2  # we find the middle index
            if nums[middle] == target:  # if the nums at middle index is the target, return the index, and job is done
                return middle
            elif nums[middle] > target:  # if the nums at middle index is larger than the target, then the number potentially lies between left pointer and middle, so now update the right pointer to just before the middle index
                right = middle - 1
            else:  # if the nums at middle index is smaller than the target, then the number potentially lies between middle pointer and right pointer, so now update the left pointer to just after the middle index
                left = middle + 1

        # if e exited the loop, that means we haven't found it and L and R have cris crossed and middle index is near the place where it should be found
        if nums[middle] < target: # target is larger than the nums at middle index, so it should appear after
            return middle + 1
        else: # else, it is less than the nums at middle index so just return the middle index
            return middle

# Time: O(log n)
# Space: O(1)