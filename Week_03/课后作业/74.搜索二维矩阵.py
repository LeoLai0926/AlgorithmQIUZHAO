#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row * col-1
        while left <= right:
            mid = left + (right - left) // 2
            r = mid // col
            c = mid % col
            print(mid, r, c)
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False




# @lc code=end

