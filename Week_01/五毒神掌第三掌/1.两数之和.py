#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for idx, val in enumerate(nums):
            cache[val] = idx

        for i, num in enumerate(nums):
            flag = cache.get(target - num)
            if flag and flag != i:
                return [i, flag]
# @lc code=end

