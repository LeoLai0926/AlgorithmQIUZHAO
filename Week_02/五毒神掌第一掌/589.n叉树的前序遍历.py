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
    def __init__(self):
        self.tranversal_path = []
    def preorder(self, root: 'Node') -> List[int]:
        # if root:
        #     self.tranversal_path.append(root.val)
        #     for child in root.children:
        #         self.preorder(child)
        # return self.tranversal_path
        
        if not root: return []
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            for child in cur.children[::-1]:
                if child: stack.append(child)
        return res

# @lc code=end

