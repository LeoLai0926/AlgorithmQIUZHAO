#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # def reverse(nums):
        #     i, j = 0, len(nums) - 1
        #     while i < j:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1
        #         j -= 1
        #     return nums
        # k = k % len(nums)
        # nums = reverse(nums)
        # nums[:k] = reverse(nums[:k])
        # nums[k:] = reverse(nums[k:])
        
        tmp = nums[:]
        n = len(nums)
        for i in range(len(nums)):
            nums[(i + k) % n] = tmp[i]


# @lc code=end

