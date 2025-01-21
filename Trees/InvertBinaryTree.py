# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: # if we encounter a null node, that is end of the path for that node on left, we return null
            return None

        root.left, root.right = root.right, root.left # swap the left and right
        self.invertTree(root.left) # iterate over the left
        self.invertTree(root.right) # iterate over the right

        return root # since we did it kind of in place, we return the root itself

# Time: O(n)
# Space: O(h) {call stack of size of the tree from the node which is h}