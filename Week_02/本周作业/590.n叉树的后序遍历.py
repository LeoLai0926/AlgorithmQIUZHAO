#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # # 递归1
        # if not root: return []
        # tmp = []
        # for child in root.children:
        #     tmp += self.postorder(child)
        # tmp += [root.val]
        # return tmp

        # # 递归2
        # res = []
        # def helper(cur):
        #     if not cur: return
        #     for child in cur.children:
        #         helper(child)
        #     res.append(cur.val)
        # helper(root)
        # return res

        # 迭代
        if not root: return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in node.children:
                stack.append(child)
        return res[::-1]


# @lc code=end

