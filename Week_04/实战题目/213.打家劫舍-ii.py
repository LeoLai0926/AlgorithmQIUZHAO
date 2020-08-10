#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            n = len(nums)
            if n == 0: return 0
            if n == 1: return nums[0]
            pre, cur = nums[0], max(nums[0], nums[1])
            for num in nums[2:]:
                pre, cur = cur, max(pre + num, cur)
            return cur
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))

# @lc code=end

