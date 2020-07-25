#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(nums, cur):
            if not nums:
                res.append(cur)
                return None
            for i in range(len(nums)):
                helper(nums[:i] + nums[i+1:], cur+[nums[i]])
        helper(nums, [])
        return res
# @lc code=end

