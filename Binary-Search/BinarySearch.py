# 704. Binary Search
# https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 # 2 pointers at left and right

        while left <= right: # until the pointers aren't equal
            middle = (left + right) // 2 # we find the middle index
            if nums[middle] == target: # if the nums at middle index is the target, return the index, and job is done
                return middle
            elif nums[middle] > target: # if the nums at middle index is larger than the target, then the number potentially lies between left pointer and middle, so now update the right pointer to just before the middle index
                right = middle - 1
            else: # if the nums at middle index is smaller than the target, then the number potentially lies between middle pointer and right pointer, so now update the left pointer to just after the middle index
                left = middle + 1
        # if the element is not found return -1
        return -1

# Time: O(log n)
# Space: O(1)