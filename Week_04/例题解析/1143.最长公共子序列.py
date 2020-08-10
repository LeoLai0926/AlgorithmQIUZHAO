#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)

        # # 二维数组
        # dp = [[0 for _ in range(l2)] for _ in range(l1)]
        
        # for col in range(l2):
        #     if text1[0] in text2[:col+1]:
        #         for i in range(col, l2):
        #             dp[0][i] = 1
        #         break
        
        # for row in range(l1):
        #     if text2[0] in text1[:row+1]:
        #         for j in range(row, l1):
        #             dp[j][0] = 1
        #         break
    
        # for r in range(1, l1):
        #     for c in range(1, l2):
        #         if text1[r] == text2[c]:
        #             dp[r][c] = dp[r-1][c-1] + 1
        #         else:
        #             dp[r][c] = max(dp[r-1][c], dp[r][c-1])

        # return dp[l1-1][l2-1]

        # 一维数组
        dp = [0 for _ in range(l2+1)]

        for col in range(1, l2+1):
            if text1[0] in text2[:col]:
                for i in range(col, l2+1): 
                    dp[i] = 1
                break

        for r in range(1, l1):
            tmp2 = 0
            for c in range(1, l2+1):
                tmp1 = dp[c]
                if text1[r] == text2[c-1]:
                    dp[c] = tmp2 + 1
                else:
                    dp[c] = max(dp[c], dp[c-1])
                tmp2 = tmp1
        return dp[-1]


# @lc code=end

