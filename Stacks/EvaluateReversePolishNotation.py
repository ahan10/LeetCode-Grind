# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
from math import ceil, floor
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for i in tokens:
            if i in '+-*/': # if there is any operation, pop the last two
                b, a = stk.pop(), stk.pop()
                if i == '+': # if there is +, add then and put it in the stack
                    stk.append(a + b)
                elif i == '*': # if there is *, multiply then and put it in the stack
                    stk.append(a * b)
                elif i == '-':  # if there is -, subtract b from a then and put it in the stack
                    stk.append(a - b)
                else: # if there is /, divide then and put it in the stack
                    div = a/b
                    if div < 0: # if the division result is negative store the ceiling value
                        stk.append(ceil(div))
                    else: # if the division result is positive store the floor value
                        stk.append(floor(div))
            else: # else put the integer version in
                stk.append(int(i))

        return stk[0] # at the end we will be left with only 1 element and return that

# Time: O(n)
# Space: O(n)