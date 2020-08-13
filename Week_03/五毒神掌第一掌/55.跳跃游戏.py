#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if not n: return False
        end_reachable = n-1
        for i in range(n-2, -1, -1):
            if nums[i] + i >= end_reachable:
                end_reachable = i
            
        return end_reachable == 0



# @lc code=end

