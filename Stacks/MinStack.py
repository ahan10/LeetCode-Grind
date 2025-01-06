# 155. Min Stack
# https://leetcode.com/problems/min-stack/description/

class MinStack:
    # we make 2 stacks
    def __init__(self):
        self.stk = []  # normal stack
        self.min_stk = []  # min stack, where minimum is always at the top

    def push(self, val: int) -> None:
        self.stk.append(val)  # append the val in normal one

        if not self.min_stk:  # if the min stack is empty, just put the current element
            self.min_stk.append(val)
        elif self.min_stk[-1] < val:  # if the top of min stack is less than val, then duplicate the min vale
            self.min_stk.append(self.min_stk[-1])
        else:  # else either the two values are equal or val is smaller, in that case add that to the top
            self.min_stk.append(val)

    def pop(self) -> None:
        self.stk.pop()  # remove the top element
        self.min_stk.pop()  # remove the top element

    def top(self) -> int:
        return self.stk[-1]  # we need to return the topmost of normal stack

    def getMin(self) -> int:
        return self.min_stk[-1]  # we need to return the topmost of min stack

# Time: O(1) {since all we do is pop, append and peek which are all done in O(1)}
# Space: O(n) {we have a n length stack}

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()