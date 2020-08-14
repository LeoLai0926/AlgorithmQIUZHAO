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
    def __init__(self):
        self.res = []
    def postorder(self, root: 'Node') -> List[int]:
        # if root:
        #     for child in root.children:
        #         self.postorder(child)
        #     self.res.append(root.val)
        # return self.res
        
        if not root: return []
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack.extend(cur.children)
        return res[::-1]



     
        
        
# @lc code=end

