#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # # 递归
        # cache = {}
        # def helper(level, index):
        #     # Terminator 
        #     if level == len(triangle): return 0
        #     if f'{level}-{index}' in cache:
        #         return cache[f'{level}-{index}']

        #     # Process logic in current level
        #     left = helper(level + 1, index)
        #     right = helper(level + 1, index + 1)
        #     cache[f'{level}-{index}'] = min(left, right) + triangle[level][index]
        #     return cache[f'{level}-{index}']

        # return helper(0, 0)

        # 动态规划
        dp = triangle
        for level in range(len(triangle) - 2, -1, -1):
            for index in range(len(triangle[level])):
                dp[level][index] = min(triangle[level+1][index], 
                                        triangle[level+1][index+1]) + \
                                    triangle[level][index]
        return dp[0][0]


# @lc code=end

