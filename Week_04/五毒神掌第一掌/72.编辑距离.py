#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1: return len(word2)
        if not word2: return len(word1)

        n1, n2 = len(word1), len(word2)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

        for r in range(n1+1):
            dp[r][0] = r
        for c in range(n2+1):
            dp[0][c] = c
        for r in range(1, n1+1):
            for c in range(1, n2+1):
                if word1[r-1] == word2[c-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
        return dp[-1][-1]
# @lc code=end

