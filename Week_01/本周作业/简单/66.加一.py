#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # # 方法1
        # num = int(''.join([str(i) for i in digits]))
        # return [int(i) for i in str(num+1)]            

        # # 方法2
        # num = sum([val*10**(len(digits)-i-1) for i, val in enumerate(digits)])
        # return [int(i) for i in str(num+1)]

        # 方法3
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                return digits
        
        digits = [0] * (len(digits)+1)
        digits[0] = 1
        return digits

# @lc code=end

