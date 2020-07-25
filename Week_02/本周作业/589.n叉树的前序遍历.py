#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:

        # # 迭代
        # if not root: return []
        # res = []
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     res.append(node.val)
        #     for child in node.children[::-1]:
        #         stack.append(child)
        # return res

        # # 递归1
        # if not root: return []
        # res = [root.val]
        # for child in root.children:
        #     res.extend(self.preorder(child))
        # return res

        # 递归2
        if not root: return []
        res = []
        def helper(node):
            res.append(node.val)
            for child in node.children:
                helper(child)
        helper(root)
        return res


# @lc code=end

