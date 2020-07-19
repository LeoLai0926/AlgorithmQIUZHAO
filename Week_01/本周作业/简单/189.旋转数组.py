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
        # 方法 1
        temp = nums[:]
        for i in range(len(temp)):
            nums[(i+k) % len(nums)] = temp[i]

# @lc code=end

