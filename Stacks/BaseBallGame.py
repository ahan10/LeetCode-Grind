# 682. Baseball Game
# https://leetcode.com/problems/baseball-game/description/
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = [] # use a stack

        for op in operations:
            if op == '+':
                add = stk[-1] + stk[-2] # if there is '+', we add the last two values
                stk.append(add)
            elif op == 'C': # if there is 'C', pop the top element
                stk.pop()
            elif op == 'D': # if there is 'D', peek the top element, multiply it by 2 and add it
                top = stk[-1]
                stk.append(top * 2)
            else: # else we have a number, add its integer value
                stk.append(int(op))
        # the final stack will be an integer array, so just return its sum
        return sum(stk)

# Time: O(n)
# Space: O(n)
