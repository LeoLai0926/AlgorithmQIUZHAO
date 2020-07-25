#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # # 递归 - (超时)
        # if n == 1: return 1
        # if n == 2: return 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)        

        # # 动态规划
        # if n < 3: return n
        # dp = [0] * n
        # dp[0] = 1
        # dp[1] = 2
        # for i in range(2, n):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[-1]

        # # 双指针
        # if n < 3: return n
        # p, q, r = 0, 0, 1
        # for _ in range(n):
        #     p = q
        #     q = r
        #     r = p + q
        # return r

# @lc code=end

