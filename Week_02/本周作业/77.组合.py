#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # # 方法1
        # res = []
        # def helper(nums, cur):
        #     if len(cur) == k:
        #         res.append(cur)
        #         return 
        #     for i in range(len(nums)):
        #         helper(nums[i+1:], cur+[nums[i]])
        # helper(list(range(1, n+1)), [])
        # return res

        # 方法2
        if n <= 0 or k <= 0 or k > n:
            return []
        def helper(start, k, n, pre, res):
            if len(pre) == k:
                res.append(pre[:])
                return 
            
            for i in range(start, n+1):
                pre.append(i)
                helper(i+1, k, n, pre, res)
                pre.pop()

        res = []
        helper(1, k, n, [], res)
        return res

# @lc code=end

