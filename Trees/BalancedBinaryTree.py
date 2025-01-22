# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True] # global stack

        def height(root): # we have to essentially find the max height of the tree
            if not root: # if we are at the last node, we have a height of 0, below it
                return 0

            left_height = height(root.left) # we find the left height
            if balanced[0] is False: # if at any point in analysis, we get the tree is ot balanced, we pause it nad don't proceed further
                return 0

            right_height = height(root.right) # we find the height of right tree

            diff = abs(left_height - right_height) # the absolute difference between the heights

            if diff > 1: # if the difference is more than 1, then it is not balanced, we set false and terminate the execution
                balanced[0] = False
                return 0

            return 1 + max(left_height, right_height) # we want to return the height of the node

        height(root)
        return balanced[0]

# Time: O(n)
# Space: O(n)