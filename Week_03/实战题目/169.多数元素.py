#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def helper(lb, rb):
            # Terminator
            if lb == rb:
                return nums[lb]

            # Split the big problems
            mid = (rb - lb) // 2 + lb

            left_res = helper(lb, mid)
            right_res = helper(mid+1, rb)

            # merge the result
            if left_res == right_res:
                return left_res

            nof_left = sum([1 for i in range(lb, rb+1) if nums[i] == left_res])
            nof_right = sum([1 for i in range(lb, rb+1) if nums[i] == right_res])
            
            return left_res if nof_left > nof_right else right_res


        return helper(0, len(nums)-1)



# @lc code=end

