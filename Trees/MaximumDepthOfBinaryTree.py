# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: # if we encounter numm, that is we have reached at the end of the current trace
            return 0 # return 0 we have a depth of 0 after this
        left = self.maxDepth(root.left) # find the depth of left side
        right = self.maxDepth(root.right) # find the depth of right side
        return max(left, right) + 1 # we want to keep the maximum depth + 1; (+1 to account the current node)

# Time: O(n)
# Space: O(h) {h = height of the call stack}