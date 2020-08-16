#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
    #     res = []
    #     for n in range(num+1):
    #         res.append(self.countOne(n))
    #     return res

    # def countOne(self, n):
    #     cnt = 0
    #     while n:
    #         cnt += 1
    #         n &= (n-1)
    #     return cnt

        res = [0] * (num+1)
        for i in range(num+1):
            res[i] = res[i >> 1] + (i & 1)
        return res

# @lc code=end

