#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            digits[i] = (digits[i] + 1) % 10
            if digits[i]:
                return digits
        
        digits = [0 for _ in range(len(digits)+1)]
        digits[0] = 1
        return digits
# @lc code=end

