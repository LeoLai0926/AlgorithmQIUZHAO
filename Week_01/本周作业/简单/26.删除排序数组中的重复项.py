#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        slowP = 0
        for fastP in range(slowP, len(nums)):
            if nums[fastP] != nums[slowP]:
                nums[slowP+1] = nums[fastP]
                slowP += 1
        return slowP+1

# @lc code=end

