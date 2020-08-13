#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # if not height: return 0
        # tmp_max = 0
        # Sleft = 0
        # for col in height:
        #     tmp_max = max(col, tmp_max)
        #     Sleft += tmp_max
        # tmp_max = 0
        # Sright = 0
        # for col in height[::-1]:
        #     tmp_max = max(tmp_max, col)
        #     Sright += tmp_max
        
        # return Sleft + Sright - len(height) * max(height) - sum(height)

        maxval = 0
        left = []
        for col in height:
            max_val = max(max_val, col)
            left.append(max_val)
        
        max_val=0
        right = []
        for col in height[::-1]:
            max_val = max(max_val, col)
            right.append(max_val)

        res = 0
        for i, col in enumerate(height):
            res += min(left[i], right[i]) - col
        return res




# @lc code=end

