#
# @lc app=leetcode.cn id=1480 lang=python3
#
# [1480] 一维数组的动态和
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums: return []
        res = [0]
        for n in nums:
            res.append(n+res[-1])
        return res[1:]
# @lc code=end

