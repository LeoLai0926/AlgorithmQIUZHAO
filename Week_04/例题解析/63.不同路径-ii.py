#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid: return 0
        if not obstacleGrid[0]: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # # 二维数组
        # dp = [[0 for _ in range(n)] for _ in range(m)]

        # for row in range(m):
        #     if obstacleGrid[row][0] != 1:
        #         dp[row][0] = 1
        #     else:
        #         for i in range(row, m):
        #             dp[i][0] = 0
        #         break

        # for col in range(n):
        #     if obstacleGrid[0][col] != 1:
        #         dp[0][col] = 1
        #     else:
        #         for j in range(col, n):
        #             dp[0][j] = 0
        #         break
        
        # for r in range(1, m):
        #     for c in range(1, n):
        #         if obstacleGrid[r][c] == 1:
        #             dp[r][c] = 0
        #         else:
        #             dp[r][c] = dp[r-1][c] + dp[r][c-1]
        # return dp[m-1][n-1]

        # 一维数组
        dp = [0 for _ in range(n)]

        for col in range(n):
            if obstacleGrid[0][col] == 1:
                for c in range(col, n):
                    dp[c] = 0
                break
            else:
                dp[col] = 1
        
        for r in range(1, m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                else:
                    dp[c] += dp[c-1] if c > 0 else 0
        return dp[-1]




# @lc code=end

