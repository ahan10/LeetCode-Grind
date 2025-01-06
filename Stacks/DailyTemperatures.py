# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/description/

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stk = []  # monotonic stack, is is in the order of increasing temperatures

        for i, t in enumerate(temperatures):  # we get the index and value of each elemet
            while stk and stk[-1][0] < t:  # while the stack is not empty and the temperature of the top of the stack is lower than the current temp, meaning we found a new higher temp
                stk_t, stk_i = stk.pop()  # we pop the tuple at top

                ans[stk_i] = i - stk_i  # the current index - index of lower temperature gives the distance to future day

            stk.append((t, i))  # no matter what append the current as a tuple, as we need to look a higher temperature for it ahead too

        return ans

        # Time: O(n)
        # Space: O(n)