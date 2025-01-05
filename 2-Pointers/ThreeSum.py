# 15. 3Sum
# https://leetcode.com/problems/3sum/description/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        answer = []

        for i in range(n):
            if nums[i] > 0:  # since the array is sorted, if the first index is positive then the sum is too big already and we don't check
                break
            elif i > 0 and nums[i] == nums[i - 1]:  # if nums[i] == nums[i-1], then we have the same starting value which will yield duplicates so we shift ahead
                continue

            lo, hi = i + 1, n - 1 # the lo pointer starts just after the i, and hi pointer starts form the end

            while lo < hi:
                summ = nums[i] + nums[lo] + nums[hi] # calculate the sum of the three pointers that is i, lo nad hi
                if summ == 0: # if the sum is 0, we have one solution, so we append it and move the pointers
                    answer.append([nums[i], nums[lo], nums[hi]])
                    lo, hi = lo + 1, hi - 1

                    while lo < hi and nums[lo] == nums[lo - 1]: # we moved the lo pointer, and it is the same as the previous one we will get duplicates
                        lo += 1

                    while lo < hi and nums[hi] == nums[hi + 1]: # we moved the hi pointer, and it is the same as the previous one we will get duplicates
                        hi -= 1
                elif summ < 0: # if the sum is less than 0, then we have small sum so we need ot move right to get big numbers since the array is sorted
                    lo += 1
                else: # if the sum is more than 0, then we have large sum so we need ot move right to get big numbers since the array is sorted
                    hi -= 1

        return answer

# Time: O(n^2)
# Space: O(n) excluding the output