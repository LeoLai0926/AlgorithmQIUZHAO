#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # 方法1
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # 方法2
        hashmap = {val:i for i, val in enumerate(nums)}
        for i in range(len(nums)):
            j = hashmap.get(target - nums[i])
            if j is not None and i != j:
                return [i, j]
# @lc code=end

