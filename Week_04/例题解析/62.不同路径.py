#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # # 二维数组
        # dp = [[0 for _ in range(n)] for _ in range(m)]

        # for row in range(m):
        #     dp[row][0] = 1
        # for col in range(n):
        #     dp[0][col] = 1
        
        # for r in range(1, m):
        #     for c in range(1, n):
        #         dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        # return dp[m-1][n-1]

        # 一维数组
        dp = [1 for _ in range(n)]

        for _ in range(1, m):
            for c in range(1, n):
                dp[c] += dp[c-1]
        return dp[-1]

# @lc code=end

