#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            s = ''
            if (i % 3 != 0) and (i % 5 != 0):
                res.append(str(i))
                continue
            if i % 3 == 0:
                s += 'Fizz'
            if i % 5 == 0:
                s += 'Buzz'
            res.append(s)
        return res
# @lc code=end

