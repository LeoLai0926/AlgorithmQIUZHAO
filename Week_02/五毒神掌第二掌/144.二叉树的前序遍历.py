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
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # if root:
        #     self.res.append(root.val)
        #     self.preorderTraversal(root.left)
        #     self.preorderTraversal(root.right)
        # return self.res

        # # 迭代 1
        # res = []
        # stack = [root]
        # if not root: return res
        # while stack:
        #     cur = stack.pop()
        #     res.append(cur.val)
        #     if cur.right:
        #         stack.append(cur.right)
        #     if cur.left:
        #         stack.append(cur.left)
        # return res

        # 迭代 2
        res = []
        stack = []
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

