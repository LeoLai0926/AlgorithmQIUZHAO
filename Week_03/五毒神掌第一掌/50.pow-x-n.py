#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache = {}
        def helper(x, n):
            if n in cache:
                return cache[n]
            else:
                if n == 0:
                    return 1
                val = helper(x, n // 2)
                if n % 2 == 0:
                    cache[n] = val * val
                else:
                    cache[n] = val * val * x
                return cache[n]
        return helper(x, n) if n > 0 else 1/helper(x, -n)


# @lc code=end

