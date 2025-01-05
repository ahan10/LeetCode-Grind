# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/description/
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0]) # sort the array based on the first elements of the sub arrays

        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:  # merged[-1][1] means the right element of last element of merged
                # if the merged array is empty, or the right most element of the last merged array is less than the first element of the current pair; that is there is no overlap
                merged.append(interval) # append the current interval
            else: # else if there is an interval or the above condition does not match
                merged[-1] = merged[-1][0], max(merged[-1][1], interval[1]) # the last merged interval has the first element of the last merged interval and
                            # the ending of interval is the max of the previous end or the end of current interval

        return merged

# Time: O(n log n)
# Space: O(n)