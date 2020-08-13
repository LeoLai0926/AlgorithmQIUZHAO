#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def helper(lb, rb):
            if lb == rb:
                return nums[lb]
            
            mid = lb + (rb - lb) // 2
            left = helper(lb, mid)
            right = helper(mid+1,rb)

            if left == right: return left

            nof_left = sum([left == num for num in nums[lb:rb+1]])
            nof_right = sum([right == num for num in nums[lb:rb+1]])
            return left if nof_left > nof_right else right
        return helper(0, len(nums)-1)
# @lc code=end

