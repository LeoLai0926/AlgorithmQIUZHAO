#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # # 二维数组DP
        # n = len(nums)
        # if n == 0: return 0
        # if n == 1: return nums[0]
        # dp = [[0 for _ in range(2)] for _ in range(n)]
        # dp[0][0] = 0
        # dp[0][1] = nums[0]
        # for i in range(1, n):
        #     dp[i][0] = max(dp[i-1])
        #     dp[i][1] = dp[i-1][0] + nums[i]
        # return max(dp[-1])

        # # 一维数组 DP
        # n = len(nums)
        # if n == 0: return 0
        # if n == 1: return nums[0]

        # dp = [0 for _ in range(n)]
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # for i in range(2, n):
        #     dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        # return max(dp)

        # 迭代 DP
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        pre, cur= nums[0], max(nums[0], nums[1])
        for num in nums[2:]:
            pre, cur = cur, max(pre + num, cur)
        return cur

# @lc code=end

