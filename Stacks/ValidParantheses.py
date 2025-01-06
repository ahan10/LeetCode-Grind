# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stk = [] # use stack as the data type

        for i in s:
            if i == '(' or i == '[' or i == '{':  # if it is opening brace, push it in the stack
                stk.append(i)
            # if closing bracket, and the stk is not empty and the top is opening of the same type, then pop
            elif i == ')' and stk and stk[-1] == '(':
                stk.pop()
            elif i == ']' and stk and stk[-1] == '[':
                stk.pop()
            elif i == '}' and stk and stk[-1] == '{':
                stk.pop()
            else:  # if none of the conditions do match, then return False that is, it is not valid parentheses
                return False

        return not stk  # after all the stacks operations have been done, return true if the stk is empty else false