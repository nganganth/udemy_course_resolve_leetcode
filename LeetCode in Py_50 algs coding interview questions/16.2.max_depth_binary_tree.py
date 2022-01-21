# Give a binary tree, find the maximum depth of the tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# 104. Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None: # root is a leaf node
            return 1

        left = self.maxDepthTree(root.left)
        right = self.maxDepthTree(root.right)
        return max(left, right) + 1
