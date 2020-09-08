#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        res = 0

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "1":
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
                    res = max(res, dp[r][c])
        return res ** 2
                        

# @lc code=end

