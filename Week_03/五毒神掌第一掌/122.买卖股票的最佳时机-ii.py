#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # for i in range(len(prices)-1):
        #     if prices[i] < prices[i+1]:
        #         profit += prices[i+1] - prices[i]
        # return profit

        # n = len(prices)
        # dp = [[0, 0] for _ in range(n+1)]
        # dp[0][0] = 0
        # dp[0][1] = float('-inf')
        # for i in range(1, n+1):
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
        #     dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i-1])
        # return dp[-1][0]

        n = len(prices)
        prei0, prei1 = 0, float('-inf')
        for i in range(n):
            curi0 = max(prei0, prei1 + prices[i])
            curi1 = max(prei1, prei0 - prices[i])
            prei0, prei1 = curi0, curi1
        return curi0



            

# @lc code=end

