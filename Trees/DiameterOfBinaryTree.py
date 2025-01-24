# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/description/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = [0] # to use a variable as global in python, use it as a list of one element

        def height(node): # we use the same code as finding height of a BT with one modification
            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            diameter = left_height + right_height # diameter of a node is its left height + right height
            max_d[0] = max(max_d[0], diameter) # store the maximum diameter

            return 1 + max(left_height, right_height) # return the height of the node

        height(root)
        return max_d[0]

# Time: O(n)
# Space: O(h) height of tree