# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/description/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_longest = 0
        n = len(nums)
        num_zeros = 0 # total number of zeros in our current window

        l = 0 # left pointer

        for r in range(n): # the right pointer moves through automatically
            if nums[r] == 0: # we keep the count of zeros in our current window
                num_zeros += 1

            while num_zeros > k: # while number of zeros are more than the number we can flip, the window is invalid so we have to make it valid
                if nums[l] == 0: # if we find a zero at the left index, we decrement the count since we omit it
                    num_zeros -= 1
                l += 1 # regardless of 1 or 0, shrink the window

            max_longest = max(max_longest, r - l + 1) # maximum is the current maximum or r - l + 1

        return max_longest

# Time: O(n)
# Space: O(1)