#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        left = [height[0]]
        right = [height[-1]]
        
        for i in range(1, len(height)):
            left.append(max(left[-1], height[i]))
        for i in range(len(height)-2, -1, -1):
            right.append(max(height[i], right[-1]))
        
        return sum(left) + sum(right) - max(height) * len(height) - sum(height)
# @lc code=end

