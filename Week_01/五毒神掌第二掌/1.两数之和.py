#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {val:idx for idx, val in enumerate(nums)}
        for i, num in enumerate(nums):
            idx = hashmap.get(target - num)
            if idx and idx != i:
                return [i, idx]
        
# @lc code=end

