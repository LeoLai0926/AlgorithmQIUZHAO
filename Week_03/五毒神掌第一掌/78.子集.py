#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        # res = []

        # def helper(idx, maxlen, cur):
        #     if idx == maxlen:
        #         res.append(cur[:])
        #         return 

        #     helper(idx + 1, maxlen, cur)
        #     helper(idx + 1, maxlen, cur + [nums[idx]])
        
        # helper(0, len(nums), [])
        # return res

        res = [[]]
        for num in nums:
            res = res + [subset + [num] for subset in res]
        return res

        
# @lc code=end

