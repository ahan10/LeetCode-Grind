# 16. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf') # our closest is far away
        n = len(nums)

        for i in range(n):

            if i > 0 and nums[i] == nums[i - 1]:  # if nums[i] == nums[i-1], then we have the same starting value which will yield duplicates so we shift ahead
                continue
            lo, hi = i + 1, n - 1
            while lo < hi:
                summ = nums[i] + nums[lo] + nums[hi] # we calculate the sum
                if summ == target: # if our sum = target, we can't do better so return the sum
                    return summ
                if abs(closest - target) > abs(summ - target): # we find the distance between target and current sum and target and closest sum; return the smaller one
                    closest = summ
                elif summ < target: # if the sum is less than 0, then we have small sum so we need to move right to get big numbers since the array is sorted
                    lo += 1
                else: # if the sum is more than 0, then we have large sum so we need ot move right to get big numbers since the array is sorted
                    hi -= 1

        return closest

# Time: O(n^2)
# Space: O(n) (space for sort)