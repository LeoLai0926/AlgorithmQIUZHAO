#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        # # 递归
        # res = []
        # cur = []

        # def helper(index, maxlen, cur):
        #     if index == maxlen:
        #         res.append(cur[:])
        #         return

        #     helper(index+1, maxlen, cur)

        #     cur.append(nums[index])
        #     helper(index+1, maxlen, cur)

        #     cur.pop()

        # helper(0, len(nums), cur)
        # return res

        # 迭代
        res = [[]]
        for num in nums:
            res = res + [subset + [num] for subset in res]
        return res
# @lc code=end

