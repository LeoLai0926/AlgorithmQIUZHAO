#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        dp = [0 for _ in range(n)]
        dp[0] = 0
        for i in range(1, n):
            if s[i] == "(": 
                dp[i] = 0
                continue
            if s[i] == ")":
                if s[i-1] == "(":
                    if i == 1:
                        dp[i] = 2
                    else:
                        dp[i] = dp[i-2] + 2
                else:
                    preidx = i - dp[i-1] - 1
                    if preidx < 0:
                        dp[i] = 0
                    else:
                        if s[preidx] == "(":
                            dp[i] = dp[i-1] + 2 + dp[preidx-1]
                        else:
                            dp[i] = 0
        return max(dp)

# @lc code=end

