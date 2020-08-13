#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return -1
        if len(nums) == 1: return nums[0]
        if nums[0] < nums[-1]: return nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[mid + 1 + 1]


# @lc code=end

