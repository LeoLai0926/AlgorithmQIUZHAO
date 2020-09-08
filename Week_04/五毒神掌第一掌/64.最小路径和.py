#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])

        for r in range(1, m):
            grid[r][0] += grid[r-1][0]
        for c in range(1, n):
            grid[0][c] += grid[0][c-1]
        
        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        
        return grid[-1][-1]
# @lc code=end

