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
        # # 1. 利用额外空间
        # tmp = nums[:]
        # for i in range(len(nums)):
        #     nums[ (i + k) % len(nums) ] = tmp[i]

        # 2. 不利用额外空间
        k %= len(nums)
        nums = self.reverse(nums)
        nums[:k] = self.reverse(nums[:k])
        nums[k:] = self.reverse(nums[k:])

    def reverse(self, arr):
        left, right = 0, len(arr)-1
        while left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

# @lc code=end

