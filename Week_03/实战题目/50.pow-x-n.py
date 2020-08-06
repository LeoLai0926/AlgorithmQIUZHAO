#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x

            tmp = helper(x, n // 2)
            if n % 2 == 0:
                return tmp * tmp
            else:
                return tmp * tmp * x

        if n < 0:
            return 1/helper(x, -n)
        else:
            return helper(x, n)


# @lc code=end

