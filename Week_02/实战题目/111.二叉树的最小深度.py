#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # Terminator
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        # Process and Drill down
        dleft = self.minDepth(root.left)
        dright = self.minDepth(root.right)

        # Complete terminator
        if not root.left or not root.right:
            return 1 + max(dleft, dright)

        return 1 + min(dleft, dright)
# @lc code=end

