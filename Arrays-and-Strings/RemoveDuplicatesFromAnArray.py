# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1  # this is the place where we place the character, essentially removing duplicate

        for i in range(1, len(nums)):  # we start from the first index
            if nums[i] != nums[i - 1]:  # we have found two unique adjoining characters, with i being the unique
                nums[k] = nums[
                    i]  # we place the unique at the position it is supposed to be once we remove the duplicates
                k += 1

        return k

# Time:O(n)
# Space: O(1)