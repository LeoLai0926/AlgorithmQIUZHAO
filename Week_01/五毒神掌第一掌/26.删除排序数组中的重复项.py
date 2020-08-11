#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 1
        p1, p2 = 0, 1
        while p2 < len(nums):
            if nums[p1] != nums[p2]:
                nums[p1+1], nums[p2] = nums[p2], nums[p1+1]
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        return p1+1

# @lc code=end

