#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        # def helper(n):
        #     if n == 0: return 0
        #     if n & 1 == 1:
        #         return helper(n >> 1) + 1
        #     else:
        #         return helper(n >> 1)
        # return helper(n)

        # return bin(n).count('1')
        
        sum = 0
        while n:
            sum += 1
            n &= (n-1)
        return sum
# @lc code=end

