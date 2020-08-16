#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        slow, fast = 0, 0
        while fast < n:
            if nums[slow] != nums[fast]:
                nums[slow+1], nums[fast] = nums[fast], nums[slow+1]
                slow += 1
            fast += 1
        return slow + 1

            

# @lc code=end

