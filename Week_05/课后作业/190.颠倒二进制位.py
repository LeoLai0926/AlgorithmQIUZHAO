#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        ret, pow = 0, 31
        while n:
            ret += (n & 1) << pow
            n = n >> 1
            pow -= 1
        return ret
        
# @lc code=end

