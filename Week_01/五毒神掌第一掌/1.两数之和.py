#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num] = i
        
        for i in range(len(nums)):
            idx = hashmap.get(target - nums[i])
            if idx and idx != i:
                return [i, idx]
        
# @lc code=end

