#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        # # 中序遍历
        # stack = []
        # cur = root
        # tmp = float('-inf')
        # while stack or cur:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     if cur.val <= tmp: return False
        #     tmp = cur.val
        #     cur = cur.right
        # return True
        




# @lc code=end

