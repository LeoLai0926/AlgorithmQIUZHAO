#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(nums))]
        dp[0][0], dp[0][1]  = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                dp[i][0] = max(nums[i], nums[i] * dp[i-1][0])
                dp[i][1] = min(nums[i], nums[i] * dp[i-1][1])
            else:
                dp[i][0] = max(nums[i], nums[i] * dp[i-1][1])
                dp[i][1] = min(nums[i], nums[i] * dp[i-1][0])
        return max(dp)[0]

# @lc code=end