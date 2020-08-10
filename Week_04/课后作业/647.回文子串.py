#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        res = 0
        dp = [[False for _ in range(n)] for _ in range(n)]

        for d in range(n):      # 字符串长度为 1 时
            dp[d][d] = True
        
        for c in range(1, n):
            for r in range(c-1, -1, -1):
                if s[r] == s[c]:
                    if c - r == 1:   # 字符串长度为 2 时
                        dp[r][c] = True
                    else:
                        dp[r][c] = dp[r+1][c-1]
                else:
                    dp[r][c] = False
                res += dp[r][c]
        return res + n
        
# @lc code=end

