#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        # # 迭代(队列)
        # from collections import deque
        # if not root: return []
        # res = []
        # dq = deque()
        # dq.append(root)
        # while dq:
        #     tmp = []
        #     for _ in range(len(dq)):
        #         node = dq.popleft()
        #         tmp.append(node.val)
        #         dq.extend(node.children)
        #     res.append(tmp)
        # return res

        # BFS
        if not root: return []
        res = []
        level = [root]
        while level:
            res.append([node.val for node in level])
            level = [child for node in level for child in node.children]
        return res


        
# @lc code=end

