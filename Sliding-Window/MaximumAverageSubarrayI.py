# 643. Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/description/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curr_sum = 0

        for i in range(k): # build the initial window of first k elements, and find its sum
            curr_sum += nums[i]

        max_avg = curr_sum / k # find the average, and since it is our first window, it is the current max average

        for i in range(k, n): # now we iterate over the remaining range
            curr_sum += nums[i] # first we add the latest index, but now our window is one larger
            curr_sum -= nums[i - k] # so we decide to drop the first number of the window and get the window back in bounds

            avg = curr_sum / k # find the average
            max_avg = max(max_avg, avg) # store the max average

        return max_avg

# Time: O(n)
# Space: O(1)