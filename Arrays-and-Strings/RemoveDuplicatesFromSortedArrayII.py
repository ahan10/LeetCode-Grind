# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1 # index where we copy
        count = 1 # count of the number that we see
        for i in range(1, len(nums)): # iterate over the array
            if nums[i] == nums[i - 1]: # if we see that the current number is same as the previous one/ adjacent one we increase teh count
                count += 1
            else: # else we know we encountered a new number and we reset the count
                count = 1

            if count <= 2: # we want to copy till at max 2 occurrences, so we do that
                nums[k] = nums[i]
                k += 1
        # at last, we would have copied till k index and we return it
        return k