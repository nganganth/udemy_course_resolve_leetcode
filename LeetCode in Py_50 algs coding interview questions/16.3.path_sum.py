# https://leetcode.com/problems/path-sum/
# Path Sum
# Given a binary tree and a target; Find if a root to leaf path exist where 
# summation of all elements on the path equals target

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasSum(self, root, sum, cur):
        if root is None: 
            return False
        cur += root.val
        if cur == sum and root.left is None and root.right is None:
            return True
        
        return (self.hasSum(root.right, sum, cur) or self.hasSum(root.left, sum, cur))

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.hasSum(root, targetSum, 0)
