#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n = len(prices)
        # if n < 2: return 0
        # dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(n)]
        # dp[0][2][0], dp[0][2][1] = 0, -prices[0]
        # dp[0][1][0], dp[0][1][1] = 0, -prices[0]
        # for i in range(1, n):
        #     for k in range(2, 0, -1):
        #         dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        #         dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        # return dp[-1][2][0]

        n = len(prices)
        if n < 2: return 0
        pre_20, pre_21 = 0, float('-inf')
        pre_10, pre_11 = 0, float('-inf')
        for p in prices:
            cur_20 = max(pre_20, pre_21 + p)
            cur_21 = max(pre_21, pre_10 - p)
            cur_10 = max(pre_10, pre_11 + p)
            cur_11 = max(pre_11, - p)

            pre_20, pre_21 = cur_20, cur_21
            pre_10, pre_11 = cur_10, cur_11
        return cur_20



# @lc code=end

