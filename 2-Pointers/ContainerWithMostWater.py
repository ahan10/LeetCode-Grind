# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        n = len(height)
        l, r = 0, n - 1

        while l < r:
            area = min(height[l], height[r]) * (r - l)  # max area = height of smallest pole times the width (l-r)
            maxArea = max(maxArea, area)  # keep the max area

            # we want the bigger pole

            if height[l] < height[r]:  # if left pole is shorter, move right
                l += 1
            else:  # if the right pole is shorter or both are equal, move left
                r -= 1

        return maxArea
# Time: O(n)
# Space: O(1)