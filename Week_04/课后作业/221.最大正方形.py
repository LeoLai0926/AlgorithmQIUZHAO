#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        if row == 0: return 0
        col = len(matrix[0])
        if col == 0: return 0

        res = 0
        dp = [[0 for _ in range(col)] for _ in range(row)]
        dp[0][0] = matrix[0][0]
        for r in range(row):
            dp[r][0] = 1 if matrix[r][0] == '1' else 0
        for c in range(col):
            dp[0][c] = 1 if matrix[0][c] == '1' else 0
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == "1":
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                res = max(res, dp[r][c])
        return res * res
# @lc code=end

