# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for i in tokens:
            if i == '+': # if there is +, pop the last two, add then and put it in the stack
                b = stk.pop()
                a = stk.pop()

                stk.append(a + b)
            elif i == '*': # if there is *, pop the last two, multiply then and put it in the stack
                b = stk.pop()
                a = stk.pop()

                stk.append(a * b)
            elif i == '/': # if there is /, pop the last two, divide then and put it in the stack
                b = stk.pop()
                a = stk.pop()

                stk.append(int(a / b)) # int(a/b) truncates the answer towards 0
            elif i == '-': # if there is -, pop the last two, subtract b from a then and put it in the stack
                b = stk.pop()
                a = stk.pop()

                stk.append(a - b)
            else: # else put the integer version in
                stk.append(int(i))

        return stk[0] # at the end we will be left with only 1 element and return that

# Time: O(n)
# Space: O(n)