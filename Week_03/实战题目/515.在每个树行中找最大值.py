#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        queue = collections.deque()
        queue.append((root, 0))
        res = []
        while queue:
            node, level = queue.popleft()

            # Terminator
            if level == len(res):
                res.append(float('-inf'))
            
            # Process current logic
            if node.val > res[level]:
                res[level] = node.val
            
            # Drill down
            if node.left: queue.append((node.left, level + 1))
            if node.right: queue.append((node.right, level + 1))

        return res



# @lc code=end

