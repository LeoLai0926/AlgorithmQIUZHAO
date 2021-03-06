#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        # Terminator
        if not root:
            return 0
        
        # Process and Drill down
        dleft = self.maxDepth(root.left)
        dright = self.maxDepth(root.right)
        
        return 1 + max(dleft, dright)


# @lc code=end

