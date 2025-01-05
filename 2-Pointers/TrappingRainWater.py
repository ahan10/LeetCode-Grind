# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/description/

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall = r_wall = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        for i in range(n):  # iterate over the height array and store the max to the left and right of current indexes
            j = -i - 1  # in python, negative index means start from right
            max_left[i] = l_wall  # initially both are 0
            max_right[j] = r_wall  # initially both are 0

            l_wall = max(l_wall, height[i])  # max height of the wall is it the current, or we have seen a max height to the left
            r_wall = max(r_wall, height[j])  # max height of the wall is it the current, or we have seen a max height to the right

        summ = 0

        for i in range(n):
            potential = min(max_left[i], max_right[i])  # potential water can be stored is the max to left - max to right at a particular index
            actual_water = potential - height[i]  # actual water = potential - height of the column ath that index

            if actual_water > 0: # add water only if positive
                summ += actual_water

        return summ
# Time: O(n)
# Space: O(n)