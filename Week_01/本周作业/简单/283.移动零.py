#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # 方法1
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[j] = nums[i]
        #         if i != j:
        #             nums[i] = 0
        #         j += 1

        # # 方法2
        # temp = [i for i in nums if i!= 0]
        # for i in range(len(temp)):
        #     nums[i] = temp[i]
        # for i in range(len(temp), len(nums)):
        #     nums[i] = 0

        # # 方法3
        # if not nums: return []
        # fast, slow = 0, 0
        # for fast in range(len(nums)):
        #     if nums[fast] != 0:
        #         nums[slow] = nums[fast]
        #         slow += 1
        # for i in range(slow, len(nums)):
        #     nums[i] = 0

        # 方法4
        if not nums: return []
        fast, slow = 0, 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1


            
# @lc code=end

