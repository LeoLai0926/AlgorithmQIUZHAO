#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(nums, cur):
            if not nums:
                if cur not in res:
                    res.append(cur)
                return

            for i in range(len(nums)):
                helper(nums[:i] + nums[i+1:], cur + [nums[i]])
        
        helper(nums, [])
        return res
# @lc code=end

