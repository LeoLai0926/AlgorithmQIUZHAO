#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # # 递归
        # if not root:
        #     return []
        # return [root.val] + \
        #     self.preorderTraversal(root.left) + \
        #     self.preorderTraversal(root.right)

        # 迭代
        stack = []
        res = []
        cur = root
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return res
        
# @lc code=end

