#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            val = nums[mid]
            if val == target:
                return mid
            if val >= nums[0]:
                if nums[0] <= target < val:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if val < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
            


# @lc code=end

