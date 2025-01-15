# 27. Remove Element
# https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 # pointer to location to place the element
        for j in range(len(nums)): # iterate over the whole array
            if nums[j] != val: # if the current value is not the value to be removed, copy it in the array
                nums[i] = nums[j]
                i += 1
        return i # the number of the copied items is the length of unique array