#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(nums, cur):
            if len(cur) >= k:
                res.append(cur)
                return 
            
            for i in range(len(nums)):
                helper(nums[i+1:], cur + [nums[i]])
        helper([i for i in range(1, n+1)], [])
        return res
            


# @lc code=end

