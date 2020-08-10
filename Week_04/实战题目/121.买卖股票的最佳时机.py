#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. 重复子问题
        # 2. 状态定义
        # 3. 状态转移方程
        # n = len(prices)
        # if n < 2: return 0
        # dp = [[0 for _ in range(2)] for _ in range(n)]
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]
        # for i in range(1, n):
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i]) 
        #     dp[i][1] = max(dp[i-1][1], - prices[i])
        # return dp[-1][0]

        n = len(prices)
        if n < 2: return 0
        pre_0, pre_1 = 0, -prices[0]
        for p in prices[1:]:
            cur_0 = max(pre_0, pre_1 + p)
            cur_1 = max(pre_1, -p)
            pre_0, pre_1 = cur_0, cur_1
        return cur_0


# @lc code=end

