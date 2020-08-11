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
    #     n = len(nums)
    #     k = k % n
    #     if n < 2: 
    #         pass
    #     else:
    #         self.reverse(nums, 0, n-1)
    #         self.reverse(nums, 0, k-1)
    #         self.reverse(nums, k, n-1)

    # def reverse(self, nums, s, t):
    #     while s < t:
    #         nums[s], nums[t] = nums[t], nums[s]
    #         s += 1
    #         t -= 1

        tmp = nums[:]
        n = len(nums)
        for i in range(n):
            nums[(i+k) % n] = tmp[i]


# @lc code=end

